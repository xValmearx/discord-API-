from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),

    # Pages app
    path("", include("pages.urls")),

    # Accounts app
    path("accounts/", include("accounts.urls")),

    # Django authentication
    path("accounts/", include("django.contrib.auth.urls")),
]