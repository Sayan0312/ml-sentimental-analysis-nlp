# Sentimental Analysis using NLP

This project is a **Sentimental (Emotion) Analysis system** built using **Machine Learning and Natural Language Processing (NLP)**.
It predicts the **emotion behind a given text** using a trained ML model and a **TF-IDF Vectorizer**, deployed with **Streamlit**.

---

## 🔥 Emotions Supported

The model classifies text into **6 emotion classes**:

* 😊 Joy
* 😢 Sadness
* 😡 Anger
* 😨 Fear
* ❤️ Love
* 😲 Surprise

---

## 🧠 Tech Stack

* **Python**
* **Scikit-learn**
* **TF-IDF Vectorizer**
* **Streamlit**
* **Pickle**

---

## 📂 Project Structure

```
sentimental_analysis/
│── app.py
│── emotion_model.pkl
│── tfidf_vectorizer.pkl
│── requirements.txt
│── .gitignore
│── README.md
│── venv/
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/sentimental_analysis.git
cd sentimental_analysis
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```


---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

The app will open in your browser 🚀

---

## 🧪 Model Details

* **Feature Extraction:** TF-IDF Vectorizer
* **Algorithm:** Machine Learning Classifier
  (Logistic Regression / SVM / Naive Bayes)
* **Input:** User text
* **Output:** Emotion label

---

## 📸 App Features

* User-friendly Streamlit UI
* Real-time emotion prediction
* Supports multiple emotions
* Clean and lightweight ML deployment

---



## 👨‍💻 Author

**Sayan Rana**

---

⭐ If you find this project useful, consider giving it a star!
