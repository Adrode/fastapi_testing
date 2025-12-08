from fastapi import FastAPI

app = FastAPI()

all_todos = [
  {'id': 1, 'category': 'sports', 'description': 'Go to the gym'},
  {'id': 2, 'category': 'programming', 'description': 'Learn for 2h'},
  {'id': 3, 'category': 'reading', 'description': 'Read a book for 15 minutes'},
  {'id': 4, 'category': 'meditating', 'description': 'Meditate for 10 minutes'},
  {'id': 5, 'category': 'food', 'description': 'Eat 2700 kcal'},
]

@app.get("/todos/{id}")
def get_todo(id: int):
  for item in all_todos:
    if item['id'] == id:
      return {'result': item}