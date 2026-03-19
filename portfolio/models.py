from django.db import models


class Appointment(models.Model):
    class AppointmentType(models.TextChoices):
        NEW = "new_consultation", "New Consultation"
        FOLLOW_UP = "follow_up", "Follow-up Review"
        SECOND_OPINION = "second_opinion", "Second Opinion"
        DIALYSIS = "dialysis_review", "Dialysis Review"

    class Condition(models.TextChoices):
        KIDNEY_DISEASE = "kidney_disease", "Kidney Disease"
        PROTEINURIA = "proteinuria", "Proteinuria"
        KIDNEY_STONE = "kidney_stone", "Kidney Stone"
        URINE_INFECTION = "urine_infection", "Urine Infection"
        HYPERTENSION = "hypertension", "Hypertension"
        TRANSPLANT = "transplant", "Transplant Follow-up"
        OTHER = "other", "Other Kidney Concern"

    class Status(models.TextChoices):
        NEW = "new", "New"
        CONFIRMED = "confirmed", "Confirmed"
        RESCHEDULED = "rescheduled", "Rescheduled"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    patient_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    city = models.CharField(max_length=120, blank=True)
    appointment_type = models.CharField(
        max_length=32,
        choices=AppointmentType.choices,
        default=AppointmentType.NEW,
    )
    condition = models.CharField(
        max_length=32,
        choices=Condition.choices,
        default=Condition.KIDNEY_DISEASE,
    )
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    message = models.TextField(blank=True)
    status = models.CharField(
        max_length=16,
        choices=Status.choices,
        default=Status.NEW,
    )
    admin_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.patient_name} - {self.get_condition_display()} - {self.preferred_date}"
