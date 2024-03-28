from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard/<int:category>/', views.index, name='index'),
    path('submit_quiz/', views.submit_quiz, name='submit_quiz'),
    path('result/<int:score>/<int:total_questions>/<str:correct_answers>/', views.result, name='result'),
]
