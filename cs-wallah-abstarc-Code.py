from abc import ABC, abstractmethod

class CloudDrive(ABC):

  #concreate method
  def display(self):
    print("show data")

  @abstractmethod
  def upload(self, file_name):
    pass


class GoogleDrive(CloudDrive):
  def upload(self, file_name):
     return "upload" + file_name + "To my drive"

class GitHubRepo(CloudDrive):
  def upload(self, file_name):
    return "Pushed" + file_name + "to code repo"


d1 = GoogleDrive()
d2 = GitHubRepo()

print(d1.upload("notes.pdf"))
print(d2.upload("app.py"))

d1.display()
d2.display()




from abc import ABC , abstractmethod

class BankApp(ABC):
  def database(self):
    print("conneted to db")

  @abstractmethod
  def security(self):
    pass


  @abstractmethod
  def display(self):
    pass




class MobileApp(BankApp):
  def mobile_login(self):
    print("login from mobile")

  def security(self):
     print("db connecyed login from mobile")



#this is objects creations


obj = MobileApp()
obj.mobile_login()
obj.database()



#this is another class

class WebApp(BankApp):
  def web_login(self):
    print("login from web")


  def security(self):
     print("db connecyed login from web app")


  def display(self):
     print("display")


#this is objects creations

obj2= WebApp()
obj2.web_login()
obj2.display()
obj2.database()
