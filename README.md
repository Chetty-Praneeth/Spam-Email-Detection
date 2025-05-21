# Spam Email Detector

This project is a Spam Email Detector web app I built using Python and Streamlit. It uses a pretrained machine learning model to quickly identify whether an email or message is spam. The app provides real-time predictions with a simple and user-friendly interface.


## Features

- **Real-time prediction**: Paste your email or message and get an instant “Spam” / “Not Spam” prediction.  
- **Pretrained model**: Uses a scikit-learn classifier (e.g. MultinomialNB) trained on labeled email data.  
- **Lightweight UI**: Powered by Streamlit for fast iteration and minimal setup.

---

## Tech Stack

- **Python** 3.7 
- **Streamlit** – Front-end & hosting  
- **scikit-learn** – Model training & prediction  
- **pandas**, **NumPy** – Data manipulation  
- **joblib** – Model serialization



## Installation & Setup

1. Clone the repository

    ```bash
    git clone https://github.com/Chetty-Praneeth/Spam-Email-Detection.git
    cd Spam-Email-Detection

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the app
    ```bash
    streamlit run app.py

## You can try out the live app here:
[https://spamdetec.com](https://spamdetec.streamlit.app)


