from django.conf.urls import url
from . import views
from polls.views import ContactoList, ContactoCreate, ContactoUpdate, ContactoDelete
from polls.models import Contacto

urlpatterns = [
    url(r'^home$', views.index, name='home'),
    url(r'^listar$', ContactoList.as_view(), name='contacto_list'),
    url(r'^agregar$', ContactoCreate.as_view(), name='contacto_create'),
    url(r'^modificar/(?P<pk>\d+)/$', ContactoUpdate.as_view(), name='contacto_update'),
    url(r'^eliminar/(?P<pk>\d+)/$', ContactoDelete.as_view(), name='contacto_delete'),
]
