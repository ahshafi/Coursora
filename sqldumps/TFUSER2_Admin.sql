create table "Admin"
(
    ID             NUMBER not null
        constraint ADMIN_PK
            primary key
        constraint ADMIN_USER__FK
            references "User",
    "Admin_field1" VARCHAR2(20)
)
/

INSERT INTO TFUSER2."Admin" (ID, "Admin_field1") VALUES (1, 'admin1');
