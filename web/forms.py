from django import forms
from .models import ContactForm

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        labels = {
            'customer_email' : 'Correo',
            'customer_name' : 'Nombre',
            'message' : 'Mensaje',
        }
 