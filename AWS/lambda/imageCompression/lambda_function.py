import os
import boto3
from PIL import Image
from io import BytesIO

s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    if 'upload/' not in key:
        return {
            'statusCode': 200,
            'body': 'Not an image in the upload folder. No action taken.'
        }
    response = s3.get_object(Bucket=bucket, Key=key)
    image_data = response['Body'].read()
    compressed_image_data = compress_image(image_data)
    new_key = key.replace('upload/', 'finalOutput/compressed_')
    s3.put_object(Bucket=bucket, Key=new_key, Body=compressed_image_data)

    return {
        'statusCode': 200,
        'body': 'Image compressed and stored in the finalOutput folder.'
    }

def compress_image(image_data):
    image = Image.open(BytesIO(image_data))
    image.save(BytesIO(), format='JPEG', quality=80)
    compressed_image_data = BytesIO()
    image.save(compressed_image_data, format='JPEG', quality=80)
    return compressed_image_data.getvalue()
