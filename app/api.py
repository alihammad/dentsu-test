from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api, abort, reqparse
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from models import db, PeopleModel

app = Flask(__name__)
 
api = Api(app) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@dentsu-mysql:3306/skillfinder'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db.init_app(app)
# db = SQLAlchemy(app)

@app.before_first_request
def create_table():
    db.create_all()

class PeoplesView(Resource):
    def create_session(config):
        engine = create_engine(config['SQLALCHEMY_DATABASE_URI'])
        Session = sessionmaker(bind=engine)
        session = Session()
        session._model_changes = {}
        return session 
        
    def get(self):
        people = PeopleModel.query.all()
        return {'People':list(x.json() for x in people)}
 
    def post(self):
        sess = create_session(app.config)
        data = request.get_json()
        new_people = PeopleModel(data["first_name"], data["last_name"], data["email"], data["address"], data["skills"])
        # db.seesion.add(new_people)
        # db.session.commit()
        sess.add(new_people)
        sess.commit()
        return new_people.json(),201
        

class PeopleView(Resource):
    def get(self,first_name):
        people = PeopleModel.query.filter_by(first_name=first_name).first()
        if people:
            return people.json()
        return {'message':'record not found'},404
 
    def put(self,first_name):
        data = request.get_json()
        people = PeopleModel.query.filter_by(first_name=first_name).first()
 
        if people:
            people.first_name = data['first_name']
            people.last_name = data['last_name']
            people.email = data['email']
            people.address = data['address']
            people.skills = data['skills']            
        else:
            people = PeopleModel(first_name=first_name,**data)
 
        db.session.add(people)
        db.session.commit()
 
        return people.json()
 
    def delete(self,first_name):
        people = PeopleModel.query.filter_by(first_name=first_name).first()
        if people:
            db.session.delete(people)
            db.session.commit()
            return {'message':'Deleted'}
        else:
            return {'message': 'record not found'},404

class PeopleList(Resource):
    def get(self):
        people = PeopleModel.query.all()
        return {'People':list(x.json() for x in people)}
 
    def post(self):
        data = request.get_json()
        new_people = PeopleModel(data['first_name'],data['last_name'],data['email'],data['address'],data['skills'])
        db.session.add(new_people)
        db.session.commit()
        return new_people.json(),201

class People(Resource):
    def get(self,first_name):
        people = PeopleModel.query.filter_by(first_name=first_name).first()
        if people:
            return people.json()
        return {'message':'Record not found'},404
 
    def put(self,first_name):
        data = request.get_json()
 
        people = PeopleModel.query.filter_by(first_name=first_name).first()
 
        if people:
            people.first_name = data["first_name"]
            people.last_name = data["last_name"]
            people.email = data["email"]
            people.address = data["address"]
            people.skills = data["skills"]
        else:
            people = PeopleModel(first_name=first_name,**data)
 
        db.session.add(people)
        db.session.commit()
 
        return people.json()
 
    def delete(self,first_name):
        people = PeopleModel.query.filter_by(first_name=first_name).first()
        if people:
            db.session.delete(people)
            db.session.commit()
            return {'message':'Deleted'}
        else:
            return {'message': 'Record not found'},404

api.add_resource(PeoplesView, '/people','/peoples','/')
api.add_resource(PeopleView,'/people/<string:first_name>', '/peoples/<string:first_name>')

app.debug = True

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)