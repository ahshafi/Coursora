create table "COMMENT"
(
    ID                NUMBER default "TFUSER2"."SEQ_USER"."NEXTVAL" not null
        primary key,
    DESCRIPTION       VARCHAR2(1000),
    FORUM_ID          NUMBER                                        not null
        references FORUM,
    USER_ID           NUMBER
        constraint COMMENT_USER__FK
            references "User",
    PARENT_COMMENT_ID NUMBER
        constraint PARENT_COMMENT_ID_FK
            references "COMMENT"
                on delete cascade
)
/

INSERT INTO TFUSER2."COMMENT" (ID, DESCRIPTION, FORUM_ID, USER_ID, PARENT_COMMENT_ID) VALUES (532, 'I don''t understand the answer no.2', 526, 531, null);
INSERT INTO TFUSER2."COMMENT" (ID, DESCRIPTION, FORUM_ID, USER_ID, PARENT_COMMENT_ID) VALUES (533, 'ok', 526, 522, 532);
INSERT INTO TFUSER2."COMMENT" (ID, DESCRIPTION, FORUM_ID, USER_ID, PARENT_COMMENT_ID) VALUES (544, '123', 540, 531, 543);
INSERT INTO TFUSER2."COMMENT" (ID, DESCRIPTION, FORUM_ID, USER_ID, PARENT_COMMENT_ID) VALUES (496, 'abcd
', 484, 495, null);
INSERT INTO TFUSER2."COMMENT" (ID, DESCRIPTION, FORUM_ID, USER_ID, PARENT_COMMENT_ID) VALUES (462, 'ok', 453, 443, 461);
INSERT INTO TFUSER2."COMMENT" (ID, DESCRIPTION, FORUM_ID, USER_ID, PARENT_COMMENT_ID) VALUES (465, 'hello', 458, 451, null);
INSERT INTO TFUSER2."COMMENT" (ID, DESCRIPTION, FORUM_ID, USER_ID, PARENT_COMMENT_ID) VALUES (464, 'The answers are all correct.', 453, 443, null);
INSERT INTO TFUSER2."COMMENT" (ID, DESCRIPTION, FORUM_ID, USER_ID, PARENT_COMMENT_ID) VALUES (461, 'I don''t understand the answer ques no.2', 453, 451, null);
INSERT INTO TFUSER2."COMMENT" (ID, DESCRIPTION, FORUM_ID, USER_ID, PARENT_COMMENT_ID) VALUES (463, 'The answer is O(V+E)', 453, 443, 462);
INSERT INTO TFUSER2."COMMENT" (ID, DESCRIPTION, FORUM_ID, USER_ID, PARENT_COMMENT_ID) VALUES (543, 'abcd', 540, 531, null);
INSERT INTO TFUSER2."COMMENT" (ID, DESCRIPTION, FORUM_ID, USER_ID, PARENT_COMMENT_ID) VALUES (534, 'ok2', 526, 522, 533);
INSERT INTO TFUSER2."COMMENT" (ID, DESCRIPTION, FORUM_ID, USER_ID, PARENT_COMMENT_ID) VALUES (535, 'ok3', 526, 522, null);
