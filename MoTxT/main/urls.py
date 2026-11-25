"""
This code is generated using MoTxT,
checkout more about us on https://motxt.ppl.cs.ui.ac.id
"""

from django.urls import path
from .views import (
    landing_page,
    dashboard,
    create_pengguna,
    get_pengguna,
    edit_pengguna,
    delete_pengguna,create_koki,
    get_koki,
    edit_koki,
    delete_koki,create_outlet,
    get_outlet,
    edit_outlet,
    delete_outlet,create_menu,
    get_menu,
    edit_menu,
    delete_menu,create_item_pesanan,
    get_item_pesanan,
    edit_item_pesanan,
    delete_item_pesanan,create_pesanan,
    get_pesanan,
    edit_pesanan,
    delete_pesanan,create_pelanggan,
    get_pelanggan,
    edit_pelanggan,
    delete_pelanggan,create_alamat_pengiriman,
    get_alamat_pengiriman,
    edit_alamat_pengiriman,
    delete_alamat_pengiriman,create_pembayaran,
    get_pembayaran,
    edit_pembayaran,
    delete_pembayaran,create_ketersediaan_menu,
    get_ketersediaan_menu,
    edit_ketersediaan_menu,
    delete_ketersediaan_menu,
)

app_name = "main"

urlpatterns = [
    path('', landing_page , name="landing_page"),
    path('dashboard/', dashboard, name="dashboard"),
    # Path for Pengguna
    path('create-pengguna/', create_pengguna, name="create_pengguna"),
    path('get-all-pengguna/', get_pengguna, name="get_pengguna"),
    path('edit-pengguna/<int:id>/', edit_pengguna, name="edit_pengguna"),
    path('delete-pengguna/', delete_pengguna, name="delete_pengguna"),
    
    # Path for Koki
    path('create-koki/', create_koki, name="create_koki"),
    path('get-all-koki/', get_koki, name="get_koki"),
    path('edit-koki/<int:id>/', edit_koki, name="edit_koki"),
    path('delete-koki/', delete_koki, name="delete_koki"),
    
    # Path for Outlet
    path('create-outlet/', create_outlet, name="create_outlet"),
    path('get-all-outlet/', get_outlet, name="get_outlet"),
    path('edit-outlet/<int:id>/', edit_outlet, name="edit_outlet"),
    path('delete-outlet/', delete_outlet, name="delete_outlet"),
    
    # Path for Menu
    path('create-menu/', create_menu, name="create_menu"),
    path('get-all-menu/', get_menu, name="get_menu"),
    path('edit-menu/<int:id>/', edit_menu, name="edit_menu"),
    path('delete-menu/', delete_menu, name="delete_menu"),
    
    # Path for ItemPesanan
    path('create-item_pesanan/', create_item_pesanan, name="create_item_pesanan"),
    path('get-all-item_pesanan/', get_item_pesanan, name="get_item_pesanan"),
    path('edit-item_pesanan/<int:id>/', edit_item_pesanan, name="edit_item_pesanan"),
    path('delete-item_pesanan/', delete_item_pesanan, name="delete_item_pesanan"),
    
    # Path for Pesanan
    path('create-pesanan/', create_pesanan, name="create_pesanan"),
    path('get-all-pesanan/', get_pesanan, name="get_pesanan"),
    path('edit-pesanan/<int:id>/', edit_pesanan, name="edit_pesanan"),
    path('delete-pesanan/', delete_pesanan, name="delete_pesanan"),
    
    # Path for Pelanggan
    path('create-pelanggan/', create_pelanggan, name="create_pelanggan"),
    path('get-all-pelanggan/', get_pelanggan, name="get_pelanggan"),
    path('edit-pelanggan/<int:id>/', edit_pelanggan, name="edit_pelanggan"),
    path('delete-pelanggan/', delete_pelanggan, name="delete_pelanggan"),
    
    # Path for AlamatPengiriman
    path('create-alamat_pengiriman/', create_alamat_pengiriman, name="create_alamat_pengiriman"),
    path('get-all-alamat_pengiriman/', get_alamat_pengiriman, name="get_alamat_pengiriman"),
    path('edit-alamat_pengiriman/<int:id>/', edit_alamat_pengiriman, name="edit_alamat_pengiriman"),
    path('delete-alamat_pengiriman/', delete_alamat_pengiriman, name="delete_alamat_pengiriman"),
    
    # Path for Pembayaran
    path('create-pembayaran/', create_pembayaran, name="create_pembayaran"),
    path('get-all-pembayaran/', get_pembayaran, name="get_pembayaran"),
    path('edit-pembayaran/<int:id>/', edit_pembayaran, name="edit_pembayaran"),
    path('delete-pembayaran/', delete_pembayaran, name="delete_pembayaran"),
    
    # Path for KetersediaanMenu
    path('create-ketersediaan_menu/', create_ketersediaan_menu, name="create_ketersediaan_menu"),
    path('get-all-ketersediaan_menu/', get_ketersediaan_menu, name="get_ketersediaan_menu"),
    path('edit-ketersediaan_menu/<int:id>/', edit_ketersediaan_menu, name="edit_ketersediaan_menu"),
    path('delete-ketersediaan_menu/', delete_ketersediaan_menu, name="delete_ketersediaan_menu"),
    
]

