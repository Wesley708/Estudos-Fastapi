from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

students = {
    1: {
        "name": "Wesley",
        "age": 26,
        "class": "year 12"
    }
    , 2: {
        "name": "Mariana",
        "age": 25,
        "class": "year 11"
    }
}

@app.get("/")

def index():
    return students

@app.get("/get-student/{student_id}")

def get_student(student_id: int = Path(..., description="The ID of the student you want to view", gt=0, lt=2)):
    return students[student_id]

@app.get("/get-by-name")
def get_student( test: int, name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}
