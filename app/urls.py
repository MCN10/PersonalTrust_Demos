# from django.urls import path
#
# from . import views
#
# app_name = "app"
#
#
# urlpatterns = [
#     #Leave as empty string for base url
#
#     #------------ (STORE - URLS) ------------
#
# 	path('', views.landing, name="landing"),
# 	path('home', views.home, name="home"),
# 	path('track/', views.track, name="track"),
# 	path('contact/', views.contact, name="contact"),
#
# ]


from django.urls import path

from . import views

app_name = "PersonalTrust"


urlpatterns = [


	path('', views.tasks, name="tasks"),
	path('home', views.tasks, name="tasks"),
	path('track', views.track, name="track"),
	path('tasks', views.tasks, name="tasks"),
	path('my_tasks/', views.my_tasks, name="my_tasks"),
	path('created_tasks/', views.created_tasks, name="created_tasks"),
    path('add_task/', views.add_task, name="add_task"),
    path('delete_task/<str:pk>/', views.delete_task, name="delete_task"),
    path('update_task/<str:pk>/', views.update_task, name="update_task"),
    path('view_task/<str:pk>/', views.view_task, name="view_task"),
]
