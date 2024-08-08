from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Student(BaseModel):
        id: int
        name: str
        grade: int
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    )

    

students = [
        Student(id=1, name="Ebrahim", grade=5),
        Student(id=2, name="Ali", grade=3)
]
@app.get("/students/")
def read_students():
    return students

@app.post("/students/")
def create_student(New_Student:Student):
    students.append(New_Student)
    return New_Student

@app.put("/students/{student_id}")
def update_student(student_id:int, update_student: Student):
    for index,student in enumerate(students):
         if student.id==student_id:
              student[index]=updated_student
              return updated_Student
    return {"error":"Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    for index,student in enumerate(students):
         if student.id==student_id:
              del students[index]
              return {"message":"Student deleted"}
    return {"error":"Student not found"}