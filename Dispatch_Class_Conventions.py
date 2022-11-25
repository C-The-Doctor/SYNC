import sqlite3
from sqlite3 import Error
from flask import *

app=Flask(__name__)

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

    conn = create_connection("./backup.db")
def Record_Dispatch_Events(conn , DataUtility ):
    """
    Create a new Dispatch into the Dispatch table
    :param conn:
    :param Dispatch:
    :return: Dispatch id
    """

    conn = create_connection("./static/Databases/backup.db")

    sql = ''' INSERT INTO MessageLogs(MessageToken , MessageTitle , MessageBody , MessageStatus , MessageTimestamp , MessageAuthor , MessageAverts , MessageCount , DataProfile)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    with app.app_context():
        cur = conn.cursor()
        cur.execute(sql, DataUtility)
        conn.commit()
       
    return "Success"
   



def Retreive_Dispatch_Events(conn):
    """
    Query all Credential in the MessageLogsss table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM MessageLogs ")

    Credential = cur.fetchall()

   
    return Credential


def Retreive_Dipatch_Handles(conn):
    """
    Query MessageLogss by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT DataProfile FROM MessageLogs" )

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential 


def Query_Event_Existence(conn, MessageToken):
    """
    Query MessageLogsss by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT MessageToken FROM MessageLogs WHERE MessageToken=?", (MessageToken,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;

def Retreive_Parent_Dispatch(conn, MessageAuthor):
    """
    Query MessageLogsss by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = create_connection("./static/Databases/backup.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM MessageLogs WHERE MessageAuthor=?", (SecureID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;






def Delete_Dispatch_Events(conn, MessageToken):
    """
    Delete a MessageLogss by MessageLogss id
    :param conn:  Connection to the SQLite database
    :param id: id of the MessageLogss
    :return:
    """
    sql = 'DELETE FROM MessageLogs WHERE MessageToken = ?'
    cur = conn.cursor()
    cur.execute(sql, ( MessageToken ,))
    conn.commit()




conn = create_connection("./static/Databases/backup.db")

#Retreive_AllMessageDispatch(conn)


#Alpha =( "435435S9" , "Clyde Javis" , "Ahoya", "Test" ,"Test", "Test", "Test" , "Test", "Test")
#Record_Dispatch_Events(conn , Alpha )

#Remove_User_Profile(conn , "435435-XDK-9S90")

