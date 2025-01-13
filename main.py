from fastapi import FastAPI
from app.database import Base, engine
from app.routers import parcels, tracking, notifications, users, feedback_user
import logging

# Initialize the FastAPI app
app = FastAPI(
    title="Postal Service Management API",
    description="A RESTful API for managing postal services including parcels, tracking, notifications, and user authentication.",
    version="1.0.0"
)

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ensure all models are created in the database
Base.metadata.create_all(bind=engine)
logger.info("Database tables created successfully.")

# Include routers
app.include_router(users.router, prefix="/users", tags=["User Management"])
app.include_router(parcels.router, prefix="/parcels", tags=["Parcel Management"])
app.include_router(tracking.router, prefix="/tracking", tags=["Real-Time Tracking"])
app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])
app.include_router(feedback_user.router, prefix="/feedback", tags=["Feedback"])

# Root endpoint
@app.get("/")
def read_root():
    logger.info("Root endpoint accessed.")
    return {"message": "Welcome to the Postal Service Management API!"}