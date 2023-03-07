from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    #path('list/', views.uav_list)
    path('register/', views.register_page, name='register_user'),
    path('login/', views.login_page, name='login_user'),
    path('add/', views.uav_form),
    path('<int:id>/', views.uav_form, name="uav_update"),
    path('delete/<int:id>/', views.uav_delete, name="uav_delete")
]