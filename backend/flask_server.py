from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():

    return 'The Flask Server has started successfully on port 5000!'


@app.route('/query/<int:post_data>')
def query_test(post_data):

    return 'Query Returned: %d' % post_data


@app.route('/post_test', methods=['GET', 'POST'])
def post_test():

    if(request.method == 'GET'):
        return 'This is a post request test, use post method'

    if(request.method == 'POST'):
        return request.data
