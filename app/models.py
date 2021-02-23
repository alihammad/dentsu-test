from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()

class PeopleModel(db.Model):
    __tablename__ = 'people'
 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=True)
    skills = db.Column(db.String, nullable=True)

 
    def __init__(self, first_name, last_name, email, address, skills,):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.skills = skills

    def json(self):
        return {"first_name":self.first_name,"last_name":self.last_name,"email":self.email,"address":self.address,"skills":self.skills}


class ProjectModel(db.Model):
    __tablename__ = 'project'
    
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.String, nullable=True)
    department = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    skills = db.Column(db.String, nullable=True)
    
 
    def __init__(self, first_name, last_name, email, address, skills,):
        self.project_name = project_name
        self.date_posted = date_posted
        self.department = department
        self.description = description
        self.skills = skills

    def json(self):
        return {"project_name":self.project_name,"date_posted":self.date_posted,"department":self.department,"description":self.description,"skills":self.skills}
