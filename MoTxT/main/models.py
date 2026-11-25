from django.db import models
from datetime import date


class Pengguna(models.Model):
    nama = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
    pass

class Koki(Pengguna):
    outletFK = models.ForeignKey(Outlet, on_delete=models.RESTRICT)
    
    
    pass

class Outlet(models.Model):
    nama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    nomor_telepon = models.IntegerField()
    list_of_Menu = models.ManyToManyField(Menu, through='KetersediaanMenu')
    
    
    pass

class Menu(models.Model):
    nama = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255)
    harga = models.FloatField()
    list_of_Outlet = models.ManyToManyField(Outlet, through='KetersediaanMenu')
    
    
    pass

class ItemPesanan(models.Model):
    jumlah = models.IntegerField()
    harga_satuan = models.FloatField()
    catatan = models.CharField(max_length=255)
    subtotal = models.FloatField()
    menuFK = models.ForeignKey(Menu, on_delete=models.RESTRICT)
    
    pesananFK = models.ForeignKey(Pesanan, on_delete=models.RESTRICT)
    
    
    pass

class Pesanan(models.Model):
    tanggal = models.DateField(default=date.today, null=True, blank=True)
    waktu_pemesanan = models.TextField()
    metode_pengambilan = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    total_harga = models.FloatField()
    outletFK = models.ForeignKey(Outlet, on_delete=models.RESTRICT)
    
    kokiFK = models.ForeignKey(Koki, on_delete=models.RESTRICT)
    
    pelangganFK = models.ForeignKey(Pelanggan, on_delete=models.RESTRICT)
    
    alamatpengirimanFK = models.ForeignKey(AlamatPengiriman, on_delete=models.RESTRICT)
    
    pembayaran = models.OneToOneField(Pembayaran, on_delete=models.RESTRICT)
    
    
    pass

class Pelanggan(Pengguna):
    nomor_telepon = models.IntegerField()
    
    pass

class AlamatPengiriman(models.Model):
    label = models.CharField(max_length=255)
    alamat_lengkap = models.CharField(max_length=255)
    pelangganFK = models.ForeignKey(Pelanggan, on_delete=models.RESTRICT)
    
    
    pass

class Pembayaran(models.Model):
    total_bayar = models.FloatField()
    status_pembayaran = models.CharField(max_length=255)
    id_transaksi_ovo = models.CharField(max_length=255)
    pesanan = models.OneToOneField(Pesanan, on_delete=models.RESTRICT)
    
    
    pass

class KetersediaanMenu(models.Model):
    tersedia = models.BooleanField(default=False)
    
    pass
class KetersediaanMenu(models.Model):
    outlet = models.ForeignKey(Outlet, on_delete=models.RESTRICT)
    menu = models.ForeignKey(Menu, on_delete=models.RESTRICT)
    pass

