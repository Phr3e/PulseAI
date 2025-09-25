
---

# 📢 PulseAI – AI-Powered Audience Engagement Platform

PulseAI is a hackathon-ready project that helps **radio, print, and digital media outlets** engage their audiences in real time. It combines a **FastAPI backend** with a **Streamlit frontend**, allowing users to participate in polls, cast votes, and view live results. Future extensions will include **AI-powered summaries, recommendations, and sentiment analysis**.

---

## 🚀 Features

* 🗳️ **Interactive Polls** – Create and vote on polls.
* 📊 **Live Results** – See real-time vote counts and engagement.
* 🤖 **AI Extensions (coming soon)** – Content summarization, personalization, and sentiment analysis.
* 🖥️ **Full Stack** – FastAPI backend + Streamlit frontend.
* 🗄️ **SQLite Database** – Lightweight and easy to set up.

---

## 📂 Project Structure

```
pulseai/
│── backend/
│   ├── main.py           # FastAPI backend
│   ├── database.py       # SQLite setup
│   ├── models.py         # Pydantic models
│
│── frontend/
│   ├── app.py            # Streamlit frontend
│
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/Phr3e/PulseAI.git
cd  PulseAI
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### 1️⃣ Start Backend (FastAPI)

```bash
cd backend
uvicorn main:app --reload
```

### 2️⃣ Start Frontend (Streamlit)

Open a new terminal:

```bash
cd frontend
streamlit run app.py
```

### 3️⃣ Access the App

* Backend API → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Frontend → [http://localhost:8501](http://localhost:8501)

---

## 🛠️ Tech Stack

* **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
* **Frontend**: [Streamlit](https://streamlit.io/)
* **Database**: SQLite
* **Language**: Python 3.9+

---

## 🌍 Live Demo

🔗 \[Add your deployed demo link here]

---

## 📌 Future Improvements

* AI-powered **article summarization**.
* Personalized **content recommendations**.
* Sentiment analysis on audience feedback.
* User authentication and profiles.

---

## 👨‍💻 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---