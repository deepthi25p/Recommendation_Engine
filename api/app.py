from fastapi import FastAPI, HTTPException, Request, Header
from pydantic import BaseModel
import uuid
import time

from engine.orchestrator import RecommendationOrchestrator

app = FastAPI(
    title="Recommendation System API",
    version="1.0"
)

engine = RecommendationOrchestrator()

# ------------------------
# Metrics
# ------------------------

metrics = {
    "total_requests": 0,
    "cache_hits": 0,
    "avg_latency": 0
}

API_KEY = "secret123"


# ------------------------
# Middleware
# ------------------------

@app.middleware("http")
async def log_requests(
        request: Request,
        call_next):

    request_id = str(uuid.uuid4())

    start = time.time()

    response = await call_next(request)

    duration = time.time() - start

    metrics["total_requests"] += 1

    current_avg = metrics["avg_latency"]

    n = metrics["total_requests"]

    metrics["avg_latency"] = (
        (current_avg * (n - 1))
        + duration
    ) / n

    print(
        f"[{request_id}] "
        f"{request.method} "
        f"{request.url.path} "
        f"{duration:.4f}s"
    )

    response.headers[
        "X-Request-ID"
    ] = request_id

    return response


# ------------------------
# Authentication
# ------------------------

def verify_api_key(
        x_api_key: str = Header(None)):

    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )


# ------------------------
# Request Model
# ------------------------

class FeedbackRequest(
        BaseModel):

    user_id: int
    content_id: int
    rating: float


# ------------------------
# Health Endpoint
# ------------------------

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


# ------------------------
# Recommend Endpoint
# ------------------------

@app.get("/recommend/{user_id}")
def recommend(
        user_id: int,
        x_api_key: str = Header(None)
):

    verify_api_key(x_api_key)

    recommendations = (
        engine.get_recommendations(
            user_id
        )
    )

    if not recommendations:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "user_id": user_id,
        "recommendations":
        recommendations
    }


# ------------------------
# Feedback Endpoint
# ------------------------

@app.post("/feedback")
def feedback(
        data: FeedbackRequest,
        x_api_key: str = Header(None)
):

    verify_api_key(x_api_key)

    engine.record_feedback(
        data.user_id,
        data.content_id,
        data.rating
    )

    return {
        "message":
        "Feedback recorded"
    }


# ------------------------
# Metrics Endpoint
# ------------------------

@app.get("/metrics")
def get_metrics():

    return metrics
@app.get("/")
def home():
    return {
        "message": "Recommendation System API is running"
    }