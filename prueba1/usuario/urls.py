from django.conf.urls import url
from usuario.views import CrearUsuario

urlpatterns = [
    url(r'^registrar', CrearUsuario.as_view(), name="registrar"),
]
