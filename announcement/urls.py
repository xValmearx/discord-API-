from django.urls import path

from .views import CreateAnnouncementView


urlpatterns = [
    path("create/", CreateAnnouncementView.as_view(), name="create_announcement"),
]