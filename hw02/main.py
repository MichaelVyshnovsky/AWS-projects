"""Runs a script that hosts a web server that allows for image upload and image viewing"""
import os
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for, send_from_directory


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    """Checks for file types that are allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    """Handles the action if the users hits the upload file button"""
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return redirect(url_for('view_files'))
    return render_template('index.html')

@app.route('/uploads')
def view_files():
    """Allows the user to view all images that were uploaded"""
    files = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.isfile(file_path):
            file_info = {
                'name': filename,
                'size': os.path.getsize(file_path),
                'modified': datetime.fromtimestamp(
                    os.path.getmtime(file_path)
                ).strftime('%Y-%m-%d %H:%M:%S')
            }
            files.append(file_info)
    return render_template('uploads.html', files=files)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Shows the an image from the directory"""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=5000)
