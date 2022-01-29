from django.db import connections
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from util.dictfunc import multidel, multiget, multiset
from util.fetcher import *
# Create your views here.

def home(request):
    return render(request,'home.html')

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    temp=cursor.fetchall()    
    return temp

def register_student(request):
    if request.method=='POST':
        name, email, password,Class=multiget(request.POST, ['name', 'email', 'password','Class'])
        TS_ID=1
        multiset(request.session, ['name', 'email', 'password','Class','ID'], [name, email, password,Class,TS_ID])
        with connections['coursora_db'].cursor() as db:
            db.execute('''INSERT INTO "User"("Name", "Email", "Password")
                        VALUES(%s, %s, %s)''', [name, email, password])
            db.execute('''SELECT ID FROM "User"
                        WHERE "Name"=%s AND "Password"=%s ''', [name, password])
            x=dictfetchall(db)          
            db.execute('''INSERT INTO "Student"("ID", "Class")
                        VALUES(%s, %s)''', [x[0][0],Class])
            return redirect('/coursora/profile/')
    elif 'name' not in request.session:
        return render(request, 'register_student.html')
    else:
        return redirect('/coursora/profile/')

def register_teacher(request):
    if request.method=='POST':
        name, email, password,Specialization=multiget(request.POST, ['name', 'email', 'password','Specialization'])
        TS_ID=2
        multiset(request.session, ['name', 'email', 'password','Specialization','ID'], [name, email, password, Specialization,TS_ID])
        with connections['coursora_db'].cursor() as db:
            db.execute('''INSERT INTO "User"("Name", "Email", "Password")
                        VALUES(%s, %s, %s)''', [name, email, password])
            db.execute('''SELECT ID FROM "User"
                        WHERE "Name"=%s AND "Password"=%s ''', [name, password])
            x=dictfetchall(db)          
            db.execute('''INSERT INTO "Instructor"("ID", "Specialization")
                        VALUES(%s, %s)''', [x[0][0],Specialization])
            return redirect('/coursora/profile/')
    elif 'name' not in request.session:
        return render(request, 'register_teacher.html')
    else:
        return redirect('/coursora/profile/')

def login(request):
    if 'name' in request.session: 
        return redirect('/coursora/profile/')
    elif request.method == 'GET':
       return render(request, 'login.html')
    else:
        name, password=multiget(request.POST, ['name', 'password'])
        with connections['coursora_db'].cursor() as db:
            db.execute('''SELECT * FROM "User"
                        WHERE "Name"=%s AND "Password"=%s ''', [name, password])
            qres = dictfetchone(db)
            if qres is not None:
                multiset(request.session, ['name', 'email', 'password'], multiget(qres, ['Name', 'Email', 'Password']))
                return redirect('/coursora/profile')
            else:
                return redirect('/coursora/login')
                

def profile(request):
    context = { 'name':request.session['name'] }
    with connections['coursora_db'].cursor() as db:            
            db.execute('''SELECT ID FROM "User"
                        WHERE "Name"=%s AND "Password"=%s ''', [request.session['name'], request.session['password']])
            x=dictfetchall(db)
            ID=x[0][0]          
            db.execute('''SELECT ID FROM "Instructor"
                        WHERE "ID"=%s''', [x[0][0]])
            x=dictfetchone(db)
            if x is not None:
                with connections['coursora_db'].cursor() as db:            
                       db.execute('''SELECT * FROM "User"
                            WHERE "ID"=%s ''', [ID])
                       x1=dictfetchall(db)
                       db.execute('''SELECT * FROM "Instructor"
                            WHERE "ID"=%s ''', [ID])
                       x2=dictfetchall(db)
                       db.execute('''SELECT * FROM "Course"
                            WHERE "ID" in(
                                select "COURSE_ID" from "Teaches"
                                where "TEACHER_ID"=%s
                            ) ''', [ID])
                       x3=dictfetchall(db)

                       return render(request, 'teacher_profile.html', {'info1':x1,'info2':x2,'info3':x3})
            else :
              with connections['coursora_db'].cursor() as db:            
                        db.execute('''SELECT * FROM "User"
                            WHERE "ID"=%s ''', [ID])
                        x1=dictfetchall(db)
                        db.execute('''SELECT * FROM "Student"
                            WHERE "ID"=%s ''', [ID])
                        x2=dictfetchall(db)
                        db.execute('''SELECT * FROM "Course"
                            WHERE "ID" in(
                                select "Course_ID" from "Course_Registration"
                                where "Student_ID"=%s
                            ) ''', [ID])
                        x3=dictfetchall(db)

                        return render(request, 'student_profile.html',{'info1':x1,'info2':x2,'info3':x3})


def logout(request):
    multidel(request.session, ['name', 'email', 'password'])
    return redirect('/coursora/login/')
    

    