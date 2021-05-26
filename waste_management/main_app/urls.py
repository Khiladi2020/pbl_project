from django.urls import path

from . import views

app_name='main_app'

urlpatterns = [
	path('welcome',views.welcome,name="welcome"),
	path('test',views.test,name="test"),
	path('auth/login',views.login_user,name="login"),
	path('auth/signup',views.signup_user,name="signup"),
	path('auth/logout',views.logout_user,name="logout"),
	path('',views.home,name="home"),
	path('daily-waste',views.daily_waste,name="daily-waste"),
	path('stats',views.stats,name="stats"),
	path('vote',views.vote,name="vote"),
	path('awareness',views.awareness,name="awareness"),
	path('contact',views.contact,name="contact"),
]