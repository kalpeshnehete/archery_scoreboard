from .models import Team,Player,Score
from django import forms


class TeamCreationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"

class PlayerCreationForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"

class ScoreCreationForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = '__all__'

