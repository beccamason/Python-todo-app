from flask import Flask, render_template, request, redirect
import todo_app.data.session_items as session_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    items = session_items.get_items()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    session_items.add_item(request.form.get('title'))
    return redirect('/')

@app.route('/update/<int:id>')
def markDone(id):
    item = session_items.get_item(id)
    item['status'] = 'Done'
    session_items.save_item(item)
    return redirect('/')

@app.route('/remove/<int:id>')
def removeItem(id):
    session_items.remove_item(id)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)