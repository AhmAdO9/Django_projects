from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path("", views.basic, name="basic"),
    path("register/", views.basic2, name="basic2"),
    path("register/signup", views.signup, name="signup"),
    path("register/signin", views.signin, name="signin"),
    path("register/register", views.basic2, name="re"),
    path("signin", views.signin, name="signin"),
    path("register/logout", views.Logout, name="logout"),
    path("Logout", views.Logout, name="logout"),
    path("register/Logout", views.Logout, name="logout"),
    path("register/book/Appoint/Logout", views.Logout, name="logout"),
    path("book/Appoint/Logout", views.Logout, name="logout"),
    path("post", views.post, name="post"),
    path("register/post", views.post, name="post"),
    path("signin/post", views.post, name="post"),
    path("book/", views.book, name="book"),
    path("register/book/", views.book, name="book"),
    path("book/Appoint/", views.Appoint, name="appoint"),
    path("register/book/Appoint/", views.Appoint, name="appoint"),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

