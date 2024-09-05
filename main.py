from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# Define a data model using Pydantic
class Item(BaseModel):
    message: str = None
    name: str
    age: float
#making a model in python is  a littl bit defrent
#________________________________________________

# Create a simple GET endpoint
@app.get("/")
def read_root():
    return Item(age=19 ,name ='khadiaj',message="ok")
# Create a POST endpoint
@app.post("/items/")
def create_item(item: Item):
    return {"item": item}

@app.get('/para')
def calc (a:float , b:float):
    return {'result':a +b}
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; adjust as needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)
#run it by uvicorn main:app --reload