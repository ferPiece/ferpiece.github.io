from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UsuarioRegForm(UserCreationForm):
    class Meta:
        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]

        labels = {
            'username' : 'Nombre de Usuario',
            'first_name' : 'Nombre',
            'last_name' : 'Apellido',
            'email' : 'Email'
        }
        '''
        widgets = {
            'username' : form.TextInput(attrs={'class':'form-control'}),
            'first_name' : form.TextInput(attrs={'class':'form-control'}),
            'last_name' : form.TextInput(attrs={'class':'form-control'}),
            'email' : form.EmailInput(attrs={'class':'form-control'})
        }
        '''
