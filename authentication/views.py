from django.db import connections
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from util.dictfunc import multidel, multiget, multiset
from util.fetcher import *
from django.urls import reverse
# Create your views here.

def home(request):
    return render(request,'authentication/home.html')

def register_student(request):
    if request.method=='POST':
        name, email, password,klass=multiget(request.POST, ['name', 'email', 'password','klass'])
        
        with connections['coursora_db'].cursor() as db:
            db.execute('''INSERT INTO "User"("Name", "Email", "Password")
                        VALUES(%s, %s, %s)''', [name, email, password])
            db.execute('''SELECT ID FROM "User"
                        WHERE "Name"=%s AND "Password"=%s ''', [name, password])
            id=dictfetchone(db)['ID']
            request.session['id']=id;          
            db.execute('''INSERT INTO "Student"("ID", "Class")
                        VALUES(%s, %s)''', [id,klass])
            return redirect('/coursora/profile/')
    elif 'id' not in request.session:
        return render(request, 'authentication/register_student.html')
    else:
        return redirect('/coursora/profile/')

def register_teacher(request):
    if request.method=='POST':
        name, email, password,specialization=multiget(request.POST, ['name', 'email', 'password','specialization'])
        
        with connections['coursora_db'].cursor() as db:
            db.execute('''INSERT INTO "User"("Name", "Email", "Password")
                        VALUES(%s, %s, %s)''', [name, email, password])
            db.execute('''SELECT ID FROM "User"
                        WHERE "Name"=%s AND "Password"=%s ''', [name, password])
            id=dictfetchone(db)['ID']
            db.execute('''INSERT INTO "Instructor"("ID", "Specialization", "STATUS")
                        VALUES(%s, %s, %s)''', [id,specialization, 'pending'])
            return redirect('/coursora/profile/')
    elif 'id' not in request.session:
        return render(request, 'authentication/register_teacher.html')
    else:
        return redirect('/coursora/profile/')

def login(request):
    if 'id' in request.session: 
        return redirect('/coursora/profile/')
    elif request.method == 'GET':
       return render(request, 'authentication/login.html')
    else:
        name, password=multiget(request.POST, ['name', 'password'])
        with connections['coursora_db'].cursor() as db:
            db.execute('''SELECT * FROM "User"
                        WHERE "Name"=%s AND "Password"=%s ''', [name, password])
            user = dictfetchone(db)
            if user is not None:
                db.execute('''SELECT * FROM "Instructor"
                        WHERE "ID"=%s ''', [user['ID']])
                instructor=dictfetchone(db)
                if (instructor is not None) and instructor['STATUS']!='approved':
                    return HttpResponse('Please wait for admin approval')
                request.session['id']=user['ID']
                return redirect('/coursora/profile/')
            else:
                return redirect('/coursora/login/')
                

def profile(request):
    with connections['coursora_db'].cursor() as db:
            if 'id' not in request.session:
                return redirect('/coursora/login/')          
            
            db.execute('''SELECT * FROM "User"
                        WHERE "ID"=%s ''', [request.session['id']])
            user=dictfetchone(db)
            
            db.execute('''SELECT * FROM "Instructor"
                        WHERE "ID"=%s''', [user['ID']])
            instructor=dictfetchone(db)

            db.execute('''SELECT * FROM "Student"
                        WHERE "ID"=%s''', [user['ID']])
            student=dictfetchone(db)

            if instructor is not None:
                db.execute('''SELECT * FROM "Course"
                            WHERE "ID" in(
                                select "COURSE_ID" from "Teaches"
                                where "INSTRUCTOR_ID"=%s
                            ) ''', [instructor['ID']])
                courses=dictfetchall(db)
                return render(request, 'authentication/teacher_profile.html', {'user':user,'instructor':instructor,'courses':courses})            
                     
                    
            elif student is not None :
                db.execute('''SELECT * FROM "Course"
                    WHERE "ID" in(
                        select "Course_ID" from "Course_Registration"
                        where "Student_ID"=%s
                    ) ''', [student['ID']])
                courses=dictfetchall(db)
                return render(request, 'authentication/student_profile.html',{'user':user,'student':student,'courses':courses})
            

def logout(request):
    #multidel(request.session, ['name', 'email', 'password'])
    request.session.clear()
    return redirect('/coursora/login/')
    

    