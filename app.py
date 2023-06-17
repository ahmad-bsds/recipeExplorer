from flask import Flask, request, send_from_directory, render_template


app = Flask(__name__, static_folder='./static')


# Home page:
@app.route('/')
def home():
    return send_from_directory('templates', 'index.html')


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
    return send_from_directory('templates', 'addRecipe.html')


@app.route('/explore', methods=['GET', 'POST'])
def explore_recipies():
    from database import User, print_data
    if request.method == 'GET':
        data = print_data(User)
        return render_template('explore.html', data=data)
    return 'Sorry!! Cant access.'


if __name__ == "__main__":
    app.run(debug=True)
