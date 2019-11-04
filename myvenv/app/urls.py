from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path(
        'team_list/',
        views.TeamListView.as_view(template_name='team_list.html'),
        name='team_list',
    ),
    path(
        'team_list/',
        views.TeamListView.as_view(template_name='team_list.html'),
        name='team_list',
    ),

    path(
        'team/<int:pk>/',
        views.TeamDetailView.as_view(template_name='team_detail.html'),
        name='team_detail',
    ),

    path(
        'team-delete/<int:pk>/',
        views.TeamDeleteView.as_view(template_name='team_delete.html'),
        name='team_delete',
    ),
    path(
        'team_create/',
        views.TeamCreateFormView.as_view(),
        name='team_create',
    ),
    path(
        'team_update/<int:pk>/',
        views.TeamUpdateView.as_view(),
        name='team_update',
    ),
    # path(
    #     'created/',
    #     views.TeamCreateFormView.as_view(template_name='created.html'),
    #     name='created',
    # ),
]
