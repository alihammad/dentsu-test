from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api, abort, reqparse
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from models import db, PeopleModel, ProjectModel

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
    def get(self):
        people = PeopleModel.query.all()
        return {'People':list(x.json() for x in people)}
 
    def post(self):
        data = request.get_json()
        new_people = PeopleModel(data["first_name"], data["last_name"], data["email"], data["address"], data["skills"])
        db.session.add(new_people)
        db.session.commit()
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

api.add_resource(PeoplesView, '/people','/peoples', 'people/','/')
api.add_resource(PeopleView,'/people/<string:first_name>', '/peoples/<string:first_name>')


############

## Projects

############


class ProjectsView(Resource):
    def get(self):
        projects = ProjectModel.query.all()
        return {'Projects':list(x.json() for x in projects)}
 
    def post(self):
        data = request.get_json()
        new_project = ProjectModel(data["project_name"],data["date_posted"],data["department"],data["description"],data["skills"])
        db.session.add(new_project)
        db.session.commit()
        return new_project.json(),201
        

class ProjectView(Resource):
    def get(self,project_name):
        project = ProjectModel.query.filter_by(project_name=project_name).first()
        if project:
            return project.json()
        return {'message':'record not found'},404
 
    def put(self,project_name):
        data = request.get_json()
        project = ProjectModel.query.filter_by(project_name=project_name).first()
 
        if project:
            project.project_name = data['project_name']
            project.date_posted = data['date_posted']
            project.department = data['department']
            project.description = data['description']
            project.skills = data['skills']            
        else:
            project = ProjectModel(project_name=project_name,**data)
 
        db.session.add(project)
        db.session.commit()
 
        return project.json()
 
    def delete(self,project_name):
        project = ProjectModel.query.filter_by(project_name=project_name).first()
        if project:
            db.session.delete(project)
            db.session.commit()
            return {'message':'Deleted'}
        else:
            return {'message': 'record not found'},404

class ProjectSkillsFinder(Resource):
    def get(self, skill):
        app.logger.info("Find skills in a project")
        projects = ProjectModel.query.filter_by(skills=skills).first(): 
        
        if projects:
            return projects.json()
        return {'message', 'Skills not found'} ,404
        
class ProjectPeopleFinder(Resource):
    def get(self,skill):
        app.logger.info("Find people with similar skills")
        # app.logger.info("Search query: {}".format(skill))

        people = PeopleModel.query.filter_by(skill=skill)
        # project = ProjectModel.query.filter_by(skills=skill).first()
        
        if people:
            return people.json()
        return {'message':'record not found'},404
 
class ProjectList(Resource):
    def get(self):
        projects = ProjectModel.query.all()
        return {'Projects':list(x.json() for x in projects)}
 
    def post(self):
        data = request.get_json()
        new_project = ProjectModel((data["project_name"],data["date_posted"],data["department"],data["description"],data["skills"]))
        db.session.add(new_project)
        db.session.commit()
        return new_project.json(),201

class Project(Resource):
    def get(self,project_name):
        project = ProjectModel.query.filter_by(project_name=project_name).first()
        if project:
            return project.json()
        return {'message':'Record not found'},404
 
    def put(self,project_name):
        data = request.get_json()
 
        project = ProjectModel.query.filter_by(project_name=project_name).first()
 
        if project:
            project.project_name = data['project_name']
            project.date_posted = data['date_posted']
            project.department = data['department']
            project.description = data['description']
            project.skills = data['skills']          
        else:
            project = ProjectModel(project_name=project_name,**data)
 
        db.session.add(project)
        db.session.commit()
 
        return project.json()
 
    def delete(self,project_name):
        project = ProjectModel.query.filter_by(project_name=project_name).first()
        if project:
            db.session.delete(project)
            db.session.commit()
            return {'message':'Deleted'}
        else:
            return {'message': 'Record not found'},404

api.add_resource(ProjectsView, '/project','/projects','/', 'project/', 'projects/')
api.add_resource(ProjectView,'/project/<string:project_name>', '/projects/<string:project_name>')
api.add_resource(ProjectResourceFinder, '/project/resourcefinder/<string:skill>')
api.add_resource(ProjectSkillsFinder, '/project/skill/<string:skill>')

app.debug = True

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)