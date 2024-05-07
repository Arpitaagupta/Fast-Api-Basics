from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()  #just like creating instance of FastAPI object

#What is endpoint?
# End point is one end of communication. Some end points may get a particular information or a particualr data store

#for this particular url, end point is delete-user
#localhost/delete-user
#amazon.com/create-user
#path --> normal url

#Common end points-> GET, POST, PUT, DELETE
#GET -> Get an information or return an information
#POST -> Create something new  like craeting new onject in database
#PUT -> Updating data that exists in particular database
#DELETE -> Delete something

students = {
    1 : {
        "name": "arpita",
        "age": "20",
        "class" : "btech year 3"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str
    
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[str] = None
    year: Optional[str] = None
    
    
@app.get("/") #to return something
def index():
    return{"name" : "First Data"}
#fastapi uses json data

#Path
@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    # int = Path(None, description="The ID of the student you want to view.", gt=0, lt=3)
    return students[student_id]

#gt, lt, ge, le <50 and 1>=

# In path parameter we need to add whatever the parameter wants to collect in the URL,
#but in query we don't need to do that

#Path & Query Together
@app.get("/get-by-name/{/student_id}")
def get_student(*,student_id: int, name : Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data" : "Not found"}

#Request Body and Post Methods
#Request body is like the data pass when you want to create a new object or new data.

@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students:
        return {"Error" : "Student exists"}
    #user with same id cannot be created twice
    students[student_id] = student
    return students[student_id]



#Put & Delete Methods

#Put Method is used to update something that already exists
@app.put("/update-student/{student_id}")
def update_student(student_id : int, student :  UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    if student.name != None:
        students[student_id].name = student.name
    
    if student.age != None:
        students[student_id].age = student.age
    
    if student.year != None:
        students[student_id].year = student.year    
        
    return students[student_id]

#Delete Method is used for deleting object from database
@app.delete("/delete/student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    del students[student_id]
    return {"Message": "Student deleted successfully"}
