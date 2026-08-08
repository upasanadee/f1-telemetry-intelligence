# 🏎️ F1 Telemetry Intelligence

An end-to-end Formula 1 telemetry analytics platform featuring automated OpenF1 data ingestion, AI-powered driver performance analysis, and BiLSTM-based lap time prediction.

## ✨ Features

- 📡 Automated ETL pipeline for OpenF1 telemetry
- 🗄️ PostgreSQL database for telemetry storage
- ⚡ FastAPI backend with REST APIs
- 📊 Interactive Next.js dashboard
- 🏁 AI Performance Index for driver comparison
- 🧠 BiLSTM model for lap time prediction from telemetry
- 🚀 Dynamic race and session selection
- 📈 Telemetry-driven analytics including:
  - Fastest laps
  - Top speeds
  - Track conditions
  - Race summaries
  - Driver performance rankings

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL

### Frontend
- Next.js
- React
- TypeScript
- Tailwind CSS

### Machine Learning
- PyTorch (BiLSTM)
- LightGBM
- NumPy
- Pandas

### Data Source
- OpenF1 API

## 📷 Dashboard

> Add screenshots here.

## 🚀 Getting Started

```bash
git clone https://github.com/upasanadee/f1-telemetry-intelligence.git
cd f1-telemetry-intelligence
```

### Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn api.main:app --reload
```

### Frontend

```bash
cd frontend

npm install
npm run dev
```

## 🤖 Machine Learning

### AI Performance Index

A custom telemetry-based driver ranking computed using:

- Lap pace
- Top speed
- Average speed
- Throttle usage
- Braking behaviour
- DRS utilisation

### Lap Time Prediction

A BiLSTM model predicts lap times directly from telemetry sequences consisting of:

- Elapsed time
- Speed
- RPM
- Gear
- Throttle
- Brake
- DRS

## 📄 License

MIT License