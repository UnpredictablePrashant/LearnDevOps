## Installing the libraries and zipping it

```bash
pip install pillow -t .
zip -r lambda_function.zip .
```

create the bucket:

```bash
aws s3 mb s3://devopsb3
aws iam create-role --role-name lambda-s3-execution-role --assume-role-policy-document file://imageCompression/trust-policy.json
aws iam attach-role-policy --role-name lambda-s3-execution-role --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

```bash
aws lambda create-function --function-name image-compression-function --runtime python3.8 --role arn:aws:iam::515210271098:role/lambda-s3-execution-role --handler imageCompression.lambda_function.lambda_handler --timeout 30 --memory-size 128 --code S3Bucket=devopsb3,S3Key=imageCompression.zip --region us-east-1
aws s3api put-bucket-notification-configuration --bucket learningdevops   --notification-configuration file://imageCompression/notification-config.json
aws lambda update-function-code --function-name image-compression-function --s3-bucket devopsb3  --s3-key imageCompression.zip --region us-east-1
```
