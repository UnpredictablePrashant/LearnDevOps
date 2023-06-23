from flask import Flask
import logging
 
app = Flask(__name__)
 
logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
 
@app.route('/blogs')
def blog():
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    return f"Welcome to the Blog"
 
@app.route('/critical')
def critical():
    app.logger.critical('Critical level log')
    return f'ERROR'
app.run(debug=True)
