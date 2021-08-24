import webbrowser
#import pickledb
import pickle
import shelve
import random
from twilio.rest import Client
#day1=pickledb.load('amazonia',False)
#Note: Type day1 after the below input for the original url list used to test this program.
name=input("Welcome to URL Shortener v1.0.0! What's your name? This will be used to open your library of short urls in the future. ")
d=shelve.open(name)
#d=shelve.open('day1')
direction=input("Would you like to shorten a url (press a), revisit a shortened url (press b), list all shortened urls (press c), or delete a url from your database (press d)? Type quit to quit.\n")
while(direction!="quit"):
  if(direction=="a"):
    rannum=0
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    longurl=input("What's your long url? (Without https:// please)\n")
    beginning=longurl[:longurl.find("/")+1]
    shorturl=beginning
    dir2=input("Would you like to generate a random short URL (press a) or pick your own (press b)?\n")
    if(dir2=="a"):
        for i in range(0,5):
          rannum=random.randint(0,25)   
          shorturl+=alphabet[rannum]
        d[shorturl]=longurl
        print("Here is your short url: " + shorturl)
    elif(dir2=="b"):
        ending=input("What would you like to be the ending of your short url? For example, www.example.com/your-text-here.\n")
        shorturl+=ending
        d[shorturl]=longurl
        print("Here is your short url: " + shorturl)
    else:
        print("Sorry, I didn't understand. Try again?")
    #day1={shorturl:longurl}
    #outfile=open('hello',"wb")
    #pickle.dump(day1, outfile)
    #day1.set(shorturl,longurl)

  elif(direction=="b"):
    short=input("What was your shortened url?\n")
    #longurl=pickle.load(open('hello',"wb"))
    #longurl=day1.get(short)
    if short in d:
        longurl=d[short]
        webbrowser.open_new_tab(longurl)
    else:
        print("Sorry, that url isn't in your database.")
  elif(direction=="c"):
      print(name+"'s URL database:")
      mylist=list(d.keys())
      for i in mylist:
          print(i)
  elif(direction=="d"):
      delete=input("Which shortened url would you like to delete from the database?\n")
      if delete in d:
          del d[delete]
          print(delete + " has been deleted from your database.")
      else:
          print("Sorry, that url isn't in your database.\n")
  elif(direction=="e"):
    short=input("What was your shortened url?\n")
    #longurl=pickle.load(open('hello',"wb"))
    #longurl=day1.get(short)
    if short in d:
        longurl=d[short]
        client = Client()
        client.messages.create(to="",from_="",body="Here's your url: "+ longurl)
        print("Sent to your phone!")
    else:
        print("Sorry, that url isn't in your database.")

  else:
    print("Sorry, I didn't understand. Try again?\n")
  direction=input("Would you like to shorten a url (press a), revisit a shortened url (press b), list all shortened urls (press c), or delete a url from your database (press d)? Type quit to quit.\n")
print("Thanks for using URL Shortener v1.0.0!")