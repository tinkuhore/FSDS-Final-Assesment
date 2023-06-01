from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model/kmeans_model.joblib')

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint for music genre prediction
@app.route('/predict', methods=['POST'])
def predict_genre():
    # Get the audio file from the form data
    audio_file = request.files['audio']

    # Perform any necessary preprocessing on the audio file (e.g., feature extraction)

    # Make predictions using the loaded model
    predictions = model.predict(audio_file)

    # Format the predictions as desired (e.g., convert to a list)
    predictions_list = predictions.tolist()

    # Return the predictions as a JSON response
    return jsonify({'predictions': predictions_list})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
