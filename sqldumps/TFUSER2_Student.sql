create table "Student"
(
    ID      NUMBER not null
        primary key
        constraint STUDENT_USER__FK
            references "User",
    "Class" VARCHAR2(100)
)
/

INSERT INTO TFUSER2."Student" (ID, "Class") VALUES (495, '10');
INSERT INTO TFUSER2."Student" (ID, "Class") VALUES (531, 'L1 T1');
INSERT INTO TFUSER2."Student" (ID, "Class") VALUES (441, 'BSc 1st year');
INSERT INTO TFUSER2."Student" (ID, "Class") VALUES (472, '10');
INSERT INTO TFUSER2."Student" (ID, "Class") VALUES (451, 'L1 T1');
INSERT INTO TFUSER2."Student" (ID, "Class") VALUES (456, '12');
INSERT INTO TFUSER2."Student" (ID, "Class") VALUES (501, '12');
INSERT INTO TFUSER2."Student" (ID, "Class") VALUES (469, 'BSc 1st year');
INSERT INTO TFUSER2."Student" (ID, "Class") VALUES (471, 'L2 T2');
