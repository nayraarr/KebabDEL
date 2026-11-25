from django import forms
from django.utils.safestring import SafeString
from .models import *

class PenggunaForm(forms.ModelForm):
    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='form-group'>"))

    class Meta:
        model = Pengguna
        fields = ('__all__')

class KokiForm(forms.ModelForm):
    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='form-group'>"))

    class Meta:
        model = Koki
        fields = ('__all__')

class OutletForm(forms.ModelForm):
    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='form-group'>"))

    class Meta:
        model = Outlet
        fields = ('__all__')

class MenuForm(forms.ModelForm):
    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='form-group'>"))

    class Meta:
        model = Menu
        fields = ('__all__')

class ItemPesananForm(forms.ModelForm):
    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='form-group'>"))

    class Meta:
        model = ItemPesanan
        fields = ('__all__')

class PesananForm(forms.ModelForm):
    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='form-group'>"))

    class Meta:
        model = Pesanan
        fields = ('__all__')

class PelangganForm(forms.ModelForm):
    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='form-group'>"))

    class Meta:
        model = Pelanggan
        fields = ('__all__')

class AlamatPengirimanForm(forms.ModelForm):
    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='form-group'>"))

    class Meta:
        model = AlamatPengiriman
        fields = ('__all__')

class PembayaranForm(forms.ModelForm):
    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='form-group'>"))

    class Meta:
        model = Pembayaran
        fields = ('__all__')

class KetersediaanMenuForm(forms.ModelForm):
    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='form-group'>"))

    class Meta:
        model = KetersediaanMenu
        fields = ('__all__')
