from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects_index, name='index'),
    path('projects/<int:project_id>/', views.projects_detail, name='detail'),
    path('projects/create/', views.ProjectCreate.as_view(), name='projects_create'),
    path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='projects_update'),
    path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='projects_delete'),
    path('projects/<int:project_id>/add_progress/', views.add_progress, name='add_progress'),
    path('components/', views.ComponentList.as_view(), name='components_index'),
    path('components/<int:pk>/', views.ComponentDetail.as_view(), name='components_detail'),
    path('components/create/', views.ComponentCreate.as_view(), name='components_create'),
    path('components/<int:pk>/update/', views.ComponentUpdate.as_view(), name='components_update'),
    path('components/<int:pk>/delete/', views.ComponentDelete.as_view(), name='components_delete'),
]

