from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name="users"),
    path('profile/<str:pk>', views.userProfile, name="profile"),
    path('sendMessage/<str:pk>', views.sendMessage, name="sendMessage"),
    path('inbox/', views.inbox, name='inbox'),
    path('message/<str:pk>', views.viewMessage, name="message"),
    path('createUser/', views.createUser, name="createUser"),
    path('logout/', views.logoutUser, name="logout"),
    path('login/', views.loginUser, name="login"),
    path('updateUser/', views.updateUser, name="updateUser"),
]
