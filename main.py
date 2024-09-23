import uuid
from fastapi import FastAPI  , Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from typing import List, Annotated, Optional
import models
from uuid import UUID, uuid4


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

#BaseModels
class EventBase(BaseModel):
    title: str
    description: str
    description : str
    date : str
    location :str
    category :str
    media  : str

class UserBase(BaseModel):
    user_id : Optional[UUID] = str(uuid4()) # type: ignore
    name: str
    email: str
    telephone: Optional[str] 

 
    
#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#validation

db_dependency = Annotated[Session, Depends(get_db)]

# Sample data creation
def create_sample_data(db: Session):
    sample_events = [
        {
            "title": "VU Open Day",
            "description": "Explore Victoria University Kampala and its programs",
            "date": "2023-08-15",
            "location": "Victoria University Kampala Campus",
            "category": "Education",
            "media": "https://vu.ac.ug/open-day-2023.jpg"
        },
        {
            "title": "Hybase System Launch",
            "description": "Introducing the new Hybase system at Victoria University",
            "date": "2023-09-01",
            "location": "VU Main Auditorium",
            "category": "Technology",
            "media": "https://vu.ac.ug/hybase-launch.png"
        },
        {
            "title": "Original Hybrids Showcase",
            "description": "Presenting innovative hybrid solutions developed at VU",
            "date": "2023-09-15",
            "location": "VU Innovation Lab",
            "category": "Technology",
            "media": "https://vu.ac.ug/hybrid-showcase.jpg"
        },
        {
            "title": "VU Career Fair",
            "description": "Connect with potential employers and explore career opportunities",
            "date": "2023-10-05",
            "location": "Victoria University Sports Complex",
            "category": "Career",
            "media": "https://vu.ac.ug/career-fair-2023.jpg"
        },
        {
            "title": "Hybase Workshop",
            "description": "Learn how to utilize the Hybase system for academic research",
            "date": "2023-10-20",
            "location": "VU Computer Lab",
            "category": "Education",
            "media": "https://vu.ac.ug/hybase-workshop.png"
        },
        {
            "title": "VU Cultural Day",
            "description": "Celebrate diversity at Victoria University Kampala",
            "date": "2023-11-10",
            "location": "VU Quadrangle",
            "category": "Culture",
            "media": "https://vu.ac.ug/cultural-day-2023.jpg"
        },
        {
            "title": "Hybrid Learning Seminar",
            "description": "Exploring the benefits of hybrid learning models at VU",
            "date": "2023-11-25",
            "location": "VU Conference Center",
            "category": "Education",
            "media": "https://vu.ac.ug/hybrid-learning-seminar.jpg"
        },
        {
            "title": "VU Hackathon",
            "description": "24-hour coding challenge for VU students",
            "date": "2023-12-08",
            "location": "VU Tech Hub",
            "category": "Technology",
            "media": "https://vu.ac.ug/hackathon-2023.png"
        },
        {
            "title": "End of Year Gala",
            "description": "Celebrating achievements and innovations at Victoria University",
            "date": "2023-12-15",
            "location": "VU Grand Hall",
            "category": "Celebration",
            "media": "https://vu.ac.ug/gala-2023.jpg"
        },
        {
            "title": "Hybase and Hybrid Systems Expo",
            "description": "Showcasing the latest developments in Hybase and hybrid technologies at VU",
            "date": "2024-01-20",
            "location": "VU Exhibition Center",
            "category": "Technology",
            "media": "https://vu.ac.ug/hybase-hybrid-expo.png"
        }
    ]

    for event_data in sample_events:
        db_event = models.Event(**event_data)
        db.add(db_event)
    
    db.commit()

# Call this function to populate the database with sample data
@app.on_event("startup")
async def startup_event():
    db = SessionLocal()
    create_sample_data(db)
    db.close()


@app.post('/api/event/', status_code= status.HTTP_201_CREATED)
def post_event(event:EventBase, db:db_dependency):
    db_event = models.Event(
        title= event.title,
        description = event.description,
        date = event.date,
        location = event.location,
        category = event.category,
        media = event.media
    )
    db_events = models.Event(**event.model_dump())
    db.add(db_event)
    db.commit()
    return db.query(models.Event).all()

# Get route for all posts
@app.get('/api/post/', status_code=status.HTTP_200_OK)
async def all_posts(db: db_dependency):
    return db.query(models.Event).all()

# Get route for specifc post
@app.get('/api/post/{post_id}', status_code=status.HTTP_200_OK)
def get_post(post_id: int, db: db_dependency):
    db_post = db.query(models.Event).filter(models.Event.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not Available")
    return db_post

# updating the existing post 
@app.put('/api/post/{post_id}', status_code=status.HTTP_200_OK)
async def update_post(post_id:int, db: db_dependency, event: EventBase):
    db_post = db.query(models.Event).filter(models.Event.id == post_id).first()
    
    # Check if the post exists
    if db_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not Available")

    # # Update the post data
    # Update the post data
    upd_post = db_post
    upd_post.title = event.title
    upd_post.description = event.description
    upd_post.date = event.date
    upd_post.location = event.location
    upd_post.category = event.category
    upd_post.media = event.media

    # Commit the changes
    db.commit()
    return {'Message': 'Values Updated Successfully'}

#delete route for a specific post
@app.delete('/api/post/{post_id}', status_code=status.HTTP_202_ACCEPTED)
async def delete_post(post_id:int, db: db_dependency):
    return {'message': 'Post Deleted'}


####################### User HTTP METHODS #####################

@app.post('/api/users/', status_code = status.HTTP_201_CREATED)
async def post_user(user:UserBase, db:db_dependency):
    db_user = models.User(
        name = user.name,
        email = user.email,
        telephone = user.telephone,
    )
    db_users = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()

    # Sample data for users
def create_sample_data(db: Session):
    sample_users = [
        UserBase(name="Albert Altech", email="albert@example.com", telephone="1234567890"),
        UserBase(name="Benjamin Mubagi", email="benjamin@example.com", telephone="2345678901"),
        UserBase(name="Marvin Masaba", email="marvin@example.com", telephone="3456789012"),
        UserBase(name="Odongo Emmanuel", email="odongo@example.com", telephone="4567890123"),
        UserBase(name="Jewel Jeols Mulungi", email="jewel@example.com", telephone="5678901234"),
        UserBase(name="Emma Kenzi", email="emma@example.com", telephone="6789012345"),
        UserBase(name="Vincent Onzima", email="vincent@example.com", telephone="7890123456"),
        UserBase(name="Dave Aserne", email="dave@example.com", telephone="8901234567")
    ]

    # Add sample users to the database
    for sample_user in sample_users:
        db_user = models.User(**sample_user.model_dump())
        db.add(db_user)
    db.commit()

    return {"message": "Sample users added successfully"}


# Get Route for all users in the database
@app.get('/api/users/', status_code = status.HTTP_200_OK)
async def all_users(db: db_dependency):
    return db.query(models.User).all()

# Getting a specfic user by Id
@app.get('/api/users/{user_id}', status_code = status.HTTP_200_OK)
async def get_user(user_id: int, db: db_dependency):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    return db_user

# Updating a specfic User by id its not working
@app.put('/api/users/{user_id}', status_code = status.HTTP_202_ACCEPTED)
async def update_user(user_id: int, db: db_dependency, user:UserBase):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User Quered None')
    # upd_user =
    return {'message': 'User Updated'}

# Deleting a specfic user by id it not working 
@app.delete('/api/users/{user_id}', status_code = status.HTTP_202_ACCEPTED)
async def del_user(user_id: int ,db: db_dependency):
    return {'message': 'User Deleted'}