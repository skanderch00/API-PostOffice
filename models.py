from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Parcel(Base):
    __tablename__ = "parcels"
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, nullable=False)
    recipient_id = Column(Integer, nullable=False)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    transaction_type = Column(String, nullable=False)  # Local or International
    delivery_mode = Column(String, nullable=False)  # Standard or Express
    status = Column(String, nullable=False, default="Created")
    cost = Column(Float, nullable=False)

class TrackingLog(Base):
    __tablename__ = "tracking_logs"

    id = Column(Integer, primary_key=True, index=True)
    parcel_id = Column(Integer, ForeignKey("parcels.id"), nullable=False)
    location = Column(String, nullable=False)
    status = Column(String, nullable=False)
    timestamp = Column(String, nullable=False)

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    message = Column(String, nullable=False)
    is_read = Column(Boolean, default=False)
    created_at = Column(String, nullable=False)

class Branch(Base):
    __tablename__ = "branches"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(String, nullable=False)
    operational_hours = Column(String, nullable=False)

class Feedback_user(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)  # User who submitted the feedback
    parcel_id = Column(Integer, ForeignKey("parcels.id"), nullable=True)  # Optional parcel association
    message = Column(String, nullable=False)  # Feedback message
    created_at = Column(String, nullable=True)  # Timestamp of feedback creation