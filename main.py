from fastapi import FastAPI
from database import db

app = FastAPI()

@app.get("/")
def getRoutes():
    return ['/notes', '/notes/<pk>']

@app.get("/notes")
def getRoutes():
    notes = db.search_by_value('notesapp', 'notes', 'id', '*', get_attributes=['*'])
    return notes