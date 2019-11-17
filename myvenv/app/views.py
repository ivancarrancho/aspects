from . import models
from .forms import TeamForm
from .forms import UserForm
from .forms import UserHistoryForm
from .forms import ProjectForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic.edit import FormView


class TeamListView(ListView):
    model = models.Team
    template = 'team_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_queryset(self):
        queryset = models.Team.objects.all()

        return queryset


class TeamDetailView(DetailView):
    object = models.Team

    def get_object(self, queryset=None):
        return get_object_or_404(models.Team, id=self.kwargs['pk'])


class TeamDeleteView(DeleteView):
    def get_object(self, queryset=None):
        obj = get_object_or_404(models.Team, pk=self.kwargs['pk'])

        if obj:
            obj.delete()
            return JsonResponse({'ok': True})

        return JsonResponse({'ok': False})


class TeamCreateFormView(FormView):
    template_name = 'team_create.html'
    form_class = TeamForm
    success_url = '/app/team_list/'

    def form_valid(self, form):
        form.create_team()

        return super().form_valid(form)


class TeamUpdateView(FormView, DetailView):
    object = models.Team
    template_name = 'team_create.html'
    form_class = TeamForm
    success_url = '/app/team_list/'

    def get_object(self, queryset=None):
        return get_object_or_404(models.Team, id=self.kwargs['pk'])

    def form_valid(self, form):
        form.update_team(pk=self.kwargs['pk'])

        return super().form_valid(form)


class ProjectListView(ListView):
    model = models.Project
    template = 'project_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_queryset(self):
        queryset = models.Project.objects.all()

        return queryset


class ProjectDetailView(DetailView):
    object = models.Project

    def get_object(self, queryset=None):
        return get_object_or_404(models.Project, id=self.kwargs['pk'])


class ProjectDeleteView(DeleteView):
    def get_object(self, queryset=None):
        obj = get_object_or_404(models.Project, pk=self.kwargs['pk'])

        if obj:
            obj.delete()
            return JsonResponse({'ok': True})

        return JsonResponse({'ok': False})


class ProjectCreateFormView(FormView):
    template_name = 'project_create.html'
    form_class = ProjectForm
    success_url = '/app/project_list/'

    def form_valid(self, form):
        form.create_project()

        return super().form_valid(form)


class ProjectUpdateView(FormView, DetailView):
    object = models.Project
    template_name = 'project_create.html'
    form_class = ProjectForm
    success_url = '/app/project_list/'

    def get_object(self, queryset=None):
        return get_object_or_404(models.Project, id=self.kwargs['pk'])

    def form_valid(self, form):
        form.update_project(pk=self.kwargs['pk'])

        return super().form_valid(form)


class UserListView(ListView):
    model = models.User
    template = 'user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_queryset(self):
        queryset = models.User.objects.all()

        return queryset


class UserDetailView(DetailView):
    object = models.User

    def get_object(self, queryset=None):
        return get_object_or_404(models.User, id=self.kwargs['pk'])


class UserDeleteView(DeleteView):
    def get_object(self, queryset=None):
        obj = get_object_or_404(models.User, pk=self.kwargs['pk'])

        if obj:
            obj.delete()
            return JsonResponse({'ok': True})

        return JsonResponse({'ok': False})


class UserCreateFormView(FormView):
    template_name = 'user_create.html'
    form_class = UserForm
    success_url = '/app/user_list/'

    def form_valid(self, form):
        form.create_user()

        return super().form_valid(form)


class UserUpdateView(FormView, DetailView):
    object = models.User
    template_name = 'user_create.html'
    form_class = UserForm
    success_url = '/app/user_list/'

    def get_object(self, queryset=None):
        return get_object_or_404(models.User, id=self.kwargs['pk'])

    def form_valid(self, form):
        form.update_user(pk=self.kwargs['pk'])

        return super().form_valid(form)


# ************************************
class UserHistoryListView(ListView):
    model = models.UserHistory
    template = 'user_history_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_queryset(self):
        queryset = models.UserHistory.objects.all()

        return queryset


class UserHistoryDetailView(DetailView):
    object = models.UserHistory

    def get_object(self, queryset=None):
        return get_object_or_404(models.UserHistory, id=self.kwargs['pk'])


class UserHistoryDeleteView(DeleteView):
    def get_object(self, queryset=None):
        obj = get_object_or_404(models.UserHistory, pk=self.kwargs['pk'])

        if obj:
            obj.delete()
            return JsonResponse({'ok': True})

        return JsonResponse({'ok': False})


class UserHistoryCreateFormView(FormView):
    template_name = 'user_history_create.html'
    form_class = UserHistoryForm
    success_url = '/app/user_history_list/'

    def form_valid(self, form):
        form.create_user_history()

        return super().form_valid(form)


class UserHistoryUpdateView(FormView, DetailView):
    object = models.UserHistory
    template_name = 'user_history_create.html'
    form_class = UserHistoryForm
    success_url = '/app/user_history_list/'

    def get_object(self, queryset=None):
        return get_object_or_404(models.UserHistory, id=self.kwargs['pk'])

    def form_valid(self, form):
        form.update_user_history(pk=self.kwargs['pk'])

        return super().form_valid(form)
