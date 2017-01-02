from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from usuario.forms import UsuarioRegForm
# Create your views here.
class CrearUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = UsuarioRegForm
    success_url = reverse_lazy('polls:contacto_list')
