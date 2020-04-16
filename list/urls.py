from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
        path('', views.index, name="index"),
        url(r'project/(?P<pk>\d+)$', views.view_project_info, name="project_info"),
        url(r'^create/$', views.project_create, name='project_create'),
        url(r'^project/(?P<pk>\d+)/update/$', views.ProjectUpdate.as_view(), name='project_update'),
        url(r'^project/(?P<pk>\d+)/delete/$', views.ProjectDelete.as_view(), name='project_delete'),
        url(r'^task_create/$', views.task_create, name='task_create'),
        url(r'^task_update/(?P<pk>\d+)$', views.task_update, name='task_update'),
        url(r'^task_delete/(?P<pk>\d+)$', views.task_delete, name='task_delete'),
        path('register_page/', views.registerUser, name="register"),
	    path('login_page/', views.loginUser, name="login"),
	    path('logout_page/', views.logoutUser, name="logout"),
]
