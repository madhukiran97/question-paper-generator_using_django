from typing import List
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import subject,questions,objective_questions
from django.template import Context
import random
# Create your views here.
fquns=[]
def home(request):
    return render(request,'home.html')

def faculty(request):
    return render(request,'faculty.html') 
def addquestion(request):
    if request.method=="POST":
        course=request.POST['course']
        sem=request.POST['semister']
        qcode=request.POST['qcode']
        unit=request.POST['unit']
        type=request.POST['type']
        question=request.POST['question']
        qus=questions(course=course,sem=sem,unit=unit,type=type,question=question,sub_code=qcode)
        qus.save()
        messages.info(request,'question added') 
        return redirect('addquestion')
            
    else:
        return render(request,'addquestions.html')
def add_question(request):
    if request.method=="POST":
        course=request.POST['course']
        sem=request.POST['semister']
        qcode=request.POST['qcode']
        unit=request.POST['unit']
        question=request.POST['question']
        option1=request.POST['option1']
        option2=request.POST['option2']
        option3=request.POST['option3']
        option4=request.POST['option4']
        answer=request.POST['answer'] 
        qus=objective_questions(course=course,sem=sem,unit=unit,type=type,question=question,sub_code=qcode,option1=option1,option2=option2,option3=option3,option4=option4,answer=answer)
        qus.save()
        messages.info(request,'question added') 
        return redirect('add_question')
            
    else:
        return render(request,'add_questions.html')
def questionslist(request):
    if request.method=="POST":
        course=request.POST['course']
        sem=request.POST['semister']
        sub_code=request.POST['qcode']
        n=[1,2]
        r=[]
        k=2
        a=1
        u=[]
        quns=questions.objects.all()
        subs=subject.objects.all()
        
        for i in quns:
        
            if i.course == course:
                if i.sem == int(sem):
                    if i.sub_code == int(sub_code):
                        if i.type == 'short':
                    
                           l=str(i.question)
                           r.insert(0,l)

    
        draw=random.sample(r,k=10)
        draw.reverse()
        for j in quns:
        
            if j.course == course:
                if j.sem == int(sem):
                    if j.sub_code == int(sub_code):
                        if j.type == 'long':
                    
                           x=str(j.question)
                           u.insert(0,x)

    
        d=random.sample(u,k=10)
        d.reverse()
        print(d)
        return render(request,'qselect.html',{'course':course,'semister':int(sem),'qcode':int(sub_code),'list':List,'n':n,'k':k,'a':a,'r':draw,'d':d})
            
    else:
        return render(request,'questionslist.html')
  
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return render(request,'index.html',{'user':username})

        else:
            messages.info(request,'Invalid details') 
            return redirect('login')
    else:
        return render(request,'login.html')           
def signup(request):
    if request.method =='POST':
        UserName=request.POST['username']
        FirstName=request.POST['firstname']
        LastName=request.POST['lastname']
        EmailID=request.POST['email']
        Password=request.POST['password']
        Password1=request.POST['password1']
        if Password1 == Password:
            user=User.objects.create_user(username=UserName,first_name=FirstName,last_name=LastName,email=EmailID,password=Password)
            user.save()
            messages.info(request,'Account created') 
            return redirect('login')
        else:
            messages.info(request,'password not  matched')
            return redirect('signup')

    else:
        return render(request,'signup.html')
