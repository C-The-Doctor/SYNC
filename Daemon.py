from flask import Flask  , url_for , render_template , request , redirect 
from flask.views import View
from flask import g 
#from twilio.rest import Client 
import os , random , string 
from werkzeug.utils  import secure_filename
import time
import sqlite3
from sqlite3 import Error
import uuid 
import datetime
import TimeCop as Generate_Timestamp
# Databases Conventions 

import Student_Class_Conventions as Open_Student_Stream 
import First_Class_Conventions as Access_Reserved_Stream 
import Dispatch_Class_Conventions as Access_Dispatch_Stream
import Upload_Link_Conventions as Access_Secure_Upstream


app=Flask(__name__)


# Global Attributes & Containers
FounsationStorage = os.path.join(app.static_folder , "") + "/StudentsClassProfile" 
FirstClassStorage = os.path.join(app.static_folder , "") + "/FirstClassProfile" 
Message_Dispatch = os.path.join(app.static_folder , "") + "/Explorer/DispatchStreams" 
Property_Data_Scheme = os.path.join(app.static_folder , "") + "/Garage/OrgAssets/PropertyStore" 
TableStorage =os.path.join(app.static_folder , "") + "/Explorer/Table.txt" 
Unfinished_Data_Scheme = os.path.join(app.static_folder , "") + "/images/beef" 


# Liquid Configurations

app.config['PremierStorage']=FounsationStorage
app.config['SpecialUsers']=FirstClassStorage
app.config['DispatchStorage']=Message_Dispatch
app.config['Chronics']=TableStorage


#Get - User Data Location 
def DestinationUser(Username):
    Expanded_String =os.path.join(PremierStorage , Username )
    return str(Expanded_String)


def Generate_Secure_Token():
   Token_Hash = uuid.uuid4()
   return str(Token_Hash)


def Return_Twilio_Balance():
    client = Client()
    balance_data = client.api.v2010.balance.fetch()
    balance = float(balance_data.balance)
    currency = balance_data.currency

    AccountBalance = f'Your account has {balance:.2f}{currency} left.'  

# app name
@app.errorhandler(404)
  
# inbuilt function which takes error as parameter
def not_found(e):
  
# defining function
  return render_template("404.html")


# CLASS BASED VIEW DECLARATIONS 

class HomeView(View):


    def dispatch_request(self):
        Connection_Manager = Access_Dispatch_Stream.create_connection("./static/Databases/backup.db")
        User = "Uni-Identified"
        MessageData=Access_Dispatch_Stream.Retreive_Dispatch_Events(Connection_Manager)
        UploadData =Access_Secure_Upstream.Retreive_UploadLinks(Connection_Manager)
        return render_template('Dashboard.html', User=User , MessageData=MessageData , UploadData = UploadData)

class ContextUpload(View):
    methods = ["POST" ,"GET"]
    
    
    def dispatch_request(self):
        Connection_Manager = Access_Secure_Upstream.create_connection("./static/Databases/backup.db")
        User = "Uni-Identified"
        LinkTok = Generate_Secure_Token()
        LinkID = request.form.get("Title")
        LinkTarget = request.form.get("Target")
        LinkLevel = request.form.get("Level")
        LinkPeriod = request.form.get("Period")
        LinkSpan = request.form.get("Idle")
        SessionCount = str("0")
        ExpectedCount = str("Calculating")
        LinkStatus = str("Active")
        LinkAdmin = str("g.UserID")
        LinkProfile = str("Generating")
        Stream_Chunks = []
        
        
        
        Stream_Chunks.append(LinkTok)
        Stream_Chunks.append(LinkID)
        Stream_Chunks.append(LinkTarget)
        Stream_Chunks.append(LinkLevel)
        Stream_Chunks.append(LinkPeriod)
        Stream_Chunks.append(LinkSpan)
        Stream_Chunks.append(SessionCount)
        Stream_Chunks.append(ExpectedCount)
        Stream_Chunks.append(LinkStatus)
        Stream_Chunks.append(LinkAdmin)
        Stream_Chunks.append(LinkProfile)
        Access_Secure_Upstream.Create_UploadLinks(Connection_Manager, Stream_Chunks)
        
        
        return redirect(url_for("Root"))



class Explorer(View):

    def dispatch_request(self):
        User = "Uni-Identified"
        return render_template('Explorer.html', User=User)



