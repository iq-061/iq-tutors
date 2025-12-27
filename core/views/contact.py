from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def contact(request):
    """
    Contact form -> sends an email to CONTACT_TO_EMAIL (or DEFAULT_FROM_EMAIL fallback)
    containing: name, year group, lesson type, and a message about goals/situation.
    """
    if request.method == "GET":
        return render(request, "contact.html")

    # POST
    name = (request.POST.get("full_name") or "").strip()
    parent_email = (request.POST.get("email") or "").strip()
    year_group = (request.POST.get("year_group") or "").strip()
    lesson_type = (request.POST.get("lesson_type") or "").strip()
    message = (request.POST.get("message") or "").strip()

    # Basic validation
    errors = []
    if not name:
        errors.append("Please enter your name.")
    if not parent_email:
        errors.append("Please enter your email address.")
    if year_group not in {"Year 7", "Year 8", "Year 9", "Year 10", "Year 11"}:
        errors.append("Please select a valid year group.")
    if lesson_type not in {"1-to-1", "Focus group (up to 4)"}:
        errors.append("Please select a valid lesson type.")
    if not message or len(message) < 10:
        errors.append("Please include a short description (at least 10 characters).")

    if errors:
        for e in errors:
            messages.error(request, e)
        # Re-render with the user's previous input so they don't lose it
        context = {
            "prefill": {
                "name": name,
                "email": parent_email,
                "year_group": year_group,
                "lesson_type": lesson_type,
                "message": message,
            }
        }
        return render(request, "contact.html", context)

    to_email = getattr(settings, "CONTACT_TO_EMAIL", None) or getattr(settings, "DEFAULT_FROM_EMAIL", None)
    if not to_email:
        messages.error(request, "Email is not configured on the server (CONTACT_TO_EMAIL / DEFAULT_FROM_EMAIL missing).")
        return redirect("contact")

    subject = f"IQ Tutors Consultation Enquiry — {name} ({year_group}, {lesson_type})"
    body = (
        "New consultation enquiry from the website:\n\n"
        f"Name: {name}\n"
        f"Parent Email: {parent_email}\n"
        f"Year Group: {year_group}\n"
        f"Lesson Type: {lesson_type}\n\n"
        "Child’s situation & goals:\n"
        f"{message}\n"
    )

    # From: use DEFAULT_FROM_EMAIL (must be allowed by your email backend)
    from_email = getattr(settings, "DEFAULT_FROM_EMAIL", None)

    email = EmailMessage(
        subject=subject,
        body=body,
        from_email=from_email,
        to=[to_email],
        reply_to=[parent_email],  # so you can reply directly to the parent
    )

    try:
        email.send(fail_silently=False)
    except Exception as e:
        messages.error(request, f"Sorry — the message could not be sent. ({e})")
        context = {
            "prefill": {
                "name": name,
                "email": parent_email,
                "year_group": year_group,
                "lesson_type": lesson_type,
                "message": message,
            }
        }
        return render(request, "contact.html", context)

    messages.success(request, "Thanks! Your enquiry has been sent. We’ll get back to you shortly.")
    return redirect("contact")
