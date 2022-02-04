from django.shortcuts import redirect, render
from django.db import connections
from django.http import HttpResponse
from util.dictfunc import multiget

from util.fetcher import *

# Create your views here.
def show_courselist(request): 
      with connections['coursora_db'].cursor() as c:
        c.execute('SELECT * from "Course"')
        courses=dictfetchall(c)       
        #return HttpResponse(course)
        return render(request,'courses/courselist.html',{'courses':courses,'Name':request.session['name']})  

def course_reg(request,course_id):
    if  request.session['role']=='instructor':
        return HttpResponse('Only students can register')
    with connections['coursora_db'].cursor() as db:
        db.execute('''INSERT INTO "COURSE_REGISTRATION"("STUDENT_ID", "COURSE_ID") VALUES(%s, %s)''', [request.session['id'], course_id])
        return show_contentlist(request,course_id)
    

def show_contentlist(request,course_id):   
    with connections['coursora_db'].cursor() as c:
        
        c.execute('''SELECT ID,Title,SUMMARY,DURATION from "CONTENT" where "Course_ID"=%s ''',[course_id])
        content=c.fetchall() 
        c.execute('''SELECT ID FROM "User"
                        WHERE "Name"=%s AND "Password"=%s ''', [request.session['name'], request.session['password']])
        x=c.fetchall() 
        c1=x[0][0]
        c.execute('''SELECT * from "COURSE_REGISTRATION" 
                     where "STUDENT_ID"=%s and "COURSE_ID"=%s''',[c1,course_id])
        x=dictfetchone(c)
        c.execute('''SELECT * from "Student" 
                     where "ID"=%s ''',[c1])
        x1=dictfetchone(c)
        if x or (request.method=='POST' and x1):
            if request.method=='POST':
                with connections['coursora_db'].cursor() as c:
                    c.execute('''INSERT INTO "COURSE_REGISTRATION"("STUDENT_ID", "COURSE_ID")
                        VALUES(%s, %s)''', [c1, course_id])
            return render(request,'courses/contentlist.html',{'content':content})
        else:
            return render(request,'courses/contentlist_withoutaccess.html',{'content':content, 'course_id': course_id})
        #return HttpResponse(course)
        

def show_content_view(request,course_id,lec_id):    
    with connections['coursora_db'].cursor() as c:
        c.execute('''SELECT ID,Title,"Main_Content" from "CONTENT" where ID=%s ''',[lec_id])
        content=c.fetchall()        
    with connections['coursora_db'].cursor() as d:
        d.execute('''SELECT * from "EXAM" where "Content_ID"=%s ''',[lec_id])
        content1=c.fetchall() 
        #return HttpResponse(course)
    return render(request,'courses/contentview.html',{'content':content,'exam':content1})


def add_course(request):
    if request.method=='GET':
        return render(request, 'courses/add_course.html')
    else :
        name, topic, level=multiget(request.POST, ['name', 'topic', 'level'])
        with connections['coursora_db'].cursor() as db:
            db.execute('''INSERT INTO "Course"("Name", "Topic", "Level")
                        VALUES(%s, %s, %s)''', [name, topic, level])
            db.execute('''SELECT ID FROM "Course"
                        WHERE "Name"=%s''', [name])
            course_id=dictfetchone(db)['ID']
            db.execute('''INSERT INTO "Teaches"("INSTRUCTOR_ID", "COURSE_ID")
                        VALUES(%s, %s)''', [request.session['id'], course_id])
        return redirect('/coursora/profile/')

def show_contentlist_instructor(request, id):
    pass



