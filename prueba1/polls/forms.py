from django import forms
from .models import Contacto

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ["nombre", "apellido", "alias", "email", "direccion", "telefono"]
        labels = {
            "nombre" : "Nombre Contacto",
            "apellido" : "Apeliido Contacto",
            "alias" : "Nombre de Usuario",
            "email" : "Email",
            "direccion" : "Direccion",
            "telefono" : "Telefono"}

        widgets = {
            "nombre" : forms.TextInput(attrs={'class':'form-control}'}),
            "apellido" : forms.TextInput(attrs={'class':'form-control}'}),
            "alias" : forms.TextInput(attrs={'class':'form-control}'}),
            "email" : forms.EmailInput(attrs={'class':'form-control'}),
            "direccion" : forms.TextInput(attrs={'class':'form-control}'}),
            "telefono" : forms.TextInput(attrs={'class':'form-control}'})
        }
    #validaciones para los campos
    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveedor = email.split("@")
        dominio, extension = proveedor.split(".")

        if not extension == "contact":
            raise forms.ValidationError("Por favor uliza un mail con la extension .contact")
        return email

class RegForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    alias = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=150)
    direccion = forms.CharField(max_length=200)
    telefono = forms.IntegerField()


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto

        fields = [
            'nombre',
            'apellido',
            'alias',
            'email',
            'direccion',
            'telefono',
        ]

        labels = {
            'nombre' : 'Nombre Contacto',
            'apellido' : 'Apellido Contacto',
            'alias' : 'Nombre de Usuario',
            'email' : 'Email',
            'direccion': 'Direccion',
            'telefono' : 'Telefono',
            'fecha_creacion' : 'Fecha de Creacion'
        }

        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'apellido' : forms.TextInput(attrs={'class':'form-control'}),
            'alias' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'direccion' : forms.TextInput(attrs={'class':'form-control'}),
            'telefono' : forms.TextInput(attrs={'class':'form-control'})
        }
