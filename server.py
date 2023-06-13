from flask import Flask
from flask import render_template


app = Flask(__name__)


# Home page:
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/data')
def data():
    from database import User, print_data
    users = print_data(User)  # Retrieve all User records
    return render_template('temp.html', users=users)


if __name__ == "__main__":
    app.run(debug=True)
