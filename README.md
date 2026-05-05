# 📘 Exam Nova – AI-Powered Exam Preparation Tutor

## 🚀 Overview

Exam Nova is a web-based AI-powered application that dynamically generates exam preparation content based on user-provided topics. It uses generative AI to create structured study materials including explanations, multiple-choice questions (MCQs), and theory-based questions in real time.

Unlike traditional platforms that rely on static content, Exam Nova provides personalized and interactive learning experiences using AI.

---

## ✨ Features

- AI-generated topic explanations (2–3 paragraphs)  
- Automatically generated MCQs with answers and explanations  
- Theory questions with detailed answers  
- Real-time content generation  
- Interactive MCQ practice (check answers instantly)  
- Reveal answers on demand  
- Responsive and modern UI  

---

## 🛠️ Tech Stack

### Frontend
- HTML  
- CSS  
- JavaScript  

### Backend
- Python  
- Flask  

### AI Integration
- Google Gemini API  

### Concepts Used
- REST API  
- JSON Parsing  
- Prompt Engineering  

---

## 🏗️ Project Structure

Exam-Nova/

├── app.py  
├── templates/  
│   └── index.html  
├── static/  
│   └── style.css  
└── README.md  

---

## ⚙️ How It Works

1. User enters a topic in the web interface  
2. Frontend sends a request to the backend (/generate)  
3. Backend creates a structured AI prompt  
4. Gemini AI generates content in JSON format  
5. Backend parses and validates the response  
6. Frontend dynamically displays explanation, MCQs, and theory questions  

---

## 🔄 Workflow

User Input → Frontend → Flask Backend → AI Model → JSON Response → UI Rendering  

---

## 🧪 Installation & Setup

### 1. Clone the Repository
git clone https://github.com/your-username/exam-nova.git  
cd exam-nova  

### 2. Install Dependencies
pip install flask google-generativeai  

### 3. Set API Key (IMPORTANT)
export GEMINI_API_KEY=your_api_key_here  

Note: Do NOT hardcode API keys in production.

---

### 4. Run the Application
python app.py  

### 5. Open in Browser
http://127.0.0.1:5000  

---

## 📸 UI Description

- Dark-themed modern interface  
- Input field for topic  
- Dynamic MCQ and theory cards  
- Interactive answer checking system  

---

## ⚠️ Limitations

- Requires internet connection  
- AI-generated content may not always be fully accurate  
- No database (no saved history)  
- No authentication system  
- Basic error handling  

---

## 🔮 Future Enhancements

- User login system  
- Difficulty level selection  
- Performance tracking and analytics  
- Database integration (MongoDB / MySQL)  
- Voice input support  
- Mobile app version  

---

## 📚 Use Cases

- Exam preparation  
- College study tool  
- Coaching institutes  
- Self-learning platform  
- AI tutoring systems  

---

## 🔐 Security Note

Do not expose API keys in your code. Always use environment variables.

---

## 📄 License

This project is for educational purposes. You are free to modify and use it.

---

## 👨‍💻 Author

Developed as an AI-based educational project demonstrating real-time content generation using generative AI.
