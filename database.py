from flask_sqlalchemy import SQLAlchemy
from server import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes-collections.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create table user.
class User(db.Model):  # The application context keeps track of the application-level data during a request,
    # CLI command, or other activity.
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    image = db.Column(db.LargeBinary, nullable= True)

    def __repr__(self):
        return '<User %r>' % self.username


with app.app_context():
    db.create_all()


def insert_data(table, **kwargs):
    """Function to insert data."""
    with app.app_context():
        data = table(**kwargs)  # Create a new instance of the table with the provided data
        db.session.add(data)
        db.session.commit()


def print_data(table):
    """Function to show table record."""
    with app.app_context():
        data = table.query.all()  # Retrieve all records from the User table
        for user in data:
            return user.id, user.username
