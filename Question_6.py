from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

# Create a Flask application instance
app = Flask(__name__)

# In-memory storage for tasks
tasks = []

# Swagger UI setup
SWAGGER_URL = '/swagger'  # URL for accessing Swagger UI
API_URL = '/static/swagger.json'  # URL for the Swagger JSON file
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # URL endpoint for Swagger UI
    API_URL,  # URL for the Swagger JSON file
    config={'app_name': "To-Do API"}  # Configuration for Swagger UI
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)  # Register Swagger UI blueprint

# Route to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    print(f"Returning tasks: {tasks}")  # Debug: print tasks to console
    return jsonify({'tasks': tasks})  # Return the list of tasks as JSON


# Route to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()  # Parse JSON data from the request
    new_task = {  # Create a new task dictionary
        'id': len(tasks) + 1,  # Assign a unique ID to the new task
        'title': data.get('title'),  # Get the title from the request data
        'done': False  # Initialize 'done' status as False
    }
    tasks.append(new_task)  # Add the new task to the tasks list
    print(f"Created task: {new_task}")  # Debug: print new task to console
    return jsonify(new_task), 201  # Return the new task as JSON with a 201 status code


# Route to update an existing task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)  # Find the task by ID
    if task is None:  # If task is not found
        return jsonify({'message': 'Task not found'}), 404  # Return an error message with a 404 status code

    data = request.get_json()  # Parse JSON data from the request
    task['title'] = data.get('title', task['title'])  # Update the title if provided
    task['done'] = data.get('done', task['done'])  # Update the 'done' status if provided
    print(f"Updated task: {task}")  # Debug: print updated task to console
    return jsonify(task)  # Return the updated task as JSON


# Route to delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks  # Use the global tasks list
    tasks = [t for t in tasks if t['id'] != task_id]  # Remove the task with the specified ID
    print(f"Deleted task ID: {task_id}")  # Debug: print deleted task ID to console
    return jsonify({'message': 'Task deleted'}), 200  # Return a success message with a 200 status code
    

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask application with debugging enabled
