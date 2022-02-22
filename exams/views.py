from django.shortcuts import redirect, render
from django.db import connections
from django.http import HttpResponse
from util.dictfunc import multiget

from util.fetcher import *

def exam(request, exam_id):
    with connections['coursora_db'].cursor() as db:
        db.execute('''SELECT * from "EXAM" where "ID"=%s''',[exam_id])
        lec_id=dictfetchone(db)['CONTENT_ID']
        db.execute('''SELECT * from "CONTENT" where "ID"=%s''',[lec_id])
        course_id=dictfetchone(db)['COURSE_ID']
        db.execute('''SELECT * from "EXAM" where "ID"=%s''',[exam_id])
        exam_detail=dictfetchone(db)
        db.execute('''SELECT * from "TEACHES" where "COURSE_ID"=%s and "INSTRUCTOR_ID"=%s''',[course_id,request.session['id']])
        is_teacher=dictfetchone(db)
        if is_teacher:
            db.execute('''SELECT * FROM QA WHERE EXAM_ID=%s''', [exam_id])
            questions=dictfetchall(db)
            return render(request, 'exams/questions.html', {'questions':questions, 'exam_id': exam_id,'exam_detail':exam_detail,'creator': True, 'participated': False})  
    
        db.execute('''SELECT * 
        FROM "EXAM" JOIN  "CONTENT" ON ("EXAM"."CONTENT_ID"="CONTENT"."ID")
        JOIN "Course" ON ("CONTENT"."COURSE_ID"="Course"."ID")
        JOIN "COURSE_REGISTRATION" 
        ON ("COURSE_REGISTRATION"."COURSE_ID"="Course"."ID" AND "COURSE_REGISTRATION"."STUDENT_ID"=%s)''', [request.session['id']])
        registered=dictfetchall(db)
        if not registered:
           return HttpResponse('course not registered')
        
        course_registration_id=get_course_registration_id(request.session['id'], exam_id)

        db.execute('''SELECT * FROM PARTICIPATES WHERE COURSE_REGISTRATION_ID=%s 
        AND EXAM_ID=%s''', [course_registration_id, exam_id])
        participated=dictfetchall(db)
        questions=get_questions(exam_id)
        if participated:
            db.execute('''SELECT OBTAINED_MARKS FROM PARTICIPATES
            WHERE COURSE_REGISTRATION_ID=%s AND EXAM_ID=%s''', [course_registration_id, exam_id])
            marks=dictfetchone(db)['OBTAINED_MARKS']
            db.execute('''SELECT QA.ID ID, OPTION1, OPTION2, OPTION3, OPTION4, ANSWER, OPTION_ANS FROM QA, ANSWERS 
            WHERE QA.ID=ANSWERS.QA_ID AND ANSWERS.COURSE_REGISTRATION_ID=%s''', [course_registration_id])
            submission=dictfetchall(db)
            return render(request, 'exams/answers.html', {'submission': submission,'marks': marks, 'exam_id': exam_id,'exam_detail':exam_detail})
        elif request.method=='POST':
            db.execute('''INSERT INTO PARTICIPATES(COURSE_REGISTRATION_ID, EXAM_ID) VALUES(%s, %s)''',
            [course_registration_id, exam_id])
            correct=0
            for question in questions:
                db.execute('''INSERT INTO ANSWERS(COURSE_REGISTRATION_ID, QA_ID, OPTION_ANS) VALUES(%s, %s, %s)''',
                [course_registration_id, question['ID'], request.POST[str(question['ID'])]])
                correct=correct+(question['ANSWER']==request.POST[str(question['ID'])])
                
            marks=exam_detail['TOTAL_MARKS']*(correct/len(questions))
            db.execute('''UPDATE PARTICIPATES SET OBTAINED_MARKS=%s 
            WHERE COURSE_REGISTRATION_ID=%s AND EXAM_ID=%s''', [marks, course_registration_id, exam_id])
            return redirect('/coursora/exam/'+str(exam_id)+'/')
        else :
            return render(request, 'exams/questions.html', {'questions':questions, 'exam_id': exam_id,'exam_detail':exam_detail,'creator': False})

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


def get_course_registration_id(student_id, exam_id):
    with connections['coursora_db'].cursor() as db:
        db.execute('''SELECT COURSE_REGISTRATION.ID
            FROM COURSE_REGISTRATION, CONTENT, EXAM
            WHERE COURSE_REGISTRATION.STUDENT_ID=%s 
            AND COURSE_REGISTRATION.COURSE_ID=CONTENT.COURSE_ID 
            AND CONTENT.ID=EXAM.CONTENT_ID
            AND EXAM.ID=%s''', 
            [student_id, exam_id])
        return dictfetchone(db)['ID']

def get_questions(exam_id):
    with connections['coursora_db'].cursor() as db:
        db.execute('''SELECT * FROM QA WHERE EXAM_ID=%s''', [exam_id])
        questions=dictfetchall(db)
        return questions

# def evaluate(student_id, exam_id):
    