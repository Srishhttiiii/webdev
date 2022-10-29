from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name ="home"),
    path('support/', views.support, name ="support"),
    path('meditation/', views.meditation, name ="meditation"),
    path('journaling/', views.journaling, name ="journaling"),
    path('timetable/', views.timetable, name ="timetable"),
    path('therapy/', views.therapy, name ="therapy"),
    path('contact/', views.contact, name="contact"),
    path('blogs/', views.blogs, name="blogs"),
    path('rec/', views.rec, name="rec"),
    # path('login/', views.login, name="login"),
    # path('signup/', views.signup, name="signup"),

]
