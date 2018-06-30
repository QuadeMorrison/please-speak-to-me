#!/usr/bin/env python3
from flask import Flask, request, send_from_directory
import os

app = Flask(__name__, static_folder='./dist/static')

@app.route('/')
def root():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
