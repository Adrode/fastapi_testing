from fastapi import FastAPI

app = FastAPI()

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
@app.get("/todos/filter")
def get_category(category: str):
  return [item for item in all_todos if item['category'] == category]

# path paramters
@app.get("/todos/n/{id}")
def get_todos_till_n(id: int):
  return [item for item in all_todos if item['id'] > id]

@app.get("/todos/search")
def get_search_params(text: str):
  return [item for item in all_todos if text.lower() in item['description'].lower()]

# path parameters
@app.get("/todos/{id}")
def get_todo(id: int):
  return [item for item in all_todos if item['id'] == id][0]