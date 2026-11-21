from django.contrib import admin
from .models import Announcement


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):

    list_display = (
        "text",
        "author",
    )

    search_fields = (
        "text",
        "author__username",
    )

    ordering = (
        "-id",
    )