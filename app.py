import streamlit as st
import pickle

# Page config (must be first Streamlit command)
st.set_page_config(page_title="Emotion Detection", page_icon="😊")

# Load Model & Vectorizer
with open("emotion_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf_vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)

# Correct label mapping (based on your dataset)
label_map = {
    0: "Sadness 😢",
    1: "Anger 😡",
    2: "Love ❤️",
    3: "Surprise 😲",
    4: "Fear 😨",
    5: "Joy 😊"
}

# UI
st.title("Emotion Detection using NLP")
st.write("Detect emotions from text using a trained ML model")

user_text = st.text_area("Enter your text here:")

if st.button("Predict Emotion"):
    if user_text.strip() == "":
        st.warning("Please enter some text")
    else:
        text_vector = tfidf.transform([user_text])
        prediction_num = model.predict(text_vector)[0]
        emotion = label_map[prediction_num]
        st.success(f"Predicted Emotion: {emotion}")
