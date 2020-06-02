from django.shortcuts import render,redirect
from .models import Meet

# Create your views here.
def add(request):
    if request.method == "POST":
        subject = request.POST['subject']
        meetingWith = request.POST['with']
        date = request.POST['date']
        time = request.POST['time']
        place = request.POST['place']
        userId = request.user
        print(userId.id)
        print(place)
        print(time)
        print(date)
        print(subject)
       

        meetingInfo = Meet(subject=subject,meetingWith=meetingWith,date =date,time=time,place=place,userId=userId.id)
        meetingInfo.save()
        return render(request,"add.html")


    else:
        return render(request,"add.html")
def seeRun(request):
    if request.method == "POST":
        meetingId = request.POST['meetingId']
        summery = request.POST['summery']
        m = Meet.objects.filter(id=meetingId)
        m.update(done=True,summery=summery)
        return render(request,"seeRun.html")  
    else:
        if request.user.is_authenticated:
            meetings = Meet.objects.filter(userId=request.user.id).filter(done=False)
            return render(request,"seeRun.html",{'meetings':meetings})
        else:
            return redirect("/")

def seeDone(request):
    if request.user.is_authenticated:

        meetings = Meet.objects.filter(userId=request.user.id).filter(done=True)
        return render(request,"seeDone.html",{'meetings':meetings})
    else:
        return redirect("/")


    