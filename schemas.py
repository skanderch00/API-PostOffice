from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    role: str  # admin, staff, or customer

class UserResponse(BaseModel):
    id: int
    username: str
    role: str
    created_at: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class ParcelCreate(BaseModel):
    sender_id: int
    recipient_id: int
    origin: str
    origin_country: str
    destination: str
    destination_country: str
    weight: float
    delivery_mode: str

class ParcelResponse(ParcelCreate):
    id: int
    transaction_type: str
    cost: float
    status: str

    class Config:
        orm_mode = True

class FeedbackCreate(BaseModel):
    user_id: int
    parcel_id: int
    message: str

class FeedbackResponse(FeedbackCreate):
    id: int
    created_at: str

    class Config:
        orm_mode = True

class TrackingLogCreate(BaseModel):
    location: str
    status: str

class TrackingLogResponse(TrackingLogCreate):
    parcel_id: int
    timestamp: str

    class Config:
        orm_mode = True

class NotificationCreate(BaseModel):
    user_id: int
    message: str

class NotificationResponse(NotificationCreate):
    id: int
    is_read: bool
    created_at: str

    class Config:
        orm_mode = True
