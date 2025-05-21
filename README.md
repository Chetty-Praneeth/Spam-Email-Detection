# Spam Email Detector

A simple web app to detect whether an email (or any text message) is spam or not, built with Python and Streamlit.

---

## 🔍 Features

- **Real-time prediction**: Paste your email or message and get an instant “Spam” / “Not Spam” prediction.  
- **Pretrained model**: Uses a scikit-learn classifier (e.g. MultinomialNB) trained on labeled email data.  
- **Lightweight UI**: Powered by Streamlit for fast iteration and minimal setup.

---

## 🛠️ Tech Stack

- **Python** 3.7+  
- **Streamlit** – Front-end & hosting  
- **scikit-learn** – Model training & prediction  
- **pandas**, **NumPy** – Data manipulation  
- **joblib** – Model serialization



## Installation & Setup
## Installation & Setup

```bash
# 1. Clone the repo
git clone https://github.com/Chetty-Praneeth/Spam-Email-Detection.git
cd Spam-Email-Detection

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py




