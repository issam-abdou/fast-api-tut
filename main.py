from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi import HTTPException

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)



 # Create Data Model "Student"
class Student(BaseModel):
     id: int
     name: str
     grade: int
     
# create students list
students = [
    Student(id=1, name="karim ali", grade=5),
    Student(id=2, name= "Abdou Aissam", grade=3)
]

# Get Students
@app.get("/students")
def read_students():
    return students

# Add new student
@app.post("/students")
def create_student(New_Student: Student):
    students.append(New_Student)
    return New_Student

# Update Student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    return {"error" : "Student not found"}

# Delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            deleted_student = students.pop(index)
            return {"message": f"Student {deleted_student.name} deleted successfully"}
    # If the loop finishes and we didn't find the ID
    raise HTTPException(status_code=404, detail="Student not found")
