create table "Course"
(
    ID      NUMBER default "TFUSER2"."SEQ_USER"."NEXTVAL" not null,
    "Name"  VARCHAR2(100),
    "Topic" VARCHAR2(100)                                 not null,
    "Level" VARCHAR2(20)                                  not null
)
/

create unique index COURSE_ID_UINDEX
    on "Course" (ID)
/

alter table "Course"
    add constraint COURSE_PK
        primary key (ID)
/

INSERT INTO TFUSER2."Course" (ID, "Name", "Topic", "Level") VALUES (446, 'test1', 'test1', 'Beginner');
INSERT INTO TFUSER2."Course" (ID, "Name", "Topic", "Level") VALUES (537, 'Graph AlgoI', 'DS', 'Intermediate');
INSERT INTO TFUSER2."Course" (ID, "Name", "Topic", "Level") VALUES (481, 'Data Structures and Algorithms II', 'Advanced DS Algo Topics', 'Advanced');
INSERT INTO TFUSER2."Course" (ID, "Name", "Topic", "Level") VALUES (523, 'Data Structures and Algorithms III', 'DS', 'Intermediate');
INSERT INTO TFUSER2."Course" (ID, "Name", "Topic", "Level") VALUES (479, 'Fourier Analysis', 'Fourier and Laplace Transformation', 'Intermediate');
INSERT INTO TFUSER2."Course" (ID, "Name", "Topic", "Level") VALUES (444, 'Graph- Data Structures', 'Graph Algorithms', 'Intermediate');
INSERT INTO TFUSER2."Course" (ID, "Name", "Topic", "Level") VALUES (445, 'test', 'test', 'Beginner');
INSERT INTO TFUSER2."Course" (ID, "Name", "Topic", "Level") VALUES (477, 'Basic Mathematics', 'Basic maths', 'Beginner');
INSERT INTO TFUSER2."Course" (ID, "Name", "Topic", "Level") VALUES (480, 'Data Structures and Algorithms I', 'Basic DS Algo', 'Intermediate');
INSERT INTO TFUSER2."Course" (ID, "Name", "Topic", "Level") VALUES (478, 'Geometry101', 'Basic Geometry', 'Beginner');
