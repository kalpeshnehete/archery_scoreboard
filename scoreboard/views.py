from django.shortcuts import render,redirect
from scoreboard.models import Score,Team,Round, Player
from .forms import TeamCreationForm,ScoreCreationForm,PlayerCreationForm

# Create your views here.

def home(request):
    r1score=Score.objects.filter(round_no='1')
    r2score=Score.objects.filter(round_no='2')
    r3score=Score.objects.filter(round_no='3')
    r4score=Score.objects.filter(round_no='4')
    r5score=Score.objects.filter(round_no='5')

    id=Score.objects.filter(team_name='1')
    #sc=Score.objects.filter(team_name='id')

    return render(request,'home.html',{'r1score':r1score,'r2score':r2score,'r3score':r3score,'r4score':r4score,'r5score':r5score})


def addteam(request):
    tdata=Team.objects.all()
    pdata=Player.objects.all()
    if request.method == 'POST':
        team_name = request.POST['team_name']
        t=Team.objects.create(team_name=team_name)
        t.save()
    return render(request, 'addteam.html',{'tdata':tdata,'pdata':pdata})

def addplayer(request):
    if request.method == 'POST':
        player_name = request.POST['player_name']
        p=Player.objects.create(player_name=player_name)
        p.save()
    return render(request,'addteam.html')

def addscore(request):
    form = ScoreCreationForm()
    print(request.POST)
    if request.method == "POST":
        form = ScoreCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,'addscore.html',{'form':form})




