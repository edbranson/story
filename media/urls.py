from django.urls import path
from . import views

urlpatterns = [
    path('media/create/', views.MediaCreate.as_view(), name="media-create"),
    path('media/createfor/', views.MediaCreateFor.as_view(), name="media-createfor"),
    # path('media/clonefor/<str:pk>/', views.MediaCloneFor.as_view(), name="media-clonefor"),
    path('media/clonefor/<str:pk>/<format>/', views.MediaCloneFor.as_view(), name="media-clonefor"),
    path('media/list/<str:col>/', views.MediaList.as_view(), name="media-list"),
    # path('media/listfor/', views.MediaListForEntry.as_view(), name="media-entry"),
    path('media/search/', views.MediaSearch.as_view(), name="media-search"),
    path('media/select/<str:pk>/', views.MediaSelect.as_view(), name="media-select"),
    path('media/edit/<str:pk>/', views.MediaEdit.as_view(), name="media-edit"),
    path('media/delete/<str:pk>/', views.MediaDelete.as_view(), name="media-delete"),
    ]