from flask_frozen import Freezer
from flask import Flask
from website import app

freezer = Freezer(app)
app.config.from_pyfile('settings.py')

if __name__ == '__main__':
    freezer.run(debug=True)
    # app.run(debug=True)
