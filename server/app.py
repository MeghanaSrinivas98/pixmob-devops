from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from sqlalchemy import exc
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)
bcrypt = Bcrypt()

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(300), unique=True, nullable=False)

  def __init__(self, email, password):
    self.email = email
    self.password = password

db.create_all()

@app.route('/user', methods=['POST'])
def create_user():
  body = request.get_json()
  try:
      pw_hash = bcrypt.generate_password_hash(body['password']).decode('utf-8')
      db.session.add(User(body['email'], pw_hash))
      db.session.commit()
      return "user created"
  except exc.IntegrityError:
      return "user exists"
