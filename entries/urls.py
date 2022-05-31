from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name ='home'),
    path('entry/create/<str:med>/', views.EntryCreate.as_view(), name='entry-create'),
    # path('entrymedia/create/', views.EntryMediaCreate.as_view(), name='entrymedia-create'),
    path('entry/list/<str:col>/', views.EntryList.as_view(), name="entry-list"),
    path('entry/edit/<str:pk>/', views.EntryEdit.as_view(), name="entry-edit"),
    path('entry/delete/<str:pk>/', views.EntryDelete.as_view(), name="entry-delete"),
    path('entry/select/<str:med>/', views.EntrySelect.as_view(), name="entry-select"),    
    ]