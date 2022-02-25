create table "Instructor"
(
    ID               NUMBER not null
        constraint INSTRUCTOR_USER_ID_FK
            references "User",
    "Specialization" VARCHAR2(20),
    STATUS           VARCHAR2(10)
)
/

create unique index INSTRUCTOR_ID_UINDEX
    on "Instructor" (ID)
/

alter table "Instructor"
    add constraint INSTRUCTOR_PK
        primary key (ID)
/

INSERT INTO TFUSER2."Instructor" (ID, "Specialization", STATUS) VALUES (475, 'CS', 'approved');
INSERT INTO TFUSER2."Instructor" (ID, "Specialization", STATUS) VALUES (476, 'Physics', 'approved');
INSERT INTO TFUSER2."Instructor" (ID, "Specialization", STATUS) VALUES (522, 'CS', 'approved');
INSERT INTO TFUSER2."Instructor" (ID, "Specialization", STATUS) VALUES (470, 'EEE', 'approved');
INSERT INTO TFUSER2."Instructor" (ID, "Specialization", STATUS) VALUES (536, 'CS', 'approved');
INSERT INTO TFUSER2."Instructor" (ID, "Specialization", STATUS) VALUES (474, 'Math', 'approved');
INSERT INTO TFUSER2."Instructor" (ID, "Specialization", STATUS) VALUES (443, 'CS', 'approved');
