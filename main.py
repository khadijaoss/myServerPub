from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# Define a data model using Pydantic
class Item(BaseModel):
    id :int
    name: str
    age: float
#making a model in python is  a littl bit defrent
#________________________________________________
items =[
    Item( id=0, name="khadija", age=19 ,),

    Item(id=1,name="John", age=30.5),
]
# Create a simple GET endpoint
@app.get("/")
def read_root():
    return Item(age=19 ,name ='khadiaj',id=3)
# Create a POST endpoint
@app.post("/items/")
def create_item(New_Item: Item):
    items.append(New_Item)
    return {New_Item}

@app.put("/items/{item_id}")


@app.get('/para')
def calc (a:float , b:float):
    return {'result':a +b}



@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    #enumerate(items) goes through the items list 
    # and returns both the index (position) and the item  object at that position.
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    return {"error": "item not found"}


@app.delete("/students/{student_id}")
def delet_student(student_id: int, updated_student: Item):
    for index, student in enumerate(Item):
        if student.id == student_id:
            del items[index] 
            return {"msg":'deleted'}
    return {"error": "Student not found"}

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; adjust as needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)
#run it by uvicorn main:app --reload
