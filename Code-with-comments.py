# VVI POINT 1: Abstraction shows "what action happens" (upload) and hides "how 
servers do it".
# VVI POINT 2: ABC + @abstractmethod sets a strict rule — child classes MUST 
define upload().
# VVI POINT 3: You cannot instantiate CloudDrive() directly — it is a 
blueprint/contract, not a real drive.
# VVI POINT 4: Real-life CS use — Storage drivers/APIs where callers just say 
"save/upload" without
#              
caring about disk blocks, network packets, or server layout.
# VVI POINT 5: Lecture hook (beginner to pro) — Beginners see a simple rule; CS 
majors see clean API design.
from abc import ABC, abstractmethod   # Import ABC (base class) and abstractmethod 
decorator from Python's abc module
class CloudDrive(ABC):              
(acts as a strict blueprint)
@abstractmethod                 
its own upload() method
def upload(self, file_name):    
# Declare the required action name and 
parameter without writing internal logic
pass                        
not execute directly
class GoogleDrive(CloudDrive):      
contract
# Real-life use: Personal & team docs/files synced to cloud folders
def upload(self, file_name):    
Drive
class GitHubRepo(CloudDrive):       
# Define CloudDrive as an Abstract Base Class 
# Decorator forcing every child class to write 
# Placeholder body because abstract methods do 
# Child class 1: Inherits the CloudDrive 
# Fulfills the @abstractmethod rule for Google 
return "Uploaded " + file_name + " to My Drive"  # Returns Google Drive's 
specific upload behavior
# Child class 2: Inherits the same CloudDrive 
contract
# Real-life use: Saving code versions and commits for developers
def upload(self, file_name):    
# Fulfills the @abstractmethod rule for GitHub
return "Pushed " + file_name + " to code repository"  # Returns GitHub's 
specific upload behavior
# Copy, paste, and run in Google Colab
d1 = GoogleDrive()                  
# Create an object of concrete child class 
GoogleDrive (Allowed!)
d2 = GitHubRepo()                   
GitHubRepo (Allowed!)
print(d1.upload("notes.pdf"))       
internals
print(d2.upload("app.py"))          
commit internals
# Create an object of concrete child class 
# Calls GoogleDrive's upload() -> hides server 
# Calls GitHubRepo's upload() -> hides git 


#THIS IS SECOND CODE WITH COMMENTS FOR BETTER UNDERSTANDING


from abc import ABC, abstractmethod   # Import abstraction tools from Python's 
standard library
class BankApp(ABC):                 
# Abstract parent class defining the core 
banking blueprint
# Concrete method: shared by all apps; child classes do NOT need to rewrite 
this
def database(self):
print("connected to database")
# Abstract method 1: every child class MUST implement its own security check
@abstractmethod
def security(self):
pass
# Abstract method 2: every child class MUST implement its own screen display
@abstractmethod
def display(self):
pass
class MobileApp(BankApp):             
def security(self):             
# Implements required abstract method #1
print("login from mobile app")
# If any @abstractmethod is missing in a child class, Python blocks object 
creation!
def display(self):              
class WebApp(BankApp):                
Application
def security(self):             
web browsers
print("login from web browser with 2FA")
def display(self):              
desktop screens
print("display works well on web")
both implemented
mobile.database()                   
mobile.security()                   
mobile.display()                    
# Child class 1: Mobile Banking Application
# Implements required abstract method #2
print("display works well on mobile")
# Child class 2: Browser-Based Web Banking 
# Implements required abstract method #1 for 
# Implements required abstract method #2 for 
# Testing both MobileApp and WebApp objects
mobile = MobileApp()                
# Works because security() and display() are 
# Inherited concrete method from BankApp
# Mobile-specific security implementation
# Mobile-specific display implementation
web = WebApp()                      
both implemented
web.database()                      
web.security()                      
web.display()                       
# Works because security() and display() are 
# Inherited concrete method from BankApp
# Web-specific security implementation
# Web-specific display implementation

