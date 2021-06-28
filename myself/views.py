from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
context=[ 
{'name':'Jakshi','place':['Jamnagr','Goa']},
{'name':'Sakshi','place':['Mumbai','Paris']},
{'name':'Vidhi','place':['Dubai','jaipur']},
{'name':'Nandini','place':['Abu','Goa']},
{'name':'Senhal','place':['Mumbai','Landon']},
{'name':'Jainam','place':['Bhuj','UK']},
{'name':'Vrttik','place':['Abu','US']},
{'name':'Jayesh','place':['baroda','Morbi']}
]

result=[
{'name':'Jakshi','enroll':101,'marks':[80,90,84,96,88]},
{'name':'Sakshi','enroll':102,'marks':[88,80,70,98,74]},
{'name':'Vidhi','enroll':103,'marks':[70,60,75,60,89]},
{'name':'Nandini','enroll':104,'marks':[68,85,75,86,80]},
{'name':'Senhal','enroll':105,'marks':[75,89,87,74,50]}
]

log=[
{'username':'jakshi','password':'jakshi@123'},
{'username':'sakshi','password':'sakshi@123'},
{'username':'vidhi','password':'vidhi@123'},
{'username':'nandini','password':'nandini@123'}
]

def home(request):
	#return HttpResponse('<center> welcome to my website</center> myself jakshi shah ')	
	return render(request,'home.html',context[0])

def login(request):
	#return HttpResponse('<center> welcome to my website</center> myself jakshi shah ')
	#return render(request,'login.html',context[1])
	name = request.GET['username']
	password = request.GET['password'] 
	for d in log:
		if d['username']==name and d['password']==password:
			return render(request,'marksheet.html',d)

	return render(request,'login.html')
def loginpage(request):
	return render(request,'login.html')

def music(request):
	return render(request,'music.html',context[2])

def movie(request):
	return render(request,'movie.html',context[3])

def place(request):
	return render(request,'place.html',context[4])

def book(request):
	return render(request,'book.html',context[5])

def hobbies(request):
	return render(request,'hobbies.html',context[6])

def friends(request):
	return render(request,'friends.html',context[7])

def marksheet(request):
	return render(request,'marksheet.html')

def showmarksheet(request):
	rollno = int(request.GET['enroll'])
	for d in result:
		if d['enroll']==rollno:
			return render(request,'showmarksheet.html',d)

	return render(request,'home.html')
