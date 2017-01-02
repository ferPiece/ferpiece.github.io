from django.shortcuts import render
from django.http import HttpResponseRedirect
from polls.forms import ContactoForm
from polls.models import Contacto
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


def index(request):
    return render(request, "polls/index.html", {})


class ContactoList(ListView):
    model = Contacto
    template_name = 'polls/lista_contactos.html'


class ContactoCreate(CreateView):
    model = Contacto
    template_name = 'polls/form_contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('polls:contacto_list')

    def get_context_data(self, **kwargs):
        context = super(ContactoCreate, self).get_context_data(**kwargs)
        if 'form' is not context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            contacto = form.save()
            contacto.save()
            return HttpResponseRedirect(self.get_success_url())
            #return render(request, "polls/lista_contactos.html", ContactoList.as_view())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ContactoUpdate(UpdateView):
    model = Contacto
    template_name = 'polls/modificar_contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('polls:contacto_list')


class ContactoDelete(DeleteView):
    model = Contacto
    template_name = 'polls/delete_contacto.html'
    success_url = reverse_lazy('polls:contacto_list')




'''
Vista basada en funciones


def contacto_create(request):
    #indico el formulario a utlizar y el metodo HTML
    form = RegForm(request.POST or None)

    #valido los campos del formulario
    if form.is_valid():
        #recupero en un json los datos del formulario
        persona_data = form.cleaned_data


        #recupero los campos obligatorios
        nombre = persona_data.get("nombre")
        apellido = persona_data.get("apellido")
        alias = persona_data.get("alias")
        direccion = persona_data.get("direccion")
        telefono = persona_data.get("telefono")
        email = persona_data.get("email")

        #Forma pichi de crear un objeto en la base de datos
        #creo un objeto de mi modelo
        #contacto = Contacto.objects.create(nombre=nombre, apellido=apellido, alias=alias, direccion=direccion, telefono=telefono, email=email)

        #Forma Chuchi de crear el objeto en la base de datos
        contacto = Contacto()
        contacto.nombre = nombre
        contacto.apellido = apellido
        contacto.alias = alias
        contacto.direccion = direccion
        contacto.email = email
        contacto.telefono = telefono
        contacto.save()


    context = {"el_form":form}
    return render(request, "polls/form_contacto.html", context)
'''
