from django.shortcuts import render,HttpResponse
from .models import Paper
from django.contrib.auth.models import User,auth
# Create your views here.
def index(request):
    data=Paper.objects.all()
    context={
        'questions':data
    }
    return render(request,'index.html',context)

def adminlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'admindashboard.html')
        else:
            return render(request,'adminlogin.html')
    return render(request, 'adminlogin.html')

def addquestion(request):
    if request.method=='POST':
        question=request.POST['question']
        option1=request.POST['option1']
        option2 = request.POST['option2']
        option3 = request.POST['option3']
        option4 = request.POST['option4']
        answer=request.POST['answer']
        data=Paper(question=question,option1=option1,option2=option2,option3=option3,option4=option4,answer=answer)
        data.save()
        message='Added Successfully'
        return render(request,'admindashboard.html',{'message':message})

