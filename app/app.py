from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api, abort, reqparse
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@dentsu-mysql:3306/skillfinder'
db = SQLAlchemy(app)
api = Api(app)
######



######
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=True)
    skills = db.Column(db.String, nullable=True)

    def serialize(self):
        return {
            'firstname': self.first_name,
            'lastname': self.last_name,
            'email': self.email,
            'address': self.address,
            'skills': self.skills
        }

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('firstname', type=float, required=True, help="firstname is required parameter!")
parser.add_argument('lastname', type=float, required=True, help="lastname is required parameter!")
parser.add_argument('email', type=float, required=True, help="email is required parameter!")
parser.add_argument('address', type=float, required=True, help="address is optional!")
parser.add_argument('skills', type=float, required=True, help="skills is optional!")


class PeopleList(Resource):
    def get(self):
        print("GET called")
        # people = db.session.query(People.query.all())
        people = People.query.all()
        return [People.serialize(person) for person in people]

    def post(self):
        #print("POST called with first name: {}".format(args['firstname']))
        args = parser.parse_args()
        people = People(firstname=args['firstname'],lastname=args['lastname'],email=args['email'],address=args['address'],skills=args['skills'])
        db.session.add(people)
        db.session.commit()
        return People.serialize(people), 201


class PeopleRecord(Resource):
    def get(self, record_id):
        print("GET called")
        return People.serialize(
            People.query.filter_by(id=record_id)
                .first_or_404(description='Record with id={} is not available'.format(record_id)))
    
    def delete(self, record_id):
        print("DELETE called")
        record = People.query.filter_by(id=record_id)\
            .first_or_404(description='Record with id={} is not available'.format(record_id))
        db.session.delete(record)
        db.session.commit()
        return '', 204

    def put(self, record_id):
        args = parser.parse_args()
        record = People.query.filter_by(id=record_id)\
            .first_or_404(description='Record with id={} is not available'.format(record_id))
        
        record.first_name = args["first_name"]
        record.last_name = args["last_name"]
        record.email = args["email"]
        record.address = args["address"]
        record.skills = args["skills"]

        db.session.commit()
        return People.serialize(record), 201

#########
#########

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.String, nullable=True)
    department = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    skills = db.Column(db.String, nullable=True)

    def serialize(self):
        return {
            'project_name': self.project_name,
            'date_posted': self.date_posted,
            'department': self.department,
            'description': self.description,
            'skills': self.skills
        }

class ProjectList(Resource):
    def get(self):
        proejcts = Project.query.all()
        return [Project.serialize(project) for project in proejcts]

    def post(self):
        args = parser.parse_args()
        project = Project(id=args['id'], project_name=args['project_name'], date_posted=args['date_posted'], department=args['department'], description=args['description'], skills=args['skills'])
        db.session.add(project)
        db.session.commit()
        return Project.serialize(project), 201


class ProjectRecord(Resource):
    def get(self, record_id):
        return Project.serialize(
            Project.query.filter_by(id=record_id)
                .first_or_404(description='Record with id={} is not available'.format(record_id)))
    
    def delete(self, record_id):
        record = Project.query.filter_by(id=record_id)\
            .first_or_404(description='Record with id={} is not available'.format(record_id))
        db.session.delete(record)
        db.session.commit()
        return '', 204

    def put(self, record_id):
        args = parser.parse_args()
        record = Project.query.filter_by(id=record_id)\
            .first_or_404(description='Record with id={} is not available'.format(record_id))

        record.project_name = args["project_name"]
        record.date_posted = args["date_posted"]
        record.department = args["department"]
        record.description = args["description"]
        record.skills = args["skills"]

        db.session.commit()
        return Project.serialize(record), 201

api.add_resource(PeopleList, '/peoplelist','/')
api.add_resource(PeopleRecord, '/people/<record_id>')

api.add_resource(ProjectList, '/projectlist','/')
api.add_resource(ProjectRecord, '/project/<record_id>')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
