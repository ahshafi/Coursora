from logging.config import dictConfig
from django.shortcuts import redirect, render
from django.db import connections
from django.http import HttpResponse
from util.dictfunc import multiget

from util.fetcher import *

# Create your views here.
def show_courselist(request):
    if request.method=='POST':
      with connections['coursora_db'].cursor() as c:
         str="%";str+=request.POST['Search'];str+="%"
         c.execute('SELECT * from "Course" where "Name" like %s ',[str])
         courses=dictfetchall(c)       
         #return HttpResponse(course)
         return render(request,'courses/courselist.html',{'courses':courses,'Name':request.session['name']})
    else:      
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
    creator = 0 # if a teacher has not entered to create a lecture
    with connections['coursora_db'].cursor() as c:
         c.execute('''SELECT * from "TEACHES" where "COURSE_ID"=%s and "INSTRUCTOR_ID"=%s''',[course_id,request.session['id']])
         x=dictfetchone(c)
         if x:
             creator=1 # if a teacher has entered to create a lecture

    with connections['coursora_db'].cursor() as c:        
        
        c.execute('''SELECT ID,Title,SUMMARY,DURATION from "CONTENT" where "COURSE_ID"=%s ''',[course_id])
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
        if x or (request.method=='POST' and x1) or creator==1 :
            if request.method=='POST':
                with connections['coursora_db'].cursor() as c:
                    c.execute('''INSERT INTO "COURSE_REGISTRATION"("STUDENT_ID", "COURSE_ID")
                        VALUES(%s, %s)''', [c1, course_id])
            return render(request,'courses/contentlist.html',{'content':content,'creator':creator,'course_id':course_id})
        else:
            return render(request,'courses/contentlist_withoutaccess.html',{'content':content, 'course_id': course_id})
        #return HttpResponse(course)
        

def show_content_view(request,course_id,lec_id):
    creator = 0 # if a teacher has not entered to create a lecture
    with connections['coursora_db'].cursor() as c:
         c.execute('''SELECT * from "TEACHES" where "COURSE_ID"=%s and "INSTRUCTOR_ID"=%s''',[course_id,request.session['id']])
         x=dictfetchone(c)
         if x:
             creator=1 # if a teacher has entered to create a lecture  

    with connections['coursora_db'].cursor() as c:
        c.execute('''SELECT ID,Title,"Main_Content" from "CONTENT" where ID=%s ''',[lec_id])
        content=c.fetchall()
        c.execute('''SELECT * from "EXAM" where "CONTENT_ID"=%s ''',[lec_id])
        content1=c.fetchall()
        return render(request,'courses/contentview.html',{'content':content,'exam':content1,'creator':creator,'lec_id':lec_id})        
    


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
            db.execute('''INSERT INTO "TEACHES"("INSTRUCTOR_ID", "COURSE_ID")
                        VALUES(%s, %s)''', [request.session['id'], course_id])                        
        return redirect('/coursora/profile/')

def add_lecture(request,course_id):
    if request.method=='GET':
        return render(request, 'courses/add_lecture.html')
    else :
        Title,Summary,Duration,Main_Content=multiget(request.POST, ['Title', 'Summary', 'Duration','Main_Content'])
        with connections['coursora_db'].cursor() as db:
            db.execute('''INSERT INTO "CONTENT"("TITLE", "SUMMARY", "DURATION","COURSE_ID","Main_Content")
                        VALUES(%s, %s, %s,%s,%s)''', [Title, Summary, Duration,course_id,Main_Content])
            #return render(request, 'courses/add_lecture.html')
            str='/coursora/courselist/';str+="% s" % course_id;str+='/contentlist/'
            return redirect(str)   

def add_exam(request,lec_id):
    if request.method=='GET':
        return render(request, 'courses/add_exam.html')
    else :            
         Title,Total_Marks,Exam_Time=multiget(request.POST, ['Title', 'Total_Marks', 'Exam_Time'])
         with connections['coursora_db'].cursor() as db:
            db.execute('''INSERT INTO "EXAM"("TITLE", "TOTAL_MARKS", "CONTENT_ID","EXAM_TIME")
                        VALUES(%s, %s, %s,%s)''', [Title, Total_Marks, lec_id,Exam_Time])     
            db.execute('''SELECT * FROM "CONTENT"
                        WHERE "ID"=%s''', [lec_id])
            course_id=dictfetchone(db)['COURSE_ID']
            str='/coursora/courselist/';str+="% s" % course_id;str+='/contentlist/';str+="% s" % lec_id;str+='/view/'
            return redirect(str)

def course_progress(request, course_id):
    with connections['coursora_db'].cursor() as db:
        db.execute('''SELECT ID FROM COURSE_REGISTRATION WHERE STUDENT_ID=%s AND COURSE_ID=%s''', [request.session['id'], course_id])
        course_registration_id=dictfetchone(db)['ID']
        db.execute('''SELECT OBTAINED_MARKS, TOTAL_MARKS FROM PARTICIPATES, EXAM WHERE COURSE_REGISTRATION_ID=%s AND PARTICIPATES.EXAM_ID=EXAM.ID''', [course_registration_id])
        participated_exams=dictfetchall(db)
        db.execute('''SELECT * FROM EXAM WHERE CONTENT_ID IN (SELECT ID FROM CONTENT WHERE COURSE_ID=%s)''', [course_id])
        all_exams=dictfetchall(db)
        tot_obtained_marks, tot_obtainable_marks, tot_exam_marks=0, 0, 0
        for exam in participated_exams:
            tot_obtained_marks+=exam['OBTAINED_MARKS']
            tot_obtainable_marks+=exam['TOTAL_MARKS']
        for exam in all_exams:
            tot_exam_marks+=exam['TOTAL_MARKS']

        return render(request, 'courses/course_progress.html', {'tot_obtained_marks': tot_obtained_marks, 'tot_obtainable_marks': tot_obtainable_marks, 'tot_exam_marks': tot_exam_marks})



