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

    path(
        'project_list/',
        views.ProjectListView.as_view(template_name='project_list.html'),
        name='project_list',
    ),

    path(
        'project/<int:pk>/',
        views.ProjectDetailView.as_view(template_name='project_detail.html'),
        name='project_detail',
    ),

    path(
        'project-delete/<int:pk>/',
        views.ProjectDeleteView.as_view(template_name='project_delete.html'),
        name='project_delete',
    ),

    path(
        'project_create/',
        views.ProjectCreateFormView.as_view(),
        name='project_create',
    ),

    path(
        'project_update/<int:pk>/',
        views.ProjectUpdateView.as_view(),
        name='project_update',
    ),

    path(
        'user_list/',
        views.UserListView.as_view(template_name='user_list.html'),
        name='user_list',
    ),

    path(
        'user/<int:pk>/',
        views.UserDetailView.as_view(template_name='user_detail.html'),
        name='user_detail',
    ),

    path(
        'user-delete/<int:pk>/',
        views.UserDeleteView.as_view(template_name='user_delete.html'),
        name='user_delete',
    ),

    path(
        'user_create/',
        views.UserCreateFormView.as_view(),
        name='user_create',
    ),

    path(
        'user_update/<int:pk>/',
        views.UserUpdateView.as_view(),
        name='user_update',
    ),


    path(
        'user_history_list/',
        views.UserHistoryListView.as_view(
            template_name='user_history_list.html'
        ),
        name='user_history_list',
    ),

    path(
        'user_history/<int:pk>/',
        views.UserHistoryDetailView.as_view(
            template_name='user_history_detail.html'
        ),
        name='user_history_detail',
    ),

    path(
        'user_history-delete/<int:pk>/',
        views.UserHistoryDeleteView.as_view(
            template_name='user_history_delete.html'
        ),
        name='user_history_delete',
    ),

    path(
        'user_history_create/',
        views.UserHistoryCreateFormView.as_view(),
        name='user_history_create',
    ),

    path(
        'user_history_update/<int:pk>/',
        views.UserHistoryUpdateView.as_view(),
        name='user_history_update',
    ),

    path(
        'activity_list/',
        views.ActivityListView.as_view(template_name='activity_list.html'),
        name='activity_list',
    ),

    path(
        'activity_detail/<int:pk>/',
        views.ActivityDetailView.as_view(template_name='activity_detail.html'),
        name='activity_detail',
    ),

    path(
        'activity_delete/<int:pk>/',
        views.ActivityDeleteView.as_view(template_name='activity_delete.html'),
        name='activity_delete',
    ),

    path(
        'activity_create/',
        views.ActivityCreateFormView.as_view(),
        name='activity_create',
    ),

    path(
        'activity_update/<int:pk>/',
        views.ActivityUpdateView.as_view(),
        name='activity_update',
    )
]
