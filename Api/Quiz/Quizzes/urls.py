from django.urls import path
from . import views
# from Quizzes.views import Register



urlpatterns = [

    path('quizzes/<id>/', views.list_all , name="List"),
    path('quizzes/<id>/result/', views.Result , name="Result"),
    path('quizzes/', views.create , name="create"),
    path('quizzes/active/', views.active , name="active"),
    path('quizzes/participate/', views.participate , name="participate"),
    # path('register/<id>/', Register.as_view()),
    path('update/<id>/', views.update )

    ]
