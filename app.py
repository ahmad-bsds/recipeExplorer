from flask import Flask, request
from flask import render_template
app = Flask(__name__)


# Home page:
@app.route('/')
def home():
    return render_template('index.html')


# Add Recipe page
@app.route('/addRecipe', methods=['GET', 'POST'])
def add_recipe():
    from database import User, insert_data
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username_']
        recipe = request.form['editordata']
        insert_data(User, name=name, username=username, recipe=recipe)
        return f'Action completed!'
    return render_template('addRecipe.html')


@app.route('/explore', methods=['GET', 'POST'])
def explore_recipies():
    from database import User, print_data
    if request.method == 'GET':
        data = print_data(User)
        return render_template('explore.html', data=data)
    return 'Sorry!! Cant access.'


if __name__ == "__main__":
    from gunicorn.app.wsgiapp import run
    run()

