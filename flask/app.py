from flask import Flask, render_template, request
import os
from fst import get_result


app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_file():
    content = request.files['content']
    style = request.files['style']
    content.save('content.jpg')
    style.save('style.jpg')
    get_result('content.jpg', 'style.jpg')
    os.remove('content.jpg')
    os.remove('style.jpg')
    return render_template('success.html')

if __name__ == '__main__':
    app.run('localhost', '3000')