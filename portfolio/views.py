import logging
import os

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.db import DatabaseError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.html import escape
from django.utils.timezone import now

from .forms import AppointmentForm

logger = logging.getLogger(__name__)


def home(request):
    if request.method == "POST":
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            try:
                appointment = appointment_form.save()
            except DatabaseError:
                logger.exception("Failed to save appointment request")
                messages.error(
                    request,
                    "We could not save your appointment request right now. Please try again after the database is configured correctly.",
                )
                return HttpResponseRedirect(f"{reverse('home')}#appointment")
            email_sent = send_appointment_notification(appointment)
            if email_sent:
                messages.success(
                    request,
                    "Your appointment request has been submitted successfully. A notification has been sent to the clinic.",
                )
            else:
                messages.success(
                    request,
                    "Your appointment request has been submitted successfully.",
                )
                messages.warning(
                    request,
                    "The request was saved, but email notification is not configured correctly yet.",
                )
            return HttpResponseRedirect(f"{reverse('home')}#appointment")
        messages.error(
            request,
            "Please correct the highlighted fields and submit the appointment request again.",
        )
    else:
        appointment_form = AppointmentForm()

    site_url = os.getenv("SITE_URL", "").rstrip("/")
    canonical_url = site_url if site_url else request.build_absolute_uri(request.path)
    image_url = (
        f"{site_url}/static/portfolio/images/nephrologist-og.svg"
        if site_url
        else request.build_absolute_uri("/static/portfolio/images/nephrologist-og.svg")
    )
    seo_keywords = [
        "best nephrologist in Chennai",
        "nephrologist in Chennai" ,
        "kidney specialist in Chennai",
        "proteinuria treatment in Chennai",
        "kidney stone specialist in Chennai",
        "urine infection specialist in Chennai",
        "chronic kidney disease doctor in Chennai",
        "dialysis specialist in Chennai",
        "transplant nephrologist in Chennai",
    ]
    context = {
        "doctor": {
            "name": "Dr. Vigneshwaran S",
            "credentials": "DrNB Nephrology, MD General Medicine, MBBS",
            "title": "Nephrologist for Kidney Disease, Dialysis, Proteinuria, Urine Infection, and Transplant-Related Renal Care",
            "tagline": (
                "Dr. Vigneshwaran S, provides evidence-based nephrology care with training in Chronic Kidney Disease, "
                "Acute Kidney Injury, Dialysis Services, Proteinuria Evaluation, Recurrent Urine Infection in Kidney Patients, and Transplant Nephrology."
            ),
            "experience": "3+ years",
            "patients": "Inpatient, OP, ICU care",
            "transplants": "Pre and post-transplant care",
            "location": "Tamil Nadu and Kerala",
        },
        "highlights": [
            "Nephrologist with tertiary-care exposure in CKD, Dialysis, AKI, and Transplant Medicine",
            "Experienced in evaluation of Proteinuria, Resistant Hypertension, Recurrent Urine Infection, and Glomerular Disorders",
            "Clinical training across Outpatient Nephrology, Inpatient Renal Care, Dialysis Units, and ICU Nephrology Services",
        ],
        "profile_points": [
            "Nephrology superspecialty training completed through the National Board of Examinations at VPS Lakeshore Hospital and Research Limited, Kochi",
            "Strong internal medicine base from Madras Medical College with progression into dedicated renal and transplant care",
            "Works closely with urology, cardiology, and critical care teams in complex renal and metabolic cases",
        ],
        "expertise": [
            {
                "title": "Chronic Kidney Disease Management",
                "description": "Evaluation and longitudinal management of CKD across stages, including diabetic kidney disease and resistant hypertension.",
            },
            {
                "title": "Dialysis Care and Prescription",
                "description": "Supervision of hemodialysis services, dialysis prescription, adequacy review, access care, and complication management.",
            },
            {
                "title": "Transplant Nephrology",
                "description": "Pre-transplant evaluation, post-transplant immunosuppression monitoring, infection surveillance, and clinical rejection follow-up.",
            },
            {
                "title": "Acute and Critical Care Nephrology",
                "description": "Management of AKI, sepsis-associated kidney injury, electrolyte imbalance, acid-base disorders, and CRRT-related clinical decisions.",
            },
        ],
        "services": [
            "Chronic kidney disease and diabetic kidney disease management",
            "Acute kidney injury, ICU nephrology, and electrolyte disorder evaluation",
            "Hemodialysis initiation, prescription review, and complication management",
            "Glomerulonephritis, nephrotic syndrome, and resistant hypertension assessment",
            "Renal transplant evaluation and post-operative nephrology follow-up",
            "Academic case discussion, journal review, and protocol-based inpatient management",
        ],
        "conditions": [
            {
                "title": "Kidney Disease",
                "description": "Assessment and treatment planning for chronic kidney disease, diabetic kidney disease, acute kidney injury, and progressive loss of kidney function.",
            },
            {
                "title": "Proteinuria",
                "description": "Evaluation of protein in urine, nephrotic syndrome, glomerular disease, and kidney damage risk with appropriate renal work-up and follow-up.",
            },
            {
                "title": "Kidney Stone and Renal Risk Assessment",
                "description": "Nephrology evaluation for recurrent kidney stone disease, metabolic risk factors, kidney function impact, and referral coordination with urology where required.",
            },
            {
                "title": "Urine Infection and Recurrent UTI",
                "description": "Assessment of recurrent urine infection, complicated UTI in kidney patients, and infection risk in chronic kidney disease and post-transplant settings.",
            },
        ],
        "journey": [
            {
                "year": "2018",
                "title": "MBBS, Kanyakumari Government Medical College, Asaripallam",
                "description": "Completed undergraduate medical training with a strong base in internal medicine and acute care.",
            },
            {
                "year": "2019-2022",
                "title": "Junior Resident, General Medicine, Madras Medical College",
                "description": "Managed diverse inpatient medical cases and built a strong foundation in internal medicine and emergency care.",
            },
            {
                "year": "2022",
                "title": "MD General Medicine, Madras Medical College, Chennai",
                "description": "Completed postgraduate training in general medicine before moving into dedicated nephrology specialization.",
            },
            {
                "year": "2022-2023",
                "title": "Senior Resident, General Medicine, A.C.S Medical College Hospital, Chennai",
                "description": "Continued hospital-based patient care with emphasis on complex medicine and interdisciplinary management.",
            },
            {
                "year": "2023-2026",
                "title": "Senior Resident, Nephrology, VPS Lakeshore Hospital and Research Limited, Kochi",
                "description": "Managed outpatient and inpatient nephrology, dialysis units, ICU renal cases, renal biopsy workflows, and transplant-related care.",
            },
            {
                "year": "2026",
                "title": "DrNB Nephrology, National Board of Examinations, India",
                "description": "Completed superspecialty nephrology training with broad exposure to academic and tertiary kidney care practice.",
            },
        ],
        "achievements": [
            "1st prize in ISN South Zone and NAKON poster presentation",
            "Presented papers and attended multiple nephrology conferences",
            "Actively involved in journal clubs and structured case discussions",
            "Familiar with KDIGO guidelines and evidence-based nephrology pathways",
        ],
        "research_focus": [
            "Evidence-based nephrology practice guided by KDIGO recommendations",
            "Case discussions, journal clubs, and academic presentations",
            "Ongoing development in dialysis, transplant, and critical care nephrology",
        ],
        "strengths": [
            {
                "title": "Core Clinical Competencies",
                "points": [
                    "CKD, AKI, glomerulonephritis, nephrotic syndrome, diabetic kidney disease",
                    "Hypertension, resistant hypertension, electrolyte and acid-base disorders",
                    "Pre- and post-transplant renal patient evaluation and monitoring",
                ],
            },
            {
                "title": "Procedural Exposure",
                "points": [
                    "Ultrasound-guided renal biopsy assistance and post-biopsy care",
                    "Temporary and permanent dialysis catheter care",
                    "Dialysis troubleshooting, fluid balance review, and CRRT decision-making",
                ],
            },
            {
                "title": "Professional Skills",
                "points": [
                    "Strong clinical decision-making",
                    "Patient counseling and education",
                    "Team leadership, coordination, and EMR familiarity",
                ],
            },
        ],
        "faqs": [
            {
                "question": "When should someone see a nephrologist?",
                "answer": "Persistent swelling, uncontrolled blood pressure, protein in urine, kidney stones with recurrent infections, or abnormal creatinine values should be evaluated early.",
            },
            {
                "question": "Do all kidney patients require dialysis?",
                "answer": "No. Many patients can preserve kidney function for years with medication, lifestyle changes, and close monitoring when treatment starts early.",
            },
            {
                "question": "Can a nephrologist treat proteinuria?",
                "answer": "Yes. Proteinuria is a key sign of kidney disease. A nephrologist evaluates the cause, estimates kidney damage risk, and plans treatment to reduce protein loss and protect kidney function.",
            },
            {
                "question": "Should I see a nephrologist for kidney stone problems?",
                "answer": "A nephrologist is useful when kidney stones are recurrent, associated with reduced kidney function, frequent urine infections, or metabolic abnormalities. Surgical stone removal is usually coordinated with urology when needed.",
            },
            {
                "question": "When does a urine infection need nephrology evaluation?",
                "answer": "Urine infection needs nephrology review when it keeps recurring, affects someone with kidney disease, occurs after transplant, or is accompanied by worsening creatinine, swelling, or blood pressure changes.",
            },
            {
                "question": "Is teleconsultation available for follow-up?",
                "answer": "Consultation format depends on clinical need and appointment availability. In-person evaluation is important when there are active symptoms, abnormal kidney reports, or the need for detailed examination.",
            },
        ],
        "contact": {
            "hospital": "Dr. Vigneshwaran S Nephrology Profile",
            "address": "Available for nephrology consultations and institutional opportunities in Tamil Nadu, Kerala, and South India",
            "phone": "9600441305",
            "email": "sakthivignesh527@gmail.com",
            "hours": "Professional appointments by prior communication",
        },
        "memberships": [
            "Indian Society of Nephrology (ISN)",
            "Indian Society of Organ Transplantation",
        ],
        "certifications": [
            "BLS / ACLS",
            "AI in Medicine",
        ],
        "languages": [
            "English",
            "Tamil",
            "Malayalam",
            "Hindi",
        ],
        "career_objective": (
            "Open to consultant nephrology, senior residency, and institutional kidney care roles where training in dialysis, transplant nephrology, critical care nephrology, and evidence-based renal medicine can support high-quality patient outcomes."
        ),
        "appointment_intro": (
            "Patients can submit an appointment request for kidney disease, proteinuria, kidney stone-related renal evaluation, urine infection, dialysis review, or transplant follow-up."
        ),
        "appointment_form": appointment_form,
        "seo": {
            "title": "Dr. Vigneshwaran S | Nephrologist and Kidney Specialist",
            "description": (
                "Dr. Vigneshwaran S is a nephrologist with training in kidney disease, proteinuria, dialysis, "
                "kidney stone evaluation, recurrent urine infection in kidney patients, transplant nephrology, and critical care renal medicine."
            ),
            "keywords": ", ".join(seo_keywords),
            "canonical_url": canonical_url,
            "image_url": image_url,
        },
    }
    return render(request, "portfolio/home.html", context)


