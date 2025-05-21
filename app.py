import streamlit as st
import pickle
import sklearn

# Load your model
model = pickle.load(open('spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# UI
st.title("Spam Message Detection")
input_text = st.text_area("Enter a message to check:")

if st.button("Check"):
    if input_text.strip() == "":
        st.warning("Please enter a message.")
    else:
        vectorized = vectorizer.transform([input_text])
        prediction = model.predict(vectorized)
        label = "Spam" if prediction[0] == 1 else "Not Spam"
        st.success(f"Prediction: **{label}**")
