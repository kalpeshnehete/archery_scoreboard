from django.shortcuts import render,redirect
from scoreboard.models import Score,Team,Round, Player
from .forms import TeamCreationForm,ScoreCreationForm,PlayerCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.sessions.models import Session

# Create your views here.

def home(request):
    r1score=Score.objects.filter(round_no='1')
    r2score=Score.objects.filter(round_no='2')
    r3score=Score.objects.filter(round_no='3')
    r4score=Score.objects.filter(round_no='4')
    r5score=Score.objects.filter(round_no='5')
    t1s=Score.objects.all()
    m=[]
    for i in t1s:
        h=int(i.playerscore)
        m.append(h)
    mscore=(sum(m))
    t2s=Score.objects.filter(team_name='2')
    n=[]
    for k in t2s:
        o=int(k.playerscore)
        n.append(o)
    nscore=(sum(n))
    if m > n:
        tw="Team 1 won"
    elif m<n:
        tw="Team 2 won"
    return render(request,'home.html',{'r1score':r1score,'r2score':r2score,'r3score':r3score,'r4score':r4score,'r5score':r5score,'mscore':mscore,'nscore':nscore,'tw':tw})


def addteam(request):
    if request.session.has_key('is_logged'):
        tdata=Team.objects.all()
        if request.method == 'POST':
            team_name = request.POST['team_name']
            t=Team.objects.create(team_name=team_name)
            t.save()
        return render(request, 'addteam.html',{'tdata':tdata})
    return redirect('/login/')



def addplayer(request):
    if request.session.has_key('is_logged'):
        pdata=Player.objects.all()
        form = PlayerCreationForm()
        print(request.POST)
        if request.method == "POST":
            form = PlayerCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/")
        return render(request,'addplayer.html',{'form':form,'pdata':pdata})
    return redirect('/login/')


def addscore(request):
    if request.session.has_key('is_logged'):
        form = ScoreCreationForm()
        print(request.POST)
        if request.method == "POST":
           form = ScoreCreationForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect("/")
        return render(request,'addscore.html',{'form':form})
    return redirect('/login/')


def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        password=request.POST['password']
        x=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password)
        x.save()
        return redirect('/login/')
    return render(request,'signup.html')

def login(request):
    if request.session.has_key('is_logged'):
        return redirect('/')
    if request.method == 'POST':
        username1=request.POST['username']
        password1=request.POST['password']
        user=auth.authenticate(username=username1,password=password1)
        request.session['is_logged']=request.POST['username']
        if user is None:
            return redirect('/login/')
        else:
            return redirect('/')
    return render(request,'login.html')

def logout(request):
    del request.session['is_logged']
    return redirect('/login/')






