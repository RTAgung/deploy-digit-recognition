from flask import Flask, render_template, request, send_from_directory
import joblib
import cv2
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/uploads/'
model = joblib.load('model.h5')

class_dict = {0: 'Cat (Kucing)', 1: 'Dog (Anjing)'}

def predict_label(img_path):
    return class_dict[0]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.files:
            image = request.files['image']
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(img_path)
            prediction = predict_label(img_path)
            return render_template('index.html', uploaded_image=image.filename, prediction=prediction)

    return render_template('index.html')

@app.route('/display/<filename>')
def send_uploaded_image(filename=''):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)