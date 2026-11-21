from django.urls import path

from .views import CreateAnnouncementView, DeleteAnnouncementView


urlpatterns = [
    path(
        "create/", 
         CreateAnnouncementView.as_view(), 
         name="create_announcement"
        ),

    path(
        "delete/<int:pk>/",
        DeleteAnnouncementView.as_view(),
        name="delete_announcement",
        ),
        
]