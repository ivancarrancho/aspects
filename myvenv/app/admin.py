from django.contrib import admin
from .models import Team
from .models import Project
from .models import UserHistory
from django.contrib.auth.models import User


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
    )

    search_fields = ('name', 'id')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
    )

    search_fields = ('name', 'id')


@admin.register(UserHistory)
class UserHistoryAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'project',
        'get_teams',
    )

    search_fields = ('title', 'id')

    list_filter = ('project__name', 'project__team__name')

    def get_teams(self, obj):
        return obj.project.team

    get_teams.short_description = 'Equipos'


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'get_groups', 'username', 'is_active')
    list_filter = ('is_staff', 'is_superuser')

    def get_groups(self, obj):
        return list(obj.groups.values_list('name', flat=True))

    get_groups.short_description = 'Grupos de usuario'


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
