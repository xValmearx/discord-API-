
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.shortcuts import render

from .forms import AnnouncementForm
from .models import Announcement


class CreateAnnouncementView(LoginRequiredMixin, CreateView):

    model = Announcement
    form_class = AnnouncementForm
    template_name = "partials/announcement_form.html"

    def form_valid(self, form):

        announcement = form.save(commit=False)
        announcement.author = self.request.user
        announcement.save()

        response = render(
            self.request,
            "partials/announcement_list.html",
            {
                "announcements": Announcement.objects.filter(
                    author=self.request.user
                ),
            },
        )

        response["HX-Trigger"] = "announcementCreated"

        return response