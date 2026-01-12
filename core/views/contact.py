from django.shortcuts import render, redirect
from core.forms import ContactTicketForm
from django.http import HttpResponse
from django.contrib import messages


def contact(request):
    if request.method == "POST":
        form = ContactTicketForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your message has been received. We’ll get back to you shortly."
            )
            return redirect("contact")
        
    else:
        form = ContactTicketForm()
    
    return render(request, "contact.html", {"form": form})
    
