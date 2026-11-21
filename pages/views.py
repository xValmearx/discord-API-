from django.views.generic import TemplateView

from announcement.forms import AnnouncementForm
from announcement.models import Announcement


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form"] = AnnouncementForm()

        context["announcements"] = Announcement.objects.none()

        if self.request.user.is_authenticated:
            context["announcements"] = Announcement.objects.filter(
                author=self.request.user
            )

        return context


class AboutPageView(TemplateView):
    template_name = "about.html"