from django.db import models
from datetime import date


class Pengguna(models.Model):
    nama = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class Koki(Pengguna):
    outletFK = models.ForeignKey('Outlet', on_delete=models.RESTRICT)

    def __str__(self):
        return self.nama

class Outlet(models.Model):
    nama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    nomor_telepon = models.IntegerField()
    list_of_Menu = models.ManyToManyField('Menu', through='KetersediaanMenu', blank=True)

    def __str__(self):
        return self.nama

class Menu(models.Model):
    nama = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255)
    harga = models.FloatField()

    def __str__(self):
        return self.nama

class ItemPesanan(models.Model):
    jumlah = models.IntegerField()
    harga_satuan = models.FloatField()
    catatan = models.CharField(max_length=255)
    subtotal = models.FloatField()
    menuFK = models.ForeignKey('Menu', on_delete=models.RESTRICT)
    pesananFK = models.ForeignKey('Pesanan', on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.jumlah}x {self.menuFK}"

class Pesanan(models.Model):
    tanggal = models.DateField(default=date.today, null=True, blank=True)
    waktu_pemesanan = models.TextField()
    metode_pengambilan = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    total_harga = models.FloatField()
    outletFK = models.ForeignKey('Outlet', on_delete=models.RESTRICT)
    kokiFK = models.ForeignKey('Koki', on_delete=models.RESTRICT)
    pelangganFK = models.ForeignKey('Pelanggan', on_delete=models.RESTRICT)
    alamatpengirimanFK = models.ForeignKey('AlamatPengiriman', on_delete=models.RESTRICT)

    def __str__(self):
        return f"Pesanan #{self.pk} - {self.pelangganFK} ({self.tanggal})"

class Pelanggan(Pengguna):
    nomor_telepon = models.IntegerField()

    def __str__(self):
        return self.nama

class AlamatPengiriman(models.Model):
    label = models.CharField(max_length=255)
    alamat_lengkap = models.CharField(max_length=255)
    pelangganFK = models.ForeignKey('Pelanggan', on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.label} - {self.pelangganFK}"

class Pembayaran(models.Model):
    total_bayar = models.FloatField()
    status_pembayaran = models.CharField(max_length=255)
    id_transaksi_ovo = models.CharField(max_length=255)
    pesanan = models.OneToOneField('Pesanan', on_delete=models.RESTRICT)

    def __str__(self):
        return self.id_transaksi_ovo

class KetersediaanMenu(models.Model):
    tersedia = models.BooleanField(default=False)
    outlet = models.ForeignKey('Outlet', on_delete=models.RESTRICT)
    menu = models.ForeignKey('Menu', on_delete=models.RESTRICT)

    def __str__(self):
        status = "Tersedia" if self.tersedia else "Tidak tersedia"
        return f"{self.menu} @ {self.outlet} ({status})"
