from django.contrib import admin
from .forms import RegModelForm
from .models import Question, Contacto

class AdminContacto(admin.ModelAdmin):
    #campos que deseo mostrar
    list_display = ["id","nombre", "apellido", "alias", "direccion", "email", "telefono", "fecha_creacion"]
    form = RegModelForm
    list_filter = ["fecha_creacion"]
    #list_editable = ["direccion"]
    search_fields = ["apellido"]

    #class Meta:
    #    model = Contacto

admin.site.register(Contacto, AdminContacto)
