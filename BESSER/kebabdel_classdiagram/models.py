from django.db import models

class Pesanan(models.Model):
    """
    Represents a pesanan in the system.
    """
    tanggal =  models.DateField()
    waktuPemesanan = None
    metodePengambilan =  models.CharField(max_length=255)
    status =  models.CharField(max_length=255)
    totalHarga =  models.FloatField()
    alamatpengiriman = models.ForeignKey(
        'AlamatPengiriman', related_name='pesanan', on_delete=models.SET_NULL, blank=True, null=True)
    koki = models.ForeignKey(
        'Koki', related_name='pesanan', on_delete=models.SET_NULL, blank=True, null=True)
    outlet = models.ForeignKey(
        'Outlet', related_name='pesanan', on_delete=models.PROTECT)
    pelanggan = models.ForeignKey(
        'Pelanggan', related_name='pesanan', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Pesanan"
        verbose_name_plural = "Pesanans"
    def __str__(self):
        """
        Returns a string representation of the pesanan
        """
        return str(self.tanggal)
class Pengguna(models.Model):
    """
    Represents a pengguna in the system.
    """
    nama =  models.CharField(max_length=255)
    email =  models.CharField(max_length=255)

    class Meta:
        verbose_name = "Pengguna"
        verbose_name_plural = "Penggunas"
    def __str__(self):
        """
        Returns a string representation of the pengguna
        """
        return str(self.nama)
class Pembayaran(models.Model):
    """
    Represents a pembayaran in the system.
    """
    totalBayar =  models.FloatField()
    statusPembayaran =  models.CharField(max_length=255)
    idTransaksiOVO =  models.CharField(max_length=255)
    pesanan = models.OneToOneField(
        'Pesanan', related_name='pembayaran', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Pembayaran"
        verbose_name_plural = "Pembayarans"
    def __str__(self):
        """
        Returns a string representation of the pembayaran
        """
        return str(self.totalBayar)
class Pelanggan(Pengguna):
    """
    Represents a pelanggan in the system.
    """
    nomorTelepon =  models.IntegerField()

    class Meta:
        verbose_name = "Pelanggan"
        verbose_name_plural = "Pelanggans"
    def __str__(self):
        """
        Returns a string representation of the pelanggan
        """
        return str(self.nomorTelepon)
class Outlet(models.Model):
    """
    Represents a outlet in the system.
    """
    nama =  models.CharField(max_length=255)
    alamat =  models.CharField(max_length=255)
    nomorTelepon =  models.IntegerField()

    class Meta:
        verbose_name = "Outlet"
        verbose_name_plural = "Outlets"
    def __str__(self):
        """
        Returns a string representation of the outlet
        """
        return str(self.nama)
class Menu(models.Model):
    """
    Represents a menu in the system.
    """
    nama =  models.CharField(max_length=255)
    deskripsi =  models.CharField(max_length=255)
    harga =  models.FloatField()
    outlet = models.ManyToManyField(
        'Outlet', related_name='menu', blank=True)

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
    def __str__(self):
        """
        Returns a string representation of the menu
        """
        return str(self.nama)
class Koki(Pengguna):
    """
    Represents a koki in the system.
    """
    outlet = models.ForeignKey(
        'Outlet', related_name='koki', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Koki"
        verbose_name_plural = "Kokis"
class KetersediaanMenu(models.Model):
    """
    Represents a ketersediaanMenu in the system.
    """
    tersedia =  models.BooleanField()

    class Meta:
        verbose_name = "KetersediaanMenu"
        verbose_name_plural = "KetersediaanMenus"
    def __str__(self):
        """
        Returns a string representation of the ketersediaanMenu
        """
        return str(self.tersedia)
class ItemPesanan(models.Model):
    """
    Represents a itemPesanan in the system.
    """
    jumlah =  models.IntegerField()
    hargaSatuan =  models.FloatField()
    catatan =  models.CharField(max_length=255)
    subtotal =  models.FloatField()
    menu = models.ForeignKey(
        'Menu', related_name='itempesanan', on_delete=models.PROTECT)
    pesanan = models.ForeignKey(
        'Pesanan', related_name='itempesanan', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "ItemPesanan"
        verbose_name_plural = "ItemPesanans"
    def __str__(self):
        """
        Returns a string representation of the itemPesanan
        """
        return str(self.jumlah)
class AlamatPengiriman(models.Model):
    """
    Represents a alamatPengiriman in the system.
    """
    label =  models.CharField(max_length=255)
    alamatLengkap =  models.CharField(max_length=255)
    pelanggan = models.ForeignKey(
        'Pelanggan', related_name='alamatpengiriman', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "AlamatPengiriman"
        verbose_name_plural = "AlamatPengirimans"
    def __str__(self):
        """
        Returns a string representation of the alamatPengiriman
        """
        return str(self.label)
