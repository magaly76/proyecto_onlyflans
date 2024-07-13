from django import forms

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Correo', widget=forms.EmailInput(attrs={'class': 'form-control custom-input'}))
    customer_name = forms.CharField(max_length=64, label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Mensaje', widget=forms.TextInput(attrs={'class': 'form-control'}))