from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        if task_content:
            new_task = {
                'id': len(tasks) + 1,
                'content': task_content,
                'date_created': datetime.now()
            }
            tasks.append(new_task)
            return redirect('/')
    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    global tasks
    tasks = [task for task in tasks if task['id'] != id]
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = next((task for task in tasks if task['id'] == id), None)
    if request.method == 'POST':
        new_content = request.form['content']
        if new_content:
            task['content'] = new_content
            return redirect('/')
    return render_template('update.html', task=task)

if __name__ == "__main__":
    app.run(debug=True)
