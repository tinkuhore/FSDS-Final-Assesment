from flask import Flask, render_template, request
import joblib
import nltk
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load the saved model
model = joblib.load('model.joblib')

# Preprocess function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)
    text = re.sub(r"\d+", "number", text)
    stopwords_list = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stopwords_list]
    text = ' '.join(words)
    return text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the user inputs
    question1 = request.form['question1']
    question2 = request.form['question2']

    # Preprocess the inputs
    question1 = preprocess_text(question1)
    question2 = preprocess_text(question2)

    # Apply TfidfVectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([question1, question2])

    # Calculate cosine similarity and convert to DataFrame
    similarity_matrix = cosine_similarity(tfidf_matrix)
    similarity_df = pd.DataFrame(similarity_matrix, columns=['Similarity'])

    # Load and predict using the saved model
    prediction = model.predict(similarity_df)

    # Convert binary output to 'Yes' or 'No'
    prediction = 'Yes' if prediction[0] == 1 else 'No'

    # Calculate prediction accuracy
    accuracy = model.score(similarity_df, [1])

    return render_template('index.html', prediction=prediction, accuracy=accuracy)

if __name__ == '__main__':
    app.run(debug=True)
