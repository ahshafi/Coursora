create table CONTENT
(
    ID             NUMBER default "TFUSER2"."SEQ_USER"."NEXTVAL" not null
        primary key,
    TITLE          VARCHAR2(100)                                 not null,
    SUMMARY        VARCHAR2(1000),
    DURATION       NUMBER                                        not null,
    COURSE_ID      NUMBER
        constraint CONTENT_COURSE__FK
            references "Course",
    "Main_Content" VARCHAR2(1000)
)
/

INSERT INTO TFUSER2.CONTENT (ID, TITLE, SUMMARY, DURATION, COURSE_ID, "Main_Content") VALUES (450, 'Dijkstra2', 'same', 40, 444, 'https://www.youtube.com/embed/2E7MmKv0Y24');
INSERT INTO TFUSER2.CONTENT (ID, TITLE, SUMMARY, DURATION, COURSE_ID, "Main_Content") VALUES (482, 'Addition', 'We will learn about basic addition process', 10, 477, 'https://www.youtube.com/embed/mAvuom42NyY');
INSERT INTO TFUSER2.CONTENT (ID, TITLE, SUMMARY, DURATION, COURSE_ID, "Main_Content") VALUES (539, 'Dijkstra', 'We shall learn about Dijkstra', 50, 537, 'https://www.youtube.com/embed/2E7MmKv0Y24');
INSERT INTO TFUSER2.CONTENT (ID, TITLE, SUMMARY, DURATION, COURSE_ID, "Main_Content") VALUES (448, 'Dijkstra', 'Overview of Dijkstra and calculation of its complexity', 50, 444, 'https://www.youtube.com/embed/2E7MmKv0Y24');
INSERT INTO TFUSER2.CONTENT (ID, TITLE, SUMMARY, DURATION, COURSE_ID, "Main_Content") VALUES (525, 'Dijkstra', 'We shall learn about Dijkstra', 50, 523, 'https://www.youtube.com/embed/2E7MmKv0Y24');
INSERT INTO TFUSER2.CONTENT (ID, TITLE, SUMMARY, DURATION, COURSE_ID, "Main_Content") VALUES (538, 'BFS+DFS', 'We shall learn about DFS and BFS', 10, 537, 'https://www.youtube.com/embed/s-CYnVz-uh4');
INSERT INTO TFUSER2.CONTENT (ID, TITLE, SUMMARY, DURATION, COURSE_ID, "Main_Content") VALUES (447, 'DFS+BFS', 'We shall learn about DFS and BFS in this lecture', 30, 444, 'https://www.youtube.com/embed/s-CYnVz-uh4');
INSERT INTO TFUSER2.CONTENT (ID, TITLE, SUMMARY, DURATION, COURSE_ID, "Main_Content") VALUES (449, 'Dijkstra1', 'same', 50, 444, '"https://www.youtube.com/embed/2E7MmKv0Y24"');
INSERT INTO TFUSER2.CONTENT (ID, TITLE, SUMMARY, DURATION, COURSE_ID, "Main_Content") VALUES (524, 'DFS+BFS', 'We shall learn about DFS and BFS in this lecture', 10, 523, 'https://www.youtube.com/embed/s-CYnVz-uh4');
INSERT INTO TFUSER2.CONTENT (ID, TITLE, SUMMARY, DURATION, COURSE_ID, "Main_Content") VALUES (483, 'Substraction', 'We will learn about basic substraction process', 10, 477, 'https://www.youtube.com/embed/mAvuom42NyY');
