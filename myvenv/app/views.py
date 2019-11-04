from . import models
from .forms import TeamForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
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
    template_name = 'team_create.html'
    form_class = TeamForm
    success_url = '/app/team_list/'
    object = models.Team

    def get_object(self, queryset=None):
        return get_object_or_404(models.Team, id=self.kwargs['pk'])

    def form_valid(self, form):
        form.update_team(pk=self.kwargs['pk'])

        return super().form_valid(form)
