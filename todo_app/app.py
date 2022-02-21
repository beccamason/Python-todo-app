from flask import Flask, render_template, request, redirect
import todo_app.data.trello_items as trello_items
from todo_app.flask_config import Config
from todo_app.ViewModel import ViewModel

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        items = trello_items.get_items()
        item_view_model = ViewModel(items)
        return render_template('index.html', view_model=item_view_model)

    @app.route('/add', methods=['POST'])
    def add():
        trello_items.add_item(request.form.get('title'), request.form.get('description'))
        return redirect('/')

    @app.route('/complete/<id>')
    def markDone(id: str):
        trello_items.complete_item(id)
        return redirect('/')

    @app.route('/progress/<id>')
    def markStarted(id: str):
        trello_items.progress_item(id)
        return redirect('/')

    @app.route('/remove/<id>')
    def removeItem(id):
        trello_items.remove_item(id)
        return redirect('/')

    if __name__ == "__main__":
        app.run(debug=True)
    
    return app