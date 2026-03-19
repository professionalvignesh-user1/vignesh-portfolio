from django import forms
from django.utils import timezone

from .models import Appointment


class AppointmentForm(forms.ModelForm):
    website = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "autocomplete": "off",
                "tabindex": "-1",
                "class": "honeypot-input",
            }
        ),
    )

    class Meta:
        model = Appointment
        fields = [
            "patient_name",
            "phone",
            "email",
            "age",
            "city",
            "appointment_type",
            "condition",
            "preferred_date",
            "preferred_time",
            "message",
        ]
        widgets = {
            "preferred_date": forms.DateInput(attrs={"type": "date"}),
            "preferred_time": forms.TimeInput(attrs={"type": "time"}),
            "message": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "patient_name": "Full name",
            "phone": "Phone number",
            "email": "Email address",
            "age": "Age",
            "city": "City",
            "message": "Describe symptoms, diagnosis, reports, or the reason for appointment",
        }
        for field_name, field in self.fields.items():
            css_class = "form-control"
            if field_name == "message":
                css_class += " form-control-textarea"
            field.widget.attrs["class"] = css_class
            if field_name in placeholders:
                field.widget.attrs["placeholder"] = placeholders[field_name]

    def clean_preferred_date(self):
        preferred_date = self.cleaned_data["preferred_date"]
        if preferred_date < timezone.localdate():
            raise forms.ValidationError("Please choose today or a future date.")
        return preferred_date

    def clean_website(self):
        value = self.cleaned_data.get("website", "")
        if value:
            raise forms.ValidationError("Spam detected.")
        return value
