from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Appointment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("patient_name", models.CharField(max_length=120)),
                ("phone", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("age", models.PositiveSmallIntegerField(blank=True, null=True)),
                ("city", models.CharField(blank=True, max_length=120)),
                (
                    "appointment_type",
                    models.CharField(
                        choices=[
                            ("new_consultation", "New Consultation"),
                            ("follow_up", "Follow-up Review"),
                            ("second_opinion", "Second Opinion"),
                            ("dialysis_review", "Dialysis Review"),
                        ],
                        default="new_consultation",
                        max_length=32,
                    ),
                ),
                (
                    "condition",
                    models.CharField(
                        choices=[
                            ("kidney_disease", "Kidney Disease"),
                            ("proteinuria", "Proteinuria"),
                            ("kidney_stone", "Kidney Stone"),
                            ("urine_infection", "Urine Infection"),
                            ("hypertension", "Hypertension"),
                            ("transplant", "Transplant Follow-up"),
                            ("other", "Other Kidney Concern"),
                        ],
                        default="kidney_disease",
                        max_length=32,
                    ),
                ),
                ("preferred_date", models.DateField()),
                ("preferred_time", models.TimeField()),
                ("message", models.TextField(blank=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "New"),
                            ("confirmed", "Confirmed"),
                            ("rescheduled", "Rescheduled"),
                            ("completed", "Completed"),
                            ("cancelled", "Cancelled"),
                        ],
                        default="new",
                        max_length=16,
                    ),
                ),
                ("admin_notes", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
