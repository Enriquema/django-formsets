from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Compra

# Create your views here.
class ListadoCompras(ListView):
	model = Compra
	template_name = 'compras.html'
	context_object_name = 'compras'

from .forms import CompraForm, DetalleCompraFormSet

class CrearCompra(CreateView):
	model = Compra
	template_name = 'compra.html'
	form_class = CompraForm
	# success_url = reverse_lazy('productos:listado_compras')

