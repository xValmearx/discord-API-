
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.shortcuts import render
from django.http import HttpResponse

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




class DeleteAnnouncementView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView,
):

    model = Announcement

    def test_func(self):
        announcement = self.get_object()
        return announcement.author == self.request.user

    def form_valid(self, form):
        self.object.delete()
        return HttpResponse(status=200)
