# Coursora
Coursora is an online learning platform where students can widen their knowledge on different topics and teachers can spread their knowledge via different courses.

## Follow the steps stated below to run the server

### Install latest version of python.

### Install django

    pip install django
    
### Clone the project into a directory
    git clone https://github.com/ahshafi/Coursora.git .
    
### Create a new oracle user into your system named 'c##coursora' with password: coursora 
	```
	create user c##coursora identified by coursora
	grant dba to c##coursora
	```
### Runs the scripts contained in the sqldumps folder. It will create all the tables, procedures and triggers
    
### Run the server
    python manage.py runserver

### Go the following link
[<b>Coursora</b>](http://127.0.0.1:8000/coursora/)



Video Demonstration of the project-
https://www.youtube.com/watch?v=agsbupE0l4Q
