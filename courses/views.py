from django.shortcuts import render
from django.db import connections
from django.http import HttpResponse

# Create your views here.
def show_course_list(request):    
     with connections['coursora_db'].cursor() as c:
        c.execute('SELECT * from "Course"')
        course=dictfetchall(c)
        #return HttpResponse(course)
        return render(request,'courselist.html',{'course':course})  



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
        #return HttpResponse(course)
        return render(request,'contentlist.html',{'content':content})

def show_content_view(request,course_id,lec_id):    
    with connections['coursora_db'].cursor() as c:
        c.execute('''SELECT ID,Title,"Main_Content" from "CONTENT" where ID=%s ''',[lec_id])
        content=dictfetchall(c)        
    with connections['coursora_db'].cursor() as d:
        d.execute('''SELECT * from "EXAM" where "Content_ID"=%s ''',[lec_id])
        content1=dictfetchall(d)
        #return HttpResponse(course)
    return render(request,'contentview.html',{'content':content,'exam':content1})