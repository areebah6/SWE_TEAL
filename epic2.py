from tkinter import *
from tkinter import messagebox
import sys, re
#SUCCESS STORY
print("InCollege is the number one app in the country in helping students grow their network and land their dream jobs! Emily landed an internship right after her")
print("junior year of college at Amazon and has since recieved a full time offer! She credits InCollege for being a stepping stone for breaking into the industry") 
print("and believes all college students should register and take full advantage of the benefits InCollege has to offer!\n")
#VIDEO BUTTON AND MESSAGE
def button():
    window=Tk()
    def popup():
     messagebox.showinfo("Message", "Video is now playing")

    Button(window, text="Learn more about InCollege", command=popup).pack()

    window.mainloop()
button()

#ACCOUNTS DATABASE
class acc_db:
   accs=0 #will start by storing first entry at 0th index
   max_accs=5 #ensures only 5 accounts are stored
   sys_acc=[{}]#initializes empty list containing dictionary where we will store as the db

   #CHECKS IF ACCOUNT EXISTS
   def exists(self, username, password):
      for data in acc_db.sys_acc: 
         if 'user_name' in data and data['user_name']==username and 'password' in data and data['password']==password:
            return True
      return False
      
    
   #CHECKS IF USERNAME IS TAKEN
   def check_username(self, username):
        for data in acc_db.sys_acc: #data is the holder of each dictionary for that specific iteration
         if 'user_name' in data and data['user_name']==username: #checks first if key exists and if username typed in equals the key value. 
            return False
        return True
         

   #CHECK IF PASSWORD IS ACCEPTABLE
   def check_pass(self, password):
      if 8<=len(password)<=12:
         if any(char.isupper() for char in password): #built in python func
              if any(char.isdigit() for char in password): 
                  if re.search("[!@#$%^&*(),.?\":{}|<>]", password): #parsing string for special chars
                    return True
                  else:
                     print("Password must contain at least one special character.")
              else:
               print("Password must have at least one digit")
         else:
           print("Password must have at least one upper-case character.") 
      else: 
         print("Password must be between 8-12 characters.")
      return False
   
      
   #ADDS ACCOUNT ONCE USERNAME AND PASSWORD HAVE BEEN APPROVED.
   def add_acc(self, username, password, fname, lname):
    if acc_db.accs<acc_db.max_accs:
       acc_db.sys_acc[acc_db.accs]={
            'user_name':username,
            'password':password,
            'first_name':fname,
            'last_name':lname
         }
       acc_db.accs+=1 #increments so that next user can be added
    else:
       print("All permitted accounts have been created, please come back later")
        
   
   

    

   #FIND FRIENDS IN SYS
   def fr_sys(self, fname, lname):
      for data in acc_db.sys_acc: 
         if 'first_name' in data and data['first_name']==fname and 'last_name' in data and data['last_name']==lname: 
            return True
      return False
'''__________________________________________________________________________________________
   FOLLOWING FUNCTIONS ARE JUST FOR THE MENU OF WHAT USER WANTS TO DO WHEN THEY ENTER THE APP
   __________________________________________________________________________________________'''
#CALL WHEN USER WANTS TO LOG IN  
def login():
   ac_db=acc_db()
   while True:
      username=input("Enter your username: ")
      password=input("Enter your password: ")
      print("\n")
      check=ac_db.exists(username, password)
      if check:
         print("Login succesful")
         return True
      else:
         tryagain= input("Incorrect Username/Password. Please try again.(Y or N): ")
         print("\n")
         if tryagain=="Y" or tryagain=="y":
            login()
         elif tryagain=="N" or tryagain=="n":
            print("Returning to home screen")
            print("\n")
            return False
         else:
            print("Returning to home screen")
            print("\n")
            return False
  

#CALL WHEN USER WANTS TO CREATE ACC
def create():
   ac_db=acc_db()
   new_username=input("Create username: ")
   new_password=input("Enter your password (Must contain 8-12 characters, one uppercase letter, one number, and one special character): ")
   fname=input("Enter first name: ")
   lname=input("Enter your last name: ")
   print("\n")
   user_check=ac_db.check_username(new_username)
   user_password=ac_db.check_pass(new_password)
   if user_check and user_password:
      ac_db.add_acc(new_username, new_password, fname, lname)
      print("Account has successfully been created")
      print("\n")
      return True
   else:
       return False
   
def search_friend():
      ac_db=acc_db()
      frname=input("Type in first name (first letter must be capitalized): ")
      laname=input("Type in last name (first letter must be capitalized): ")
      print("\n")
      check_fr=ac_db.fr_sys(frname, laname)
      if check_fr:
         print("They are a part of the InCollege system")
         print("\n")
      else:
         print("They are not yet a part of the InCollege system")
         print("\n")
     

         
def main():
    option=input("MAIN MENU:\n-login\n-create an account\n-search for a friend\n(Please type L, C, or S for each corresponding option)\n Type B or E if you wish to go back or exit the program.: ")
    if option=="L" or option=="l":
       loggingin=login()
       if not loggingin:
          main()
    elif option=="C" or option=="c":
       creating=create()
       if not creating:
          again=input("Do you want to try creating an account again? (Y or N <- By typing in N, or any other character you will return back to the menu): ")
          if again=="Y" or again=="y":
              create()
              main()
          else:
             main()
    elif option=="S" or option=="s":
      search=search_friend()
      again_search=input("Do you want to search for any more friends (Y or N <- By typing in N, or any other character, you will return back to the menu): ")
      while again_search=="Y" or again_search=="y":
         search_friend()
         again_search=input("Do you want to search for any more friends (Y or N <- By typing in N, or any other character, you will return back to the menu): ")
      main()
    elif option=="B" or option=="b":
       main()
    elif option=="E" or option=="e":
      print("Thank you for visiting InCollege. Hope to see you back soon!")
      sys.exit()
    else:
      print("Invalid key. Please select from one of the options in the menu. Thank you.")
      main()      
if __name__ == "__main__":
   main()
         
      

        