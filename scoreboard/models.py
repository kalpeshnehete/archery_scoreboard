from django.db import models

# Create your models here.
class Round(models.Model):
    ROUND = (
        ('R1', 'Round 1'),
        ('R2', 'Round 2'),
        ('R3', 'Round 3'),
        ('R4', 'Round 4'),
        ('R5', 'Round 5'),
    )
    round_no=models.CharField(max_length=2,choices=ROUND)

    def __str__(self):
       return f' {self.round_no} '

class Team(models.Model):
    team_name=models.CharField(max_length=10,blank=False,null=False)
    #player1=models.TextField(max_length=10,blank=False)
    #player2=models.TextField(max_length=10,blank=False)
    def __str__(self):
        return self.team_name

class Player(models.Model):
    player_name=models.TextField(max_length=10,blank=False,null=False)

    def __str__(self):
        return self.player_name

class Score(models.Model):
    SCORE_GRADES = (
                   ('5', 'A'),
                   ('4', 'B'),
                   ('3', 'C'),
                   ('2', 'D'),
                   ('1', 'E'),
                   ('0', 'F'),
    )
    round_no = models.ForeignKey(Round, on_delete=models.CASCADE)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    player_name = models.ForeignKey(Player, on_delete=models.CASCADE)
    playerscore=models.CharField(max_length=1,choices=SCORE_GRADES)

    def __str__(self):
        return f' {self.playerscore} '
