from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "pros_and_cons"}
app.config["SECRET_KEY"] = "S3cr3tK3y"

db = MongoEngine(app)

import pros_and_cons.views

if __name__ == "__main__":
  app.run(debug=True)