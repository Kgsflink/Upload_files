import argparse
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'files' in request.files:
        files = request.files.getlist('files')
        for file in files:
            # Ensure the directory exists, create it if not
            if not os.path.exists('/sdcard/insta'):
                os.makedirs('/sdcard/insta')
            # Save the file to /sdcard/insta
            file.save('/sdcard/insta/' + file.filename)
        return 'Files uploaded successfully!', 200
    else:
        return 'No files found in request', 400

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=5000, help="Port number")
    args = parser.parse_args()
    app.run(debug=True, host='0.0.0.0', port=args.port)
