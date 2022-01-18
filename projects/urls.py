from django.urls import path

from projects import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('sergiu-projects/<int:pk>', views.project_detail, name='project-detail'),
    path('all-projects', views.project_list, name='all-projects')

]