class Digitise(View):

    def dispatch_request(self):
        User = "Uni-Identified"
        return render_template('Digitise.html', User=User)


class Departmental(View):

    def dispatch_request(self):
        User = "Uni-Identified"
        return render_template('Departments.html', User=User)
        
        

class SinkStore(View):

    def dispatch_request(self):
        Connection_Manager = Access_Dispatch_Stream.create_connection("./static/Databases/backup.db")
        MessageData=Access_Dispatch_Stream.Retreive_Dispatch_Events(Connection_Manager)
        User = "Uni-Identified"
        return render_template('SinkProfiles.html', User=User , MessageData=MessageData)
        
        
        
class AllUserProfiles(View):

    def dispatch_request(self):
        User = "Uni-Identified"
        return render_template('UserProfile.html')


class SinkView(View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        Connection_Manager = Open_Student_Stream.create_connection("./static/Databases/backup.db")
        if request.method == 'POST':
            HalfIntro = request.form
            FirstChunk = str(request.form.get("Firstname"))
            SecondChunk =str(request.form.get("Secondname"))
            UserStr =  FirstChunk  + SecondChunk
            file = request.files['Profile']
            if file:
                filename = secure_filename( UserStr + ".jpg")
                Basepath=os.path.join(app.config['SpecialUsers'] , UserStr)
                os.mkdir(Basepath)
                file.save(os.path.join(app.config['SpecialUsers'] , UserStr , filename))
                Profile_Location =str(os.path.join(app.config['SpecialUsers'] , UserStr  , filename))
                # Pushing Our Usernamer To Stack 
                # Saving In Global Session Environment ( g )  Is Not Encouraged And
                # Will Be Removed In Post-Releases 
                # Were Basically Shooting Our Self In The Leg Here 
                # Cool Thing Is Only The TokeID can be  Traced G Session Varriable 

                g.UserID=UserStr
                TransitCredential = list(HalfIntro.values())
                TransitCredential.append(Profile_Location)
                Access_Reserved_Stream.Create_UserProfile(Connection_Manager , TransitCredential)
            return redirect(url_for('Auth'))
        else:
            User = "Uni-Identified"
            return render_template('CreateSinkAccount.html', User=User)


class AuthView(View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        Connection_Manager = Open_Student_Stream.create_connection("./backup.db")
        Context_Keys = ('Username' , 'Password')
        Context_Value = "Unknown"
        if request.method == 'POST':
                # - Action Zone
                UserDict = {}
                UserDict = request.form
                for k in UserDict.values():
                    print(k)
                # Database Profiling
                UserID = request.form.get("UserString")
               
                CryptoIdentifier = request.form.get("CryptoString")
                Security_Captcha = Open_Student_Stream.Query_User_Existence(Connection_Manager, UserID)
                Crypto_Captcha = Open_Student_Stream.Query_CryptoHash_Existence(Connection_Manager, CryptoIdentifier)
                print(Security_Captcha)
                if (Security_Captcha != None ):
                    if(Crypto_Captcha != None):
                        return redirect(url_for("Root" , UserID  = UserID ))
                    else:
                        return redirect("/Auth")
                else:
                    users = " jsdjsd "
                    return                    redirect(url_for('Auth'), UserID=UserID )
        else:
                return render_template('AuthController.html' )




class CreatePremierAccount(View):
   methods = ['GET', 'POST']
   def dispatch_request(self):
    print(Generate_Secure_Token())
    Connection_Manager = Open_Student_Stream.create_connection("./static/Databases/backup.db")
    if request.method == 'POST':
        HalfIntro = request.form
        UserString = request.form.get("AdmissionNo")
        file = request.files['Profilia']
        if file:
            filename = secure_filename(file.filename)
            Basepath=os.path.join(app.config['PremierStorage'] , UserString)
            os.mkdir(Basepath)
            file.save(os.path.join(app.config['PremierStorage'] , UserString , filename))
            Profile_Location =str(os.path.join(app.config['PremierStorage'] , UserString  , filename))
            # Pushing Our Usernamer To Stack 
            # Saving In Global Session Environment ( g )  Is Not Encouraged And
            # Will Be Removed In Post-Releases 
            # Were Basically Shooting Our Self In The Leg Here 
            # Cool Thing Is Only The TokeID can be  Traced G Session Varriable 

            g.UserID=UserString
            TransitCredential = list(HalfIntro.values())
            TransitCredential.append(Profile_Location)
            Open_Student_Stream.Create_UserProfile(Connection_Manager , TransitCredential)
        return redirect(url_for('Auth'), g.UserID == g.UserID )
    else:
        return render_template('CreatePremiumAccount.html' , Generate_Secure_Token=Generate_Secure_Token)





class DispatchEvents(View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        Connection_Manager = Access_Dispatch_Stream.create_connection("./static/Databases/backup.db")
        if request.method == 'POST':
            DispatchData = request.form
            for d in DispatchData.values():
                print(d)
            # Filters For The Database Entry 
            # Independent Uploads To The Database Forced US To Have 2 Upload Chunks 
            #A More Efficient Function Will Be Used In The Future
            MsgToken = Generate_Secure_Token()
            MsgTitle = request.form.get('Title')
            MsgBody  = request.form.get('Mess')
            MsgStatus = str("In-Progress")
            MsgTimestamp = Generate_Timestamp.TimePolice()
            MsgOwner = request.form.get("Author")
            MsgAvertions = request.form.get("Group")
            MsgTotal =  str("5445")
            Attachments = "Available"
            DispatchQuery  =  []
            DispatchQuery.append(MsgToken)
            DispatchQuery.append(MsgTitle)
            DispatchQuery.append(MsgBody)
            DispatchQuery.append(MsgStatus)
            DispatchQuery.append(MsgTimestamp)
            DispatchQuery.append(MsgOwner)
            DispatchQuery.append(MsgAvertions)
            DispatchQuery.append(MsgTotal)
            DispatchQuery.append(Attachments)

            for s in DispatchQuery:
                print(s)
            
            Access_Dispatch_Stream.Record_Dispatch_Events(Connection_Manager , DispatchQuery )

            # EOF --> Filter Police  
            DispatchToken = str(MsgToken)
            file = request.files['Attachments']
            if file:
                filename = secure_filename(file.filename)
                DispatchLocation=os.path.join(app.config['DispatchStorage'] , DispatchToken)
                os.mkdir(DispatchLocation)
                file.save(os.path.join(app.config['DispatchStorage'] , DispatchToken , filename))
                Data_Location =str(os.path.join(app.config['DispatchStorage'] , DispatchToken  , filename))
                # Pushing Our Usernamer To Stack 
                # Saving In Global Session Environment ( g )  Is Not Encouraged And
                # Will Be Removed In Post-Releases 
                # Were Basically Shooting Our Self In The Leg Here 
                # Cool Thing Is Only The TokeID can be  Traced G Session Varriable 
                
                DispatchUtility = list(DispatchData.values())

                DispatchUtility.append(Data_Location)
            return redirect(url_for("Root"))
        else:
            User = "Uni-Identified"
        return render_template('DispatchEvents.html', Generate_Secure_Token=Generate_Secure_Token)













app.add_url_rule('/Auth/', view_func=AuthView.as_view('Auth'))
app.add_url_rule('/', view_func=HomeView.as_view('Root'))
app.add_url_rule('/CreateAccount/', view_func=CreatePremierAccount.as_view('CreateAccount'))
app.add_url_rule('/Dispatch/', view_func=DispatchEvents.as_view('Dispatch'))
app.add_url_rule('/CreateSink/', view_func=SinkView.as_view('CreateSink'))
#Returning Explorer Container 
app.add_url_rule('/Explorer/', view_func=Explorer.as_view('Explorer'))
app.add_url_rule('/Departments/', view_func=Departmental.as_view('Departments'))
app.add_url_rule('/AllSinks/', view_func=SinkStore.as_view('AllSinks'))
app.add_url_rule('/Digitise/', view_func=Digitise.as_view('Digitise'))
app.add_url_rule('/UserProfiles/', view_func=AllUserProfiles.as_view('UserProfiles'))
# Manage Uploaded Files Here 
app.add_url_rule('/CreateUploadLink/', view_func=ContextUpload.as_view('CreateUploadLink'))



# Main Execution Block 
# Rendering With Openssl : ADHOC 
# Running This Script Requires The Following 
         # Openssl Binary Value Should Be Set To Zero 
         # Xml Parser :: Expat Should be of version > 2 Not Lower
         # For Systems With Low Expat Versions : 
               #Serialization Is therefore defaulted to Json 

if __name__=='__main__':

   # Database Creation Section 
  # DB_InitializationWizard("/static/Databases/RentLord_Databases.db")
   
   app.run("0.0.0.0" , debug="False" )
