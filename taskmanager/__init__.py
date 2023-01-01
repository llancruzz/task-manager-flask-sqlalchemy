import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa No Quality Assurance


# ^ Imports the hidden environment variables from our 'env' package
# As we aren't pushing the env.py file to GitHub it won't be visible
# once we have deployed to Heroku & will throw an error.
# So we will only import 'env' if the OS can find an existing file path
# for the env.py file itself.


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri


# ^ if development == True it will use the local db
# if false it will use the db on heroku
# if the heroku db has postgres:// it will update it with the correct value


db = SQLAlchemy(app)

from taskmanager import routes  # noqa No Quality Assurance
