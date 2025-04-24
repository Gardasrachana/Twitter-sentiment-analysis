 💬 Twitter Sentiment Analysis (Machine Learning Project)

A web-based tool for classifying the sentiment of Twitter posts using various supervised ML algorithms like Logistic Regression, SVM, Decision Tree, Random Forest, and more.



 🔍 Objective

To design and develop a sentiment analysis tool using machine learning that classifies tweets into **positive** or **negative** sentiment classes. The project uses a Kaggle dataset and implements a Flask-based web app for interactive use.

---

 🔧 Technology Stack

- **Python**
- **Scikit-Learn** for ML model training
- **NLTK / spaCy** for Natural Language Processing
- **Flask** for web interface
- **HTML/CSS** for front-end
- **Local file storage** for models & datasets

---

 🧠 ML Algorithms Used

- Logistic Regression ✅ (Best Performance – Accuracy: **81.19%**)
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest
- Naive Bayes

---

 🔄 Data Preprocessing

- Cleaning tweets (removing symbols, links)
- Tokenization and stopword removal
- Stemming/Lemmatization
- Vectorizing (TF-IDF or CountVectorizer)

---

 🖥️ Web Application Design

 Frontend:
- HTML + CSS
- Simple text input form
- “Check Sentiment” button

 Backend:
- Flask handles user requests
- Input sent to trained Logistic Regression model
- Sentiment displayed in real-time

---

 ✅ Evaluation & Results

- Accuracy: 81.19%
- Confusion Matrix
- Precision, Recall, F1-score
- Logistic Regression outperformed other models

---

 🚀 Future Enhancements

- Add support for more social media sources
- Extend to multi-class sentiment (neutral/very positive)
- Deploy on cloud (AWS/GCP)
- Connect with stock trend visualizations

---

 📚 References

- [Twitter Dataset - Kaggle](https://www.kaggle.com/yash612/stockmarket-sentiment-dataset)
- [Python Pickle](https://pythonprogramming.net/python-pickle-module-save-objects-serialization/)
- [Flask Deployment Guide](https://towardsdatascience.com/https-medium-com-radecicdario-next-level-data-visualization-dashboard-app-with-bokeh-flask-c588c9398f9)

