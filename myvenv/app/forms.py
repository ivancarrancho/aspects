from django import forms
from django.contrib.auth.models import User
from .models import Team


class TeamForm(forms.Form):
    name = forms.CharField(label='Nombre del equipo')
    user = forms.ModelMultipleChoiceField(
        label='Integrantes',
        queryset=User.objects.all(),
    )

    def create_team(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        user_list = cleaned_data.get('user')
        team_obj = Team.objects.create(name=name)
        for user in user_list:
            team_obj.user.add(user)

        team_obj.save()

    def update_team(self, pk):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        user_list = cleaned_data.get('user')
        team_obj = Team.objects.filter(pk=pk)
        team_obj.update(name=name)
        team_obj = team_obj.first()
        team_obj.user.clear()

        for user in user_list:
            team_obj.user.add(user)

        team_obj.save()

    class Meta:
        model = User
        fields = ['name', 'user']
