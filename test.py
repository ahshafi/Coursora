import cx_Oracle
import config as cfg

with cx_Oracle.connect(cfg.username,
                            cfg.password,
                            cfg.dsn,
                            encoding=cfg.encoding) as connection:
            # create a new cursor
            with connection.cursor() as cursor:
                # create a new variable to hold the value of the
                # OUT parameter
                tout = cursor.var(str)
                # call the stored procedure
                cursor.callproc('TEST_PROC',
                                [451, tout])
                print(tout.getvalue())