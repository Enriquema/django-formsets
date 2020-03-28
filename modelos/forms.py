import django.forms as forms
from .models import Compra, DetalleCompra

class CompraForm(forms.ModelForm):

	class Meta:
		model = Compra
		fields = ['proveedor']

	def __init__(self, *args, **kwargs):
		super(CompraForm, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

class DetalleCompraForm(forms.ModelForm):

	class Meta:
		model = DetalleCompra
		fields = ['producto','cantidad','precio_compra']

	def __init__(self, *args, **kwargs):
		super(DetalleCompraForm, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

	def clean_cantidad(self):
		cantidad = self.cleaned_data['cantidad']
		if cantidad == '':
			raise forms.ValidationError("Debe ingresar una cantidad valida")
		return cantidad

	def clean_precio_compra(self):
		precio = self.cleaned_data['precio_compra']
		if precio == '':
			raise forms.ValidationError("Debe ingresar un precio valido")
		return precio

from django.forms.models import inlineformset_factory

DetalleCompraFormSet = inlineformset_factory(Compra, DetalleCompra, form=DetalleCompraForm, extra=4)
