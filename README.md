# 🔐 Quishing Detector — QR Code Phishing Detection System

A security-focused web application that analyzes URLs extracted from QR codes and helps identify potentially malicious or phishing websites.

## 📌 Overview

QR codes are increasingly used for payments, authentication, websites, and information sharing. Attackers can abuse them to redirect users to malicious websites, a technique commonly known as **quishing (QR-code phishing)**.

This project was built to provide an additional security layer between scanning a QR code and visiting the URL.

The system:

1. Accepts a QR-code image from the user.
2. Decodes the QR code.
3. Extracts the URL.
4. Analyzes security-related characteristics of the URL.
5. Applies detection logic / machine-learning analysis.
6. Returns a security assessment to the user.

## 🚀 Features

- QR-code image scanning
- QR data and URL extraction
- URL security feature extraction
- Rule-based security analysis
- Machine-learning-based URL classification
- FastAPI backend
- Web-based frontend
- Suspicious URL detection
- Clear detection results for the user

## 🏗️ System Architecture

```text
User
  │
  ▼
Frontend Dashboard
  │
  │ Upload QR Image
  ▼
FastAPI Backend
  │
  ▼
OpenCV + pyzbar
  │
  │ Extract URL
  ▼
URL Feature Extraction
  │
  ├───────────────┐
  ▼               ▼
Security Rules   ML Model
  │               │
  └───────┬───────┘
          ▼
   Risk Assessment
          │
          ▼
      Result
```

## 🛠️ Technology Stack

### Backend
- Python
- FastAPI
- Uvicorn

### QR Processing
- OpenCV
- pyzbar

### Machine Learning
- Scikit-learn
- Joblib

### Networking
- Requests

### Frontend
- HTML
- CSS
- JavaScript

## 📂 Project Structure

```text
quishing-detector/
│
├── backend/
│   ├── main.py
│   ├── qr_engine.py
│   ├── feature_extractor.py
│   ├── r1.txt
│   └── requirements.txt
│
├── frontend/
│   └── index.html
│
├── .gitignore
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/sahilsaraf2004/quishing-detector.git
```

Move into the project directory:

```bash
cd quishing-detector
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r backend/requirements.txt
```

## ▶️ Running the Application

Start the FastAPI backend:

```bash
uvicorn backend.main:app --reload
```

The backend will normally be available at:

```text
http://127.0.0.1:8000
```

Open the frontend according to the project's configured frontend setup.

## 🔍 How It Works

### 1. QR Image Input

The user selects or uploads an image containing a QR code.

### 2. QR Decoding

OpenCV and pyzbar process the image and extract the information encoded in the QR code.

### 3. URL Extraction

If the QR code contains a URL, the system extracts it for further analysis.

### 4. Feature Extraction

Security-related characteristics of the URL are analyzed using URL parsing and feature extraction techniques.

### 5. Detection

The extracted information is evaluated using security rules and the machine-learning detection pipeline.

### 6. Result

The application presents the security assessment to the user.

## 🎯 Motivation

The project was independently developed to explore how software engineering, cybersecurity, QR-code processing, and machine learning can be combined to address a practical security problem.

## 🔮 Future Improvements

- Real-time QR-code scanning using a camera
- Larger and more diverse phishing datasets
- Improved model evaluation
- Explainable detection results
- Threat-intelligence API integration
- Browser extension integration
- Deployment as a cloud-based service

## ⚠️ Disclaimer

This project is intended for educational and research purposes. Detection results should not be considered a guaranteed determination of whether a website is safe or malicious.

## 👨‍💻 Author

**Sahil Saraf**

B.Tech Information Technology  
GitHub: `@sahilsaraf`