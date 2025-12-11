from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class CategoryEnum(str, Enum):
  sports = "sports"
  programming = "programming"
  reading = "reading"
  meditating = "meditating"
  food = "food"

all_todos = [
  {'id': 1, 'category': 'sports', 'description': 'Go to the gym'},
  {'id': 2, 'category': 'programming', 'description': 'Learn for 2h'},
  {'id': 3, 'category': 'reading', 'description': 'Read a book for 15 minutes'},
  {'id': 4, 'category': 'meditating', 'description': 'Meditate for 10 minutes'},
  {'id': 5, 'category': 'food', 'description': 'Eat 2700 kcal'},
  {'id': 6, 'category': 'sports', 'description': 'Run for 30 minutes'},
  {'id': 7, 'category': 'food', 'description': 'Prepare recipes'},
  {'id': 8, 'category': 'programming', 'description': 'Prepare a project'},
]

# GET

@app.get("/todos/sorted")
def get_sorted_todos(order: str):
  if order == 'asc':
    return sorted(all_todos, key = lambda x: x['id'])
  elif order == 'desc':
    return sorted(all_todos, key = lambda x: x['id'], reverse=True)

# 2 query parameters
@app.get("/todos/paginate")
def get_paginated_todos(skip: int, limit: int):
  return all_todos[skip:skip+limit]

@app.get("/todos/range/{start_id}")
def get_range_todos(start_id: int, end_id: int):
  return [item for item in all_todos if start_id <= item['id'] <= end_id]

@app.get("/todos/all")
def get_all_todos():
  return all_todos

# query parameters
@app.get("/todos/by-category/{category}")
def get_category(category: CategoryEnum):
  return [item for item in all_todos if item['category'] == category.value]

# path paramters
@app.get("/todos/n/{id}")
def get_todos_till_n(id: int):
  return all_todos[:id]

@app.get("/todos/search")
def get_search_params(text: str):
  return [item for item in all_todos if text.lower() in item['description'].lower()]

# path parameters
@app.get("/todos/{id}")
def get_todo(id: int):
  return [item for item in all_todos if item['id'] == id][0]

# POST

@app.post("/todos/new_todo")
def post_new_todo(todo: dict):
  new_todo_id = max(item['id'] for item in all_todos) + 1
  
  new_todo = {
    'id': new_todo_id,
    'category': todo['category'],
    'description': todo['description']
  }

  all_todos.append(new_todo)
  return new_todo