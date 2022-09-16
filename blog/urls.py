# from django.contrib import admin
from django.urls import path,include
from .views import User_dataCreateView,User_dataUpdate,user_dataAPI,User_dataRetrive,User_dataDelete
from . import views
urlpatterns = [
    path("", user_dataAPI.as_view(),name='API_list_all'),
    path("<int:pk>", user_dataAPI.as_view(),name='API_list_one'),
    path("delete/<int:pk>/", user_dataAPI.as_view(),name='API_delete'),
    path("update/<str:pram>=<str:udata>/<int:pk>/", user_dataAPI.as_view(),name='API_update'),
    path("UI/", User_dataCreateView.as_view(), name='User_Create_View'),
    path("UI/list/<int:pk>/", User_dataRetrive.as_view(), name='User_Retrieve'),
    path("UI/delete/<int:pk>/", User_dataDelete.as_view(), name='User_Delete'),
    path("UI/update/<int:pk>/", User_dataUpdate.as_view(), name='User_Update'),



]
