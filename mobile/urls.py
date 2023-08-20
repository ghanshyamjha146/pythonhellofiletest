from django.urls import path
from .import views

urlpatterns = [
    path('test', views.test, name = 'test'),
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.user_login, name='user_login'),
    path('about', views.about, name='about'),
    path('logout', views.logout_view, name='logout'),
    path('user_page', views.user_page, name='user_page'),

]