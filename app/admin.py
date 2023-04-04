from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Opponent)
admin.site.register(Tourney)
admin.site.register(Game)
admin.site.register(Result)
admin.site.register(Card)
admin.site.register(WorkoutDay)
admin.site.register(CauseSkip)