from django.contrib import admin
from . models import Team,Score,Round,Player

# Register your models here.

admin.site.register(Team)
admin.site.register(Score)
admin.site.register(Round)
admin.site.register(Player)

