from django.urls import path
from . import views

urlpatterns = [
    path('media/create/', views.MediaCreate.as_view(), name="media-create"),
    path('media/list/<str:col>/', views.MediaList.as_view(), name="media-list"),
    path('media/select/<str:pk>/', views.MediaSelect.as_view(), name="media-select"),
    path('media/edit/<str:pk>/', views.MediaEdit.as_view(), name="media-edit"),
    path('media/delete/<str:pk>/', views.MediaDelete.as_view(), name="media-delete"),
    ]