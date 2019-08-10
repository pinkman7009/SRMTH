from bs4 import BeautifulSoup

fileinput=open("Task.xml","r")

g=BeautifulSoup(fileinput,"xml")

pagename=input()
frame=input()

pn=g.find("Page",{"name":pagename})
f=pn.find("step",{"frame":frame})

string=f["pose"]
string=string+" "
k=""

c=len(string)

for i in range(c):
    if(string[i]!=' '):
        k=k+string[i]
    else:
        print(k)
        k=""
        
    

