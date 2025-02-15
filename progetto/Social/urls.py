from django.urls import path
from Social.views import *
from django.contrib.auth import views as auth_views

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('', homepage, name='homepage'),
    path("list_company/", list_company, name='list_company'),
    path("list_post/", list_post, name='list_post'), 
    path('company/<int:company_id>/', company_detail, name='company_detail'),
    path('register/', register, name='register'),
    path('create_company/', create_company, name='create_company'),
    path('create_post/', create_post, name='create_post'),
    path('create_tipologia/', create_tipologia, name='create_tipologia'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('post/<int:id>/', post_detail, name='post_detail'), 
    path('sentry-debug/', trigger_error),
    path('upload_csv/', upload_and_predict, name='upload_csv'),
]