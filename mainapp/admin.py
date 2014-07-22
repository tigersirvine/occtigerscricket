from django.contrib import admin
from mainapp.models import Player , Team
from django.contrib.auth.models import Permission

class PermissionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Permission, PermissionAdmin)

class PlayerAdmin(admin.ModelAdmin):
    fields = ('firstname', 'lastname','dob','teamid')

admin.site.register(Player, PlayerAdmin)


class TeamAdmin(admin.ModelAdmin):
    fields = ('team_name', 'datejoined')

admin.site.register(Team, TeamAdmin)
