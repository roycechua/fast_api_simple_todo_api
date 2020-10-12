# Fast-api Simple Todo API Sample

This simple Fast-api app sample demonstrates the use of Fast-api for a simple CRUD app endpoints using (GET, POST, PUT, DELETE).

# Dependencies

Run ```pip install -r requirements.txt``` to install the dependencies.

# How to run the program

Run the command ```uvicorn main:todo_app_api --reload```. Reload enables instant reload / debug mode when changes are made to the app.

**Note**: No Database as of now was added so once the server shuts down or restarts, all todos added will be lost. 

You can add a database (a simple one SQLite for starters) which is available on Fast-API documentation: 
https://fastapi.tiangolo.com/tutorial/sql-databases/#interact-with-the-database-directly

# Endpoints

You can test these out using Postman(https://www.postman.com/) which is free.

- GET localhost:8000/todos - returns all the todos in the todos_list.
- GET localhost:8000/todo/{id} - returns the specific todo object
- POST localhost:8000/todo/add - adds a todo object from your request body.
- DELETE localhost:8000/todo/{id} - deletes a todo with the id given in the parameter.
- PUT localhost:8000/todo/{id} - Updates an existing todo if there is any.
- PUT localhost:8000/todo/toggle/{id} - toggles the isDone boolean value (done or not done).

# License 
MIT