# 🚀Complete Recommendation System

A production-ready recommendation system built using **Python, FastAPI, SQLite, and SQLAlchemy**. This project combines recommendation algorithms, database integration, caching, REST APIs, testing, and evaluation into a complete end-to-end system.

---

## 📌 Project Overview

This project simulates a real-world recommendation engine similar to those used by Netflix, Amazon, and YouTube.

The system:

* Stores users, content, skills, and interactions in SQLite
* Generates personalized recommendations
* Supports cold-start users
* Records user feedback
* Exposes REST APIs using FastAPI
* Provides performance metrics
* Includes testing and evaluation

---

## 🏗️ System Architecture

```text
User Request
      ↓
 FastAPI API
      ↓
Recommendation Engine
      ↓
SQLite Database
      ↓
Personalized Recommendations
```

Caching Layer:

```text
Request → Cache Check
            ↓
        Cache Hit → Return Result
            ↓
        Cache Miss
            ↓
      Generate Recommendations
```

---

## 📂 Project Structure

```text
recommendation_engine/
│
├── data/
│   ├── database.py
│   ├── models.py
│   ├── repositories.py
│   └── create_db.py
│
├── engine/
│   ├── orchestrator.py
│   ├── similarity.py
│   ├── candidate_gen.py
│   ├── scorer.py
│   └── evaluator.py
│
├── api/
│   └── app.py
│
├── scripts/
│   ├── seed_data.py
│   └── evaluate.py
│
├── tests/
│   ├── test_data.py
│   ├── test_engine.py
│   └── test_api.py
│
├── recommendation.db
├── requirements.txt
├── README.md
└── evaluation_report.md
```

---

## ✨ Features

### Recommendation Engine

* Content-based recommendations
* Popularity-based recommendations
* Cold-start handling
* Candidate generation
* Scoring and ranking
* In-memory caching

### Database Layer

* SQLite database
* SQLAlchemy ORM
* Repository pattern

### API Layer

* FastAPI REST API
* API key authentication
* Request logging
* Request tracing using UUID
* Metrics endpoint

### Testing & Evaluation

* Unit tests
* API tests
* Precision@5
* Recall@5
* NDCG@5

---

## 🛠️ Technologies Used

* Python 3.13
* FastAPI
* SQLAlchemy
* SQLite
* NumPy
* Pytest
* Uvicorn

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd day30_capstone
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🗄️ Create Database

```bash
python -m data.create_db
```

Expected output:

```text
Database created successfully!
```

---

## 🌱 Seed Sample Data

```bash
python -m scripts.seed_data
```

Expected output:

```text
Database seeded successfully!
```

Dataset contains:

* 10 Users
* 20 Content Items
* 8 Skills
* 100 Interactions

---

## ▶️ Run the API

```bash
uvicorn api.app:app --reload
```

Server runs at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 🔑 API Authentication

Use the following API key:

```text
secret123
```

Send it in headers:

```text
x-api-key: secret123
```

---

## 📡 API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
    "status": "healthy"
}
```

---

### Get Recommendations

```http
GET /recommend/{user_id}
```

Example:

```http
GET /recommend/1
```

Response:

```json
{
    "user_id": 1,
    "recommendations": [
        {
            "content_id": 12,
            "title": "Course 12",
            "score": 8.54,
            "reason": "Matches user interests"
        }
    ]
}
```

---

### Record Feedback

```http
POST /feedback
```

Request:

```json
{
    "user_id": 1,
    "content_id": 12,
    "rating": 5
}
```

Response:

```json
{
    "message": "Feedback recorded"
}
```

---

### Metrics

```http
GET /metrics
```

Response:

```json
{
    "total_requests": 10,
    "cache_hits": 3,
    "avg_latency": 0.004
}
```

---

## 🧪 Running Tests

Run all tests:

```bash
pytest -v
```

Expected result:

```text
8 passed
```

---

## 📊 Evaluation

Run evaluation script:

```bash
python -m scripts.evaluate
```

Sample output:

```text
Precision@5: 0.42
Recall@5: 0.37
NDCG@5: 0.51
```

---

## 📈 Performance Goals

* Response Time < 500 ms
* Throughput > 10 requests/sec
* Cache Enabled
* Personalized Recommendations

---

## 🔮 Future Improvements

* Redis caching
* Docker deployment
* Knowledge Graph integration
* A/B testing framework
* Real-time personalization
* Cloud deployment (Render/Heroku/AWS)

---

## 📸 Screenshots

Add screenshots here:

* API Documentation (`/docs`)
* Recommendation Response
* Metrics Endpoint
* Test Results

---

## 🎥 Demo Video

Demo Video Link:

```
https://youtu.be/aTseyextwC8
```

---

## 👨‍💻 Author

**Deepthi Pachigulla**


