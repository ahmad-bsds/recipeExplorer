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
    from database import User, insert_data, print_data
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username_']
        # image = request.form['image']
        insert_data(User, name=name, username=username)
        data = print_data(User)
        return f'{data}'
    return render_template('addRecipe.html')


if __name__ == "__main__":
    app.run(debug=True)
