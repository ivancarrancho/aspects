from django.contrib import admin
from .models import Team
from .models import Project
from .models import UserHistory
from .models import User


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
        'planning_start_date',
        'planning_end_date',
        'real_start_date',
        'real_end_date',
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


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'charge',
        'salary',
        'income_date',
        'email',
        'is_active',
    ]
