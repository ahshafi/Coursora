from django.shortcuts import redirect, render
from django.db import connections
from django.http import HttpResponse

from util.fetcher import dictfetchone

# Create your views here.
def show_course_list(request):    
     with connections['coursora_db'].cursor() as c:
        
        c.execute('SELECT * from "Course"')
        course=dictfetchall(c)        
        #return HttpResponse(course)
        return render(request,'courselist.html',{'course':course,'Name':request.session['name']})  

def course_reg(request,course_id):
    return show_content_list(request,course_id)

def dictfetchall1(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]    
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    temp=cursor.fetchall()    
    return temp

def show_content_list(request,course_id):   
    with connections['coursora_db'].cursor() as c:
        c.execute('''SELECT ID,Title,SUMMARY,DURATION from "CONTENT" where "Course_ID"=%s ''',[course_id])
        content=dictfetchall(c)
        c.execute('''SELECT ID FROM "User"
                        WHERE "Name"=%s AND "Password"=%s ''', [request.session['name'], request.session['password']])
        x=dictfetchall(c)
        c1=x[0][0]
        c.execute('''SELECT * from "Course_Registration" 
                     where "Student_ID"=%s and "Course_ID"=%s''',[c1,course_id])
        x=dictfetchone(c)
        c.execute('''SELECT * from "Student" 
                     where "ID"=%s ''',[c1])
        x1=dictfetchone(c)
        if x is not None or (request.method=='POST' and x1 is not None):
            if request.method=='POST':
                with connections['coursora_db'].cursor() as c:
                    c.execute('''INSERT INTO "Course_Registration"("Student_ID", "Course_ID")
                        VALUES(%s, %s)''', [c1, course_id])
            return render(request,'contentlist.html',{'content':content})
        else:
            return render(request,'contentlist_withoutaccess.html',{'content':content})
        #return HttpResponse(course)
        

def show_content_view(request,course_id,lec_id):    
    with connections['coursora_db'].cursor() as c:
        c.execute('''SELECT ID,Title,"Main_Content" from "CONTENT" where ID=%s ''',[lec_id])
        content=dictfetchall(c)        
    with connections['coursora_db'].cursor() as d:
        d.execute('''SELECT * from "EXAM" where "Content_ID"=%s ''',[lec_id])
        content1=dictfetchall(d)
        #return HttpResponse(course)
    return render(request,'contentview.html',{'content':content,'exam':content1})