from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name ='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('index/', views.index, name='index'),
    path('tmp/', views.tmp, name='tmp'),
    path('tmp_origin/', views.tmp_origin, name='tmp_origin'),
]
