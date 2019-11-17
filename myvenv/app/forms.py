from django import forms
from .models import User
from .models import UserHistory
from .models import Team
from .models import Project


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


class ProjectForm(forms.Form):
    name = forms.CharField(label='Nombre del proyecto')
    team = forms.ModelMultipleChoiceField(
        label='Equipos',
        queryset=Team.objects.all(),
    )

    manager_name = forms.CharField(label='Nombre del gerente')
    manager_code = forms.CharField(label='Código del gerente')
    planning_start_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'datepicker'}),
        label='Fecha planeada de inicio'
    )
    planning_end_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'datepicker'}),
        label='Fecha planeada de finalización'
    )
    planning_end_date.widget.attrs['class'] = 'datepicker'
    real_start_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'datepicker'}),
        label='Fecha real de inicio'
    )
    real_end_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'datepicker'}),
        label='Fecha real de finalización'
    )

    def create_project(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        team = cleaned_data.get('team')
        manager_name = cleaned_data.get('manager_name')
        manager_code = cleaned_data.get('manager_code')
        planning_start_date = cleaned_data.get(
            'planning_start_date'
        )
        planning_end_date = cleaned_data.get('planning_end_date')
        real_start_date = cleaned_data.get('real_start_date')
        real_end_date = cleaned_data.get('real_end_date')

        Project.objects.create(
            name=name,
            team=team.first(),
            manager_name=manager_name,
            manager_code=manager_code,
            planning_start_date=planning_start_date,
            planning_end_date=planning_end_date,
            real_start_date=real_start_date,
            real_end_date=real_end_date,
        )

    def update_project(self, pk):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        team = cleaned_data.get('team')
        manager_name = cleaned_data.get('manager_name')
        manager_code = cleaned_data.get('manager_code')
        planning_start_date = cleaned_data.get('planning_start_date')
        planning_end_date = cleaned_data.get('planning_end_date')
        real_start_date = cleaned_data.get('real_start_date')
        real_end_date = cleaned_data.get('real_end_date')

        project_obj = Project.objects.filter(pk=pk)
        project_obj.update(
            name=name,
            team=team.first(),
            manager_name=manager_name,
            manager_code=manager_code,
            planning_start_date=planning_start_date,
            planning_end_date=planning_end_date,
            real_start_date=real_start_date,
            real_end_date=real_end_date,
        )

    class Meta:
        model = User
        fields = [
            'name',
            'team',
            'manager_name',
            'manager_code',
            'planning_start_date',
            'planning_end_date',
            'real_start_date',
            'real_end_date',
        ]


class UserForm(forms.Form):
    username = forms.CharField(label='Nombre')
    charge = forms.CharField(label='Cargo')
    salary = forms.CharField(label='Salario')
    income_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'datepicker'}),
        label='Fecha de ingreso'
    )
    email = forms.EmailField(label='Email address')
    is_active = forms.BooleanField(label='Activo?')

    def create_user(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        charge = cleaned_data.get('charge')
        salary = cleaned_data.get('salary')
        income_date = cleaned_data.get('income_date')
        email = cleaned_data.get('email')
        is_active = cleaned_data.get('is_active')

        User.objects.create(
            username=username,
            charge=charge,
            salary=salary,
            income_date=income_date,
            email=email,
            is_active=is_active,
        )

    def update_user(self, pk):
        cleaned_data = super().clean()
        username = cleaned_data.get('Nombre')
        charge = cleaned_data.get('Cargo')
        salary = cleaned_data.get('Salario')
        income_date = cleaned_data.get('Fecha de ingreso.')
        email = cleaned_data.get('Email address')
        is_active = cleaned_data.get('Estado')

        user_obj = User.objects.filter(pk=pk)
        user_obj.update(
            username=username,
            charge=charge,
            salary=salary,
            income_date=income_date,
            email=email,
            is_active=is_active,
        )

    class Meta:
        model = User
        fields = [
            'username',
            'charge',
            'salary',
            'income_date',
            'email',
            'is_active',
        ]


class UserHistoryForm(forms.Form):
    title = forms.CharField(label='Título')
    history_type = forms.CharField(label='Tipo de historia')
    description = forms.CharField(label='Descripción')
    criteria_of_acceptance = forms.CharField(label='Criterio de aceptación')
    interface_requirements = forms.CharField(label='Requerimientos de interfaz')
    dependencies = forms.CharField(label='Dependencias')
    project = forms.ModelChoiceField(
        label='Proyecto',
        queryset=Project.objects.all(),
    )

    def create_user_history(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        history_type = cleaned_data.get('history_type')
        description = cleaned_data.get('description')
        criteria_of_acceptance = cleaned_data.get('criteria_of_acceptance')
        interface_requirements = cleaned_data.get('interface_requirements')
        dependencies = cleaned_data.get('dependencies')
        project = cleaned_data.get('project')

        UserHistory.objects.create(
            title=title,
            history_type=history_type,
            description=description,
            criteria_of_acceptance=criteria_of_acceptance,
            interface_requirements=interface_requirements,
            dependencies=dependencies,
            project=project,
        )

    def update_user_history(self, pk):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        history_type = cleaned_data.get('history_type')
        description = cleaned_data.get('description')
        criteria_of_acceptance = cleaned_data.get('criteria_of_acceptance')
        interface_requirements = cleaned_data.get('interface_requirements')
        dependencies = cleaned_data.get('dependencies')
        project = cleaned_data.get('project')

        user_history = UserHistory.objects.filter(pk=pk)
        user_history.update(
            title=title,
            history_type=history_type,
            description=description,
            criteria_of_acceptance=criteria_of_acceptance,
            interface_requirements=interface_requirements,
            dependencies=dependencies,
            project=project,
        )

    class Meta:
        model = UserHistory
        fields = [
            'title',
            'history_type',
            'description',
            'criteria_of_acceptance',
            'interface_requirements',
            'dependencies',
            'project',
        ]
