from django.shortcuts import redirect, render
from django.db import connections
from django.http import HttpResponse
from util.dictfunc import multiget

from util.fetcher import *

def exam(request, exam_id):
    creator = 0 # if a teacher has not entered to create an exam
    with connections['coursora_db'].cursor() as db:
         db.execute('''SELECT * from "EXAM" where "ID"=%s''',[exam_id])
         lec_id=dictfetchone(db)['CONTENT_ID']
         db.execute('''SELECT * from "CONTENT" where "ID"=%s''',[lec_id])
         course_id=dictfetchone(db)['COURSE_ID']
         db.execute('''SELECT * from "Teaches" where "COURSE_ID"=%s and "INSTRUCTOR_ID"=%s''',[course_id,request.session['id']])
         x=dictfetchone(db)
         if x:
             creator=1 # if a teacher has entered to create an exam  
    with connections['coursora_db'].cursor() as db:
        db.execute('''SELECT * 
        FROM "EXAM" JOIN  "CONTENT" ON ("EXAM"."CONTENT_ID"="CONTENT"."ID")
        JOIN "Course" ON ("CONTENT"."COURSE_ID"="Course"."ID")
        JOIN "COURSE_REGISTRATION" 
        ON ("COURSE_REGISTRATION"."COURSE_ID"="Course"."ID" AND "COURSE_REGISTRATION"."STUDENT_ID"=%s)''', [request.session['id']])
        registered=dictfetchall(db)

        db.execute('''SELECT * from "EXAM" where "ID"=%s''',[exam_id])
        exam_detail=dictfetchone(db)
        
        # print(registered is None)
        # return HttpResponse(registered)
        if creator==1: # for teachers
            db.execute('''SELECT * FROM QA WHERE EXAM_ID=%s''', [exam_id])
            questions=dictfetchall(db)
            return render(request, 'exams/questions.html', {'questions':questions, 'exam_id': exam_id,'exam_detail':exam_detail,'creator':creator})
        if not registered:
           return HttpResponse('course not registered')

        if request.method=='POST':
            return HttpResponse(request.POST['1'])
        else :
            db.execute('''SELECT * FROM QA WHERE EXAM_ID=%s''', [exam_id])
            questions=dictfetchall(db)
            return render(request, 'exams/questions.html', {'questions':questions, 'exam_id': exam_id,'exam_detail':exam_detail,'creator':creator})

def add_ques(request,exam_id):
    #str='/coursora/exam/';str+="% s" % exam_id;str+='/addquestion/'
    if request.method=='POST':        
        Question,Op1,Op2,Op3,Op4,Answer=multiget(request.POST, ['Question','Op1','Op2','Op3','Op4','Answer'])
        with connections['coursora_db'].cursor() as db:
            db.execute('''INSERT INTO "QA"("OPTION1", "OPTION2", "OPTION3","OPTION4","ANSWER","EXAM_ID","QUESTION")
                        VALUES(%s, %s, %s,%s,%s,%s,%s)''', [Op1,Op2,Op3,Op4,Answer,exam_id,Question])
            str='/coursora/exam/';str+="% s" % exam_id;str+="/"
            return redirect(str) 
    else :
       return render(request,'exams/addquestion.html') 