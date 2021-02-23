# Dentsu Data Engineering Challenge


## Background information

You have been provided two files:
- People
- Projects

The `people.json` file contains a list of generated persons, their details and skills.

The `projects.json` file contains a list of positions within projects and the skills required for the project.

For the purpose of this challenge, we're looking to build out an API which stores this list of people and projects, and allows for finding the most suitable candidates for a given project.

### Your task
Create a JSON based HTTP API for interacting with an Docker hosted database. Include Unit Tests.

Create 3 HTTP Endpoints:
1. POST/GET endpoint for ingesting people provided in `./resources/people.json`
2. POST/GET endpoint for ingesting projects provided in `./resources/projects.json`
3. GET endpoint taking the Unique ID of a project
 and returning the most suitable person/s.

Create docker files and config for launching the API & database.
Allow the database and API to be launched through `docker-compose up`

__Measuring suitability of person to project__
The most suitable person for a given project is the person who has the most matching skills to the required skills of the project.
If multiple people have the same number of matching skills, please return multiple people.
If there are no matching persons, indicate this within the API.

### Clarrifying/possible questions
- You can use a bulk import for provided people and projects, or individually POST each object to the endpoint
- Multiple persons/projects may have the same name

### Some notes and tips for the solution
- Solution written in Python 3.x
- SQLALchemy would assist with development time
- Feel free to use Pytest or Unittest
- Include any dependencies required in a setup.py or requirements.txt
- Use Docker for exposing the API
- We use Flask to internally expose some of our data APIs, feel free to use Flask or another python framework.


## Evaluation criteria
- Instructions for running and testing application
- Unit tests
- Functionality & Design (And comments on design)
- Docker implementation
- List any assumptions you make

## Submission of solution
To submit, please upload a `.zip` or `.tar.gz` of your codebase, and Execution instructions to to Google Drive or OneDrive, and share the link with your Dentsu Contact.

Feel free to reach out to your point of contact for clarification, or if you have any questions.