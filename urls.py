
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('faculty',views.faculty,name="faculty"),
    path('addquestion',views.addquestion,name="addquestion"),
    path('add_question',views.add_question,name="add_question"),
    path('questionslist',views.questionslist,name="questionslist"),
    path('signup',views.signup,name="signup"),
    
    
    path('login',views.login,name="login")
    
]