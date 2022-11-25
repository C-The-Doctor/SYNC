import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def Database_Init_Override(Masterpath):
    Storage_UNIT = Masterpath

    SINK_DATABASE_STUDENT_CONSTRUCTOR = """ CREATE TABLE IF NOT EXISTS StudentClassProfiles(
                                        AdmissionNo text NOT NULL  ,
                                        FullName text NOT NULL,
                                        EmailAddress text NOT NULL ,
                                        Gender text NOT NULL ,
                                        Course text NOT NULL ,
                                        Level text NOT NULL ,
                                        Stage text NOT NULL ,
                                        PhoneNumber text NOT NULL ,
                                        AlternativeNumber text NOT NULL ,
                                        UserID text NOT NULL ,
                                        SecureID text NOT NULL ,
                                        
Status text NOT NULL ,                                        
                                        ProfilePath text NOT NULL
                                    ); """

    SINK_DATABASE_FIRSTCLASS_CONSTRUCTOR = """CREATE TABLE IF NOT EXISTS  FirstClassProfiles(
                                
                                        FirstName text NOT NULL,
                                        LastName text NOT NULL ,
                                        EmailAddress text NOT NULL ,
                                        Gender text NOT NULL ,
                                        Designation text NOT NULL ,
                                        Department text NOT NULL ,
                                        Course text NOT NULL ,
                                        PhoneNumber text NOT NULL ,
                                        AlternativeNumber text NOT NULL ,
                                        UserID text NOT NULL ,
                                        SecureID text NOT NULL ,
                                        ProfilePath text NOT NULL

                                    );"""



    SINK_DATABASE_NEWS_CONSTRUCTOR = """CREATE TABLE IF NOT EXISTS NewUpdates (
            
                                        UpdateID text NOT NULL,
                                      UpdateTitle text NOT NULL ,
                                         UpdateBody text NOT NULL,
                                        UpdateAuthor text  NOT NULL,
                                        TargetContext text NOT NULL,
                                        UpdateData text NOT NULL,
                                        Timestamp text NOT NULL,
                                        Category text NOT NULL,
                                                                             ProfilePath  text NOT NULL
                                    );"""



    SINK_DATABASE_DEPARTMENTS_CONSTRUCTOR = """CREATE TABLE IF NOT EXISTS DepartmentsProfile (
                                        DepartmentCode text NOT NULL  PRIMARY KEY,
                                        DepartmentName text NOT NULL,
                                                     DepartmentAdmin text  NOT NULL
                                       

                                    
                                    
                                    );"""



    SINK_DATABASE_COURSAL_CONSTRUCTOR    = """CREATE TABLE IF NOT EXISTS CoursesProfile (
                                        CourseCode text NOT NULL PRIMARY KEY,
                                        CourseName text NOT NULL,
                                        DepartmentCode text NOT NULL ,
                                        Level text NOT NULL,
                                        Iterations text NOT NULL,
                                        Category text NOT NULL
                                        
                                    );"""



   
                                 


    SINK_DATABASE_MESSAGELOGS_CONSTRUCTOR    = """CREATE TABLE IF NOT EXISTS MessageLogs (
                                        MessageToken text NOT NULL PRIMARY KEY,
                                        MessageTitle text NOT NULL,
                                        MessageBody  text NOT NULL ,
                                        MessageStatus text NOT NULL,
                                        MessageTimestamp text NOT NULL,
                                        MessageAuthor text NOT NULL,
                                        MessageAverts text NOT NULL,
                                        MessageCount text NOT NULL ,
                                        DataProfile text NOT NULL
                                
                                    );"""


    SINK_DATABASE_UPLOADLINKS_CONSTRUCTOR    = """CREATE TABLE IF NOT EXISTS UploadLinks (
                                        LinkToken text NOT NULL PRIMARY KEY,
                                        LinkID text NOT NULL,
                                        LinkTarget  text NOT NULL ,
                                        LinkLevel  text NOT NULL ,
                                 
LinkPeriod  text NOT NULL ,       
                                        LinkLifeSpan text NOT NULL,
                                        SessionLoadCount text NOT NULL,
                                        ExpectedLoadCount text NOT NULL,
                                        LinkStatus text NOT NULL,
                                        LinkAdmin text NOT NULL,
                                        DataProfile text NOT NULL
                                        
                                    );"""


    SINK_DATABASE_EXPLORER_CONSTRUCTOR    = """CREATE TABLE IF NOT EXISTS Explorer (
                                        FileToken text NOT NULL PRIMARY KEY,
                                        FileName text NOT NULL,
                                        FileType  text NOT NULL ,
                                        FileStamp text NOT NULL,
                                        FileAdmin text NOT NULL,
                                        FilePath text NOT NULL,
                                        FileCount text NOT NULL,
                                                                        TimeStamp text NOT NULL,
                                        FileSize text NOT NULL
                                    );"""




    # create a database connection
    conn = create_connection(Storage_UNIT)
# create tables
    if conn is not None:
        # create projects table
        create_table(conn, SINK_DATABASE_STUDENT_CONSTRUCTOR)

        # create tasks table
        create_table(conn,  SINK_DATABASE_FIRSTCLASS_CONSTRUCTOR)

        # create tasks table
        create_table(conn, SINK_DATABASE_NEWS_CONSTRUCTOR)

        # create tasks table
        create_table(conn,  SINK_DATABASE_DEPARTMENTS_CONSTRUCTOR  )

        # create tasks table
        create_table(conn, SINK_DATABASE_COURSAL_CONSTRUCTOR )

        # create tasks table
        create_table(conn, SINK_DATABASE_MESSAGELOGS_CONSTRUCTOR )

         # create tasks table
        create_table(conn, SINK_DATABASE_UPLOADLINKS_CONSTRUCTOR )

         # create tasks table
        create_table(conn, SINK_DATABASE_EXPLORER_CONSTRUCTOR )



        
    else:
        print("Error! cannot create the database connection.")

Database_Init_Override("./static/Databases/backup.db")
