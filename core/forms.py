from django import forms
from .models.contactTicketModel import ContactTicket

class ContactTicketForm(forms.ModelForm):
    class Meta:
        model = ContactTicket
        fields = "__all__"
        widgets={
            "authorName": forms.TextInput(attrs={
                "class": "form-control",
            }),
            
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "e.g. johndoe@something.com"
            }),
            
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "07898765432"
            }),
            
            "yearGroup": forms.Select(attrs={
                "class": "form-select",
            }),
            
            "lessonType": forms.Select(attrs={
                "class": "form-select",
            }),
            
            "desc": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Details"
            }),
            
        }