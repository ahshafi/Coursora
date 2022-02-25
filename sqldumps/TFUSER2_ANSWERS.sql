create table ANSWERS
(
    COURSE_REGISTRATION_ID NUMBER not null
        references COURSE_REGISTRATION,
    QA_ID                  NUMBER not null
        references QA,
    OPTION_ANS             VARCHAR2(30),
    primary key (COURSE_REGISTRATION_ID, QA_ID)
)
/

INSERT INTO TFUSER2.ANSWERS (COURSE_REGISTRATION_ID, QA_ID, OPTION_ANS) VALUES (272, 527, 'O(V+E)');
INSERT INTO TFUSER2.ANSWERS (COURSE_REGISTRATION_ID, QA_ID, OPTION_ANS) VALUES (272, 528, 'O(V+E2)');
INSERT INTO TFUSER2.ANSWERS (COURSE_REGISTRATION_ID, QA_ID, OPTION_ANS) VALUES (273, 527, 'O(V+E2)');
INSERT INTO TFUSER2.ANSWERS (COURSE_REGISTRATION_ID, QA_ID, OPTION_ANS) VALUES (273, 528, 'O(V+E)');
INSERT INTO TFUSER2.ANSWERS (COURSE_REGISTRATION_ID, QA_ID, OPTION_ANS) VALUES (278, 541, 'O(V+E)');
INSERT INTO TFUSER2.ANSWERS (COURSE_REGISTRATION_ID, QA_ID, OPTION_ANS) VALUES (278, 542, 'O(V+E2)');
INSERT INTO TFUSER2.ANSWERS (COURSE_REGISTRATION_ID, QA_ID, OPTION_ANS) VALUES (277, 530, 'O(VlogV + E)');
INSERT INTO TFUSER2.ANSWERS (COURSE_REGISTRATION_ID, QA_ID, OPTION_ANS) VALUES (277, 527, 'O(V+E)');
INSERT INTO TFUSER2.ANSWERS (COURSE_REGISTRATION_ID, QA_ID, OPTION_ANS) VALUES (277, 528, 'O(V+E)');
INSERT INTO TFUSER2.ANSWERS (COURSE_REGISTRATION_ID, QA_ID, OPTION_ANS) VALUES (272, 530, 'O(VlogV + E)');
