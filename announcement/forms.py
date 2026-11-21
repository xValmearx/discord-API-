from django import forms

from .models import Announcement


class AnnouncementForm(forms.ModelForm):

    class Meta:
        model = Announcement
        fields = ["text"]

        widgets = {
            "text": forms.Textarea(
                attrs={
                    "placeholder": "Write an announcement...",
                    "rows": 3,
                    "maxlength": 250,
                }
            )
        }