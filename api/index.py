# app.py

import vercel_blob
from flask import Flask, request, render_template, redirect
import dotenv


app = Flask(__name__)
dotenv.load_dotenv()


@app.route('/')
def index():
    resp = vercel_blob.list()
    return render_template('index.html', files=resp.get('blobs'))

if __name__ == '__main__':
    app.run()