def send_appointment_notification(appointment):
    recipient = settings.APPOINTMENT_NOTIFICATION_EMAIL or settings.EMAIL_HOST_USER
    if not recipient:
        return False

    subject = (
        f"New appointment request: {appointment.patient_name} - "
        f"{appointment.get_condition_display()}"
    )
    message = "\n".join(
        [
            "A new nephrology appointment request has been submitted.",
            "",
            f"Patient name: {appointment.patient_name}",
            f"Phone: {appointment.phone}",
            f"Email: {appointment.email}",
            f"Age: {appointment.age or 'Not provided'}",
            f"City: {appointment.city or 'Not provided'}",
            f"Appointment type: {appointment.get_appointment_type_display()}",
            f"Main concern: {appointment.get_condition_display()}",
            f"Preferred date: {appointment.preferred_date}",
            f"Preferred time: {appointment.preferred_time}",
            "",
            "Clinical note:",
            appointment.message or "No additional notes provided.",
        ]
    )

    resend_api_key = os.getenv("RESEND_API_KEY")
    if resend_api_key:
        import json
        import urllib.request
        
        url = "https://api.resend.com/emails"
        headers = {
            "Authorization": f"Bearer {resend_api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "from": "Clinic Notifications <onboarding@resend.dev>",
            "to": [recipient],
            "subject": subject,
            "text": message
        }
        
        req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req) as response:
                return True
        except Exception as e:
            logger.exception(f"Failed to send appointment notification email via Resend API: {e}")
            return False
    else:
        try:
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient], fail_silently=False)
        except Exception:
            logger.exception("Failed to send appointment notification email")
            return False
        return True


def robots_txt(request):
    site_url = os.getenv("SITE_URL", "").rstrip("/")
    sitemap_url = f"{site_url}/sitemap.xml" if site_url else request.build_absolute_uri("/sitemap.xml")
    content = "\n".join(
        [
            "User-agent: *",
            "Allow: /",
            f"Sitemap: {sitemap_url}",
        ]
    )
    return HttpResponse(content, content_type="text/plain")


def sitemap_xml(request):
    site_url = os.getenv("SITE_URL", "").rstrip("/")
    homepage = f"{site_url}/" if site_url else request.build_absolute_uri("/")
    lastmod = now().date().isoformat()
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{escape(homepage)}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
"""
    return HttpResponse(xml, content_type="application/xml")
