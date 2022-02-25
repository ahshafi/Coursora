create table FORUM
(
    FORUM_ID NUMBER default "TFUSER2"."SEQ_USER"."NEXTVAL" not null
        primary key,
    TITLE    VARCHAR2(100),
    EXAM_ID  NUMBER                                        not null
        references EXAM
)
/

INSERT INTO TFUSER2.FORUM (FORUM_ID, TITLE, EXAM_ID) VALUES (453, 'Discussion Forum', 1);
INSERT INTO TFUSER2.FORUM (FORUM_ID, TITLE, EXAM_ID) VALUES (529, 'Discussion Forum', 6);
INSERT INTO TFUSER2.FORUM (FORUM_ID, TITLE, EXAM_ID) VALUES (484, 'Discussion Forum', 3);
INSERT INTO TFUSER2.FORUM (FORUM_ID, TITLE, EXAM_ID) VALUES (526, 'Discussion Forum', 5);
INSERT INTO TFUSER2.FORUM (FORUM_ID, TITLE, EXAM_ID) VALUES (458, 'Discussion Forum', 2);
INSERT INTO TFUSER2.FORUM (FORUM_ID, TITLE, EXAM_ID) VALUES (490, 'Discussion Forum', 4);
INSERT INTO TFUSER2.FORUM (FORUM_ID, TITLE, EXAM_ID) VALUES (540, 'Discussion Forum', 7);
