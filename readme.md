# Data Engineering Challenge

## What have accomplised so far
- Created separeated container for web and database 
- Used Python and Flask for API development
- MySql is the tool of choice for database
- Web app can communicate with the databse server of a different container
- contianer specs are defined in separate Dockerfiles under build/
- Deployment is done using docker-compose.yml
- Fuctionality is incomplete at the moment. Only API GET and POST functionality is implemented
- 

## How to run the app
in the root folder run the shell script "runme.sh"
./runme.sh

## API URLs
http://localhost:5000/
http://localhost:5000/people
http://localhost:5000/people/<first_name> e.g. http://localhost:5000/people/Aldis
http://localhost:5000/
http://localhost:5000/<project_name> e.g.http://localhost:5000/project/Hatity

## PUT funciton
### People API
```
curl -X POST http://localhost:5000/people -H 'Content-Type: application/json' -d '{"first_name": "Ali",
 "last_name": "Baig",
 "email": "ali.hammad@yahoo.com",
 "address": "my home address",
 "skills": "data anlysisdata engineering"
 }'
```
### Project API
```
curl -X POST http://localhost:5000/project -H 'Content-Type: application/json' -d '{"project_name": "my project",
"date_posted": "23/02/2021",
"department": "Data Analytics",
"description": "we make the data science work",
"skills": "ML, data engineering"
}'
```

