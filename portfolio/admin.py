from django.contrib import admin

from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "patient_name",
        "condition",
        "appointment_type",
        "preferred_date",
        "preferred_time",
        "status",
        "created_at",
    )
    list_filter = ("status", "condition", "appointment_type", "preferred_date")
    search_fields = ("patient_name", "phone", "email", "city", "message")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "Patient details",
            {
                "fields": (
                    "patient_name",
                    "phone",
                    "email",
                    "age",
                    "city",
                )
            },
        ),
        (
            "Appointment request",
            {
                "fields": (
                    "appointment_type",
                    "condition",
                    "preferred_date",
                    "preferred_time",
                    "message",
                )
            },
        ),
        (
            "Internal handling",
            {
                "fields": (
                    "status",
                    "admin_notes",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )
