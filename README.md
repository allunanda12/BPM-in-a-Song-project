# 🎵 BPM in a Song Project

A full-stack AI-powered music analysis application that extracts audio features from uploaded songs and visualizes them through a React web application and a Power BI dashboard.

---

## 🚀 Features

- Upload MP3/WAV audio files
- Automatic audio feature extraction
- BPM (Tempo) Detection
- Duration Analysis
- RMS Energy Calculation
- Zero Crossing Rate (ZCR)
- Spectral Centroid Analysis
- MFCC Feature Extraction
- Chroma Feature Extraction
- Waveform Generation
- Spectrogram Generation
- Interactive React Frontend
- FastAPI Backend
- Power BI Dashboard

---

## 🛠️ Tech Stack

### Frontend
- React.js
- Vite
- Axios

### Backend
- FastAPI
- Python
- Uvicorn

### Audio Processing
- Librosa
- NumPy
- Matplotlib

### Data Visualization
- Power BI

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```
BPM-in-a-Song-project
│
├── backend
│   ├── ml
│   ├── routes
│   ├── services
│   ├── static
│   ├── uploads
│   ├── app.py
│   └── requirements.txt
│
├── frontend
│   ├── src
│   ├── public
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/allunanda12/BPM-in-a-Song-project.git
```

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```
http://localhost:5173
```

---

## 📊 Extracted Audio Features

- Duration
- Tempo (BPM)
- Sample Rate
- RMS Energy
- Zero Crossing Rate (ZCR)
- Spectral Centroid
- MFCC Mean
- Chroma Mean

---

## 📈 Power BI Dashboard

The dashboard includes:

- Average BPM
- Average Duration
- Average RMS
- Average ZCR
- BPM by Song
- Duration by Song
- RMS Analysis
- Audio Feature Comparison

---

## 📸 Screenshots

### Upload Page

(Add screenshot)

### Analysis Dashboard

(Add screenshot)

### Power BI Dashboard

(Add screenshot)

---

## 🔮 Future Enhancements

- Mood Detection
- Genre Classification
- Music Recommendation
- Playlist Analysis
- Cloud Deployment
- User Authentication

---

## 👨‍💻 Author

**Nanda Allu**

GitHub: https://github.com/allunanda12

---

## 📜 License

This project is developed for educational and portfolio purposes.