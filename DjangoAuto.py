import os,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

WebsiteName= input("Enter The Website's Name :")
Name = input("Enter Owner's Name :")
u_count = int(input("Enter Number of URL's :"))

def Main():
	os.system('cls')
	pname = input("Enter Project Name :")
	appname = input("Enter App Name :")
	create(pname)
	migrate()
	appc(appname,pname)
	runs(pname)

def create(pname):
	os.system('django-admin startproject '+pname)
	print("[+] Project created !!")
	os.chdir(r"D:\\Automation\\"+pname)
	os.system('ls')
	
def migrate():
	os.system('python manage.py makemigrations')
	os.system('python manage.py migrate')

def runs(pname):
	os.chdir(r"D:\\Automation\\"+pname)
	os.system('python manage.py runserver')

def appc(appname,pname):
	os.system('django-admin startapp '+appname)
	print("[+] Project created !!")
	purl(pname,appname)
	for i in range(u_count):
		os.chdir(r"D:\\Automation\\"+pname+"\\"+appname)
		createURL()

def purl(pname,appname):
	os.chdir(pname)
	f = open("settings.py","a+")
	f.write("INSTALLED_APPS.append('"+appname+"')")
	f.close()
	f = open("urls.py","a+")
	f.write("from django.conf.urls import include\nfrom django.conf import settings\n\nurlpatterns = [path('', include('"+appname+".urls')),]")
	f.close()

def createURL():
	n = input("Enter URL Name :")
	f = open("urls.py","a+")
	if n==" ":
		f.write("from django.urls import path\nfrom . import views\n\nurlpatterns = [path('', views.index,name='index')]")
	else:
		f.write("\nurlpatterns += [path('"+n+"/', views."+n+",name='"+n+"')]")
	f.close()
	print("[+] URL Created ")
	createView(n)

def createView(n):
	f = open("views.py","a+")
	if n==" ":
		f.write("def index(request):\n\treturn render(request,'index.html')")
	else:
		f.write("\n\ndef "+n+"(request):\n\treturn render(request,'"+n+".html')")
	f.close()
	print("[+] View Created")
	createhtml(n)


def createhtml(n):
	if n==" ":
		os.mkdir("templates")
	os.chdir("templates")
	if n==" ":
		f = open("index.html","w+")
		n="Home"
	else:
		f=open(n+".html","w+")
	f.write("<html>\n<head>\n<title>"+WebsiteName+"|"+n+"</title>\n</head>\n<body>\n<center><h1>Hello "+Name+" !!  Automation Completed</h1>\n<h2>This is "+n+" Page</h2></center>\n</body>\n</html>")
	f.close()
	print("[+] "+n+" HTML Created")


if __name__ == '__main__':       
    Main()