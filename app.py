from flask import Flask, render_template, request, send_from_directory
import joblib
import cv2
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/uploads/'
model = joblib.load('model.pkl')
scaler = joblib.load('std_scaler.bin')

class_dict = {0: 'Nol', 1: 'Satu', 2: 'Dua', 3: 'Tiga', 4: 'Empat', 5: 'Lima', 6: 'Enam', 7: 'Tujuh', 8: 'Delapan', 9: 'Sembilan'}

def predict_label(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = cv2.resize(img, (22, 22), interpolation = cv2.INTER_AREA)
    
    img = img.flatten()
    img = img.reshape(1,-1)
    img = scaler.transform(img)

    classes = model.predict(img)
    print("Digit Hasil Prediksi :", classes[0])
    
    return class_dict[classes[0]]

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