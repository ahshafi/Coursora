create table "User"
(
    ID            NUMBER default "TFUSER2"."SEQ_USER"."NEXTVAL" not null
        primary key,
    "Name"        VARCHAR2(20)
        constraint UNIQUE_NAME
            unique,
    "Email"       VARCHAR2(100)
        constraint UNIQUE_EMAIL
            unique,
    "Password"    VARCHAR2(30),
    "Institution" VARCHAR2(100)
)
/

INSERT INTO TFUSER2."User" (ID, "Name", "Email", "Password", "Institution") VALUES (476, 'Einstein', 'einstein@gmail.com', '123', 'BUET');
INSERT INTO TFUSER2."User" (ID, "Name", "Email", "Password", "Institution") VALUES (495, 'saadianuha', 'furutawashuu2711@gmail.com', 'naruto2022', 'udayan');
INSERT INTO TFUSER2."User" (ID, "Name", "Email", "Password", "Institution") VALUES (522, 'teacher5', 'teacher5@gmail.com', '1234', 'BUET');
INSERT INTO TFUSER2."User" (ID, "Name", "Email", "Password", "Institution") VALUES (531, 'student1', 'student1@gmail.com', '1234', 'BUET');
INSERT INTO TFUSER2."User" (ID, "Name", "Email", "Password", "Institution") VALUES (470, 'teacher2', 'teacher2@gmail.com', '2345', 'BUET');
INSERT INTO TFUSER2."User" (ID, "Name", "Email", "Password", "Institution") VALUES (475, 'teacher3', 't@gmail.com', '345', 'BUET');
INSERT INTO TFUSER2."User" (ID, "Name", "Email", "Password", "Institution") VALUES (441, 'abcd', 'abcd@gmail.com', '1234', 'BUET');
INSERT INTO TFUSER2."User" (ID, "Name", "Email", "Password", "Institution") VALUES (536, 'teacher6', 'teacher6@gmail.com', '1234', 'BUET');
INSERT INTO TFUSER2."User" (ID, "Name", "Email", "Password", "Institution") VALUES (1, 'Admin', 'admin@gmail.com', 'admin', null);
INSERT INTO TFUSER2."User" (ID, "Name", "Email", "Password", "Institution") VALUES (456, 'testuser1', 'testuser1@gmail.com', '1234', 'BUET');
INSERT INTO TFUSER2."User" (ID, "Name", "Email", "Password", "Institution") VALUES (472, 'Nuha', 'nuha123@gmail.com', '2345', 'abcd');
INSERT INTO TFUSER2."User" (ID, "Name", "Email", "Password", "Institution") VALUES (474, 'John', 'john@gmail.com', '456', 'BUET');
INSERT INTO TFUSER2."User" (ID, "Name", "Email", "Password", "Institution") VALUES (501, 'J Hunt', 'jhunt@gmail.com', '1234', 'TU');
INSERT INTO TFUSER2."User" (ID, "Name", "Email", "Password", "Institution") VALUES (443, 'teacher1', 'teacher1@gmail.com', '1234', 'BUET');
INSERT INTO TFUSER2."User" (ID, "Name", "Email", "Password", "Institution") VALUES (451, 'Rafiq', 'Rafiq@gmail.com', '1234', 'BUET');
INSERT INTO TFUSER2."User" (ID, "Name", "Email", "Password", "Institution") VALUES (469, 'Karim', 'karim@gmail.com', '2345', 'BUET');
INSERT INTO TFUSER2."User" (ID, "Name", "Email", "Password", "Institution") VALUES (471, 'Rumi', 'amsrumi@gmail.com', '3456', 'BUET');
