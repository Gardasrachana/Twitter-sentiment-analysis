# Flask app (app.py)
from flask import Flask, request, render_template
import pickle
import re
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

app = Flask(__name__)

# Define the text preprocessing function based on the notebook
def clean_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower().split()
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    text = [ps.stem(word) for word in text if not word in stop_words]
    return ' '.join(text)

# Load the trained model and vectorizer
try:
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
except FileNotFoundError as e:
    print(f"An error occurred: {e}")
    raise e

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        cleaned_message = clean_text(message)
        vect = vectorizer.transform([cleaned_message])
        prediction = model.predict(vect)[0]
        # Map numerical prediction to sentiment text
        prediction_text = 'Positive' if prediction == 1 else 'Negative' if prediction == -1 else 'Neutral'
        emoji_url = ('https://github.com/googlefonts/noto-emoji/blob/main/png/128/emoji_u1f603.png?raw=true'
                     if prediction_text == 'Positive'
                     else 'https://github.com/googlefonts/noto-emoji/blob/main/png/128/emoji_u1f641.png?raw=true')
        return render_template('result.html', prediction_text=prediction_text, emoji_url=emoji_url)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=8080)

