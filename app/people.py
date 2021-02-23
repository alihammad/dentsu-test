from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@dentsu-mysql:3306/skillfinder'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=True)
    skills = db.Column(db.String, nullable=True)
    
    def __repr__(self):
        return '<People %s>' % self.firstname

class PeopleSchema(ma.Schema):
    class Meta:
        fields = ("id", "firstname", "lastname", "email", "address", "skills")
        model = People

people_schema = PeopleSchema()
peoples_schema = PeopleSchema(many=True)

class PeopleListResource(Resource):
    def get(self):
        peoples = People.query.all()
        return people_schema.dump(peoples)

api.add_resource(PeopleListResource, '/people')

if __name__ == '__main__':
    app.run(debug=True)
