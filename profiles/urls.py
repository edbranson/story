from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name = 'register'),
    path('login/', views.LoginUser.as_view(), name = 'login'),
    path('logout/', views.LogoutUser.as_view(), name = 'logout'),
    path('profiles/', views.ProfileList.as_view(), name="profile-list"),
    path('profiles/create/', views.ProfileCreate.as_view(), name="profile-create"),
    path('profiles/edit/<str:pk>/', views.ProfileEdit.as_view(), name="profile-edit"),
    path('profiles/delete/<str:pk>/', views.ProfileDelete.as_view(), name="profile-delete"),
    path('profiles/tags/', views.TagList.as_view(), name="tag-list"),
    path('profiles/tags/create/', views.TagCreate.as_view(), name="tag-create"),
    path('profiles/tags/edit/<str:pk>', views.TagEdit.as_view(), name="tag-edit"),
    path('profiles/tags/delete/<str:pk>', views.TagDelete.as_view(), name="tag-delete"),
    ]