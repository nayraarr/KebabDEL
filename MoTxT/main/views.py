from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import *
from .models import *
from django.apps import apps
from datetime import date


def landing_page(request):

    model_info = {}
    model_info["pengguna"] = "Pengguna"
    model_info["koki"] = "Koki"
    model_info["outlet"] = "Outlet"
    model_info["menu"] = "Menu"
    model_info["item_pesanan"] = "Itempesanan"
    model_info["pesanan"] = "Pesanan"
    model_info["pelanggan"] = "Pelanggan"
    model_info["alamat_pengiriman"] = "Alamatpengiriman"
    model_info["pembayaran"] = "Pembayaran"
    model_info["ketersediaan_menu"] = "Ketersediaanmenu"
    

    return render(request, 'landing_page.html', {'model_info': model_info})

def dashboard(request):
    entity_cards = [
        {
            'label': 'Pengguna',
            'count': Pengguna.objects.count(),
            'list_url': 'main:get_pengguna',
            'create_url': 'main:create_pengguna',
            'fields': [field.name for field in Pengguna._meta.get_fields()],
        }
,
        {
            'label': 'Koki',
            'count': Koki.objects.count(),
            'list_url': 'main:get_koki',
            'create_url': 'main:create_koki',
            'fields': [field.name for field in Koki._meta.get_fields()],
        }
,
        {
            'label': 'Outlet',
            'count': Outlet.objects.count(),
            'list_url': 'main:get_outlet',
            'create_url': 'main:create_outlet',
            'fields': [field.name for field in Outlet._meta.get_fields()],
        }
,
        {
            'label': 'Menu',
            'count': Menu.objects.count(),
            'list_url': 'main:get_menu',
            'create_url': 'main:create_menu',
            'fields': [field.name for field in Menu._meta.get_fields()],
        }
,
        {
            'label': 'ItemPesanan',
            'count': ItemPesanan.objects.count(),
            'list_url': 'main:get_item_pesanan',
            'create_url': 'main:create_item_pesanan',
            'fields': [field.name for field in ItemPesanan._meta.get_fields()],
        }
,
        {
            'label': 'Pesanan',
            'count': Pesanan.objects.count(),
            'list_url': 'main:get_pesanan',
            'create_url': 'main:create_pesanan',
            'fields': [field.name for field in Pesanan._meta.get_fields()],
        }
,
        {
            'label': 'Pelanggan',
            'count': Pelanggan.objects.count(),
            'list_url': 'main:get_pelanggan',
            'create_url': 'main:create_pelanggan',
            'fields': [field.name for field in Pelanggan._meta.get_fields()],
        }
,
        {
            'label': 'AlamatPengiriman',
            'count': AlamatPengiriman.objects.count(),
            'list_url': 'main:get_alamat_pengiriman',
            'create_url': 'main:create_alamat_pengiriman',
            'fields': [field.name for field in AlamatPengiriman._meta.get_fields()],
        }
,
        {
            'label': 'Pembayaran',
            'count': Pembayaran.objects.count(),
            'list_url': 'main:get_pembayaran',
            'create_url': 'main:create_pembayaran',
            'fields': [field.name for field in Pembayaran._meta.get_fields()],
        }
,
        {
            'label': 'KetersediaanMenu',
            'count': KetersediaanMenu.objects.count(),
            'list_url': 'main:get_ketersediaan_menu',
            'create_url': 'main:create_ketersediaan_menu',
            'fields': [field.name for field in KetersediaanMenu._meta.get_fields()],
        }
    ]

    return render(request, 'dashboard.html', {
        'entity_cards': entity_cards,
    })
	
#-------------- CRUD methods for Class Pengguna ---------------
def create_pengguna(request):
    if request.method == 'POST':
        form = PenggunaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:get_pengguna')
    else:
        form = PenggunaForm()
    return render(request, 'create_pengguna.html', {'form': form})

def edit_pengguna(request, id):
    pengguna_obj = Pengguna.objects.get(pk=id)
    form = PenggunaForm(request.POST or None, instance=pengguna_obj)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:get_pengguna')

    return render(request, 'edit_pengguna.html', {'form': form})

def get_pengguna(request):
    penggunas = Pengguna.objects.all()
    
    all_fields = [field.name for field in Pengguna._meta.get_fields()]
    pengguna_data = []
    form = PenggunaForm()
    
    for pengguna in penggunas:
        pengguna_dict = {}
        for field_name in all_fields:
            try:
                field = Pengguna._meta.get_field(field_name)
                if field.is_relation and field.many_to_many:
                    related_objects = getattr(pengguna, field_name).all()
                    pengguna_dict[field_name] = ", ".join([str(obj) for obj in related_objects]) or "None"
                else:
                    pengguna_dict[field_name] = getattr(pengguna, field_name)
            except:
                pengguna_dict[field_name] = "N/A"
        pengguna_data.append((pengguna, pengguna_dict))
    
    return render(request, 'pengguna_list.html', {
        'pengguna_data': pengguna_data,
        'fields': all_fields,
        'form': form,
        
    })

def delete_pengguna(request):
    if request.method == 'POST':
        object_id = request.POST.get('object_id')

        if object_id is None:
            return JsonResponse({"error": "ID is required"}, status=400)

        obj = Pengguna.objects.get(pk=object_id)
        obj.delete()
        return redirect('main:get_pengguna')
    return JsonResponse({"error": "Invalid request method"}, status=405)


#-------------- end of Class Pengguna ----------------

#-------------- CRUD methods for Class Koki ---------------
def create_koki(request):
    if request.method == 'POST':
        form = KokiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:get_koki')
    else:
        form = KokiForm()
    return render(request, 'create_koki.html', {'form': form})

def edit_koki(request, id):
    koki_obj = Koki.objects.get(pk=id)
    form = KokiForm(request.POST or None, instance=koki_obj)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:get_koki')

    return render(request, 'edit_koki.html', {'form': form})

def get_koki(request):
    kokis = Koki.objects.all()
    
    all_fields = [field.name for field in Koki._meta.get_fields()]
    koki_data = []
    form = KokiForm()
    
    for koki in kokis:
        koki_dict = {}
        for field_name in all_fields:
            try:
                field = Koki._meta.get_field(field_name)
                if field.is_relation and field.many_to_many:
                    related_objects = getattr(koki, field_name).all()
                    koki_dict[field_name] = ", ".join([str(obj) for obj in related_objects]) or "None"
                else:
                    koki_dict[field_name] = getattr(koki, field_name)
            except:
                koki_dict[field_name] = "N/A"
        koki_data.append((koki, koki_dict))
    
    return render(request, 'koki_list.html', {
        'koki_data': koki_data,
        'fields': all_fields,
        'form': form,
        
    })

def delete_koki(request):
    if request.method == 'POST':
        object_id = request.POST.get('object_id')

        if object_id is None:
            return JsonResponse({"error": "ID is required"}, status=400)

        obj = Koki.objects.get(pk=object_id)
        obj.delete()
        return redirect('main:get_koki')
    return JsonResponse({"error": "Invalid request method"}, status=405)


#-------------- end of Class Koki ----------------

#-------------- CRUD methods for Class Outlet ---------------
def create_outlet(request):
    if request.method == 'POST':
        form = OutletForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:get_outlet')
    else:
        form = OutletForm()
    return render(request, 'create_outlet.html', {'form': form})

def edit_outlet(request, id):
    outlet_obj = Outlet.objects.get(pk=id)
    form = OutletForm(request.POST or None, instance=outlet_obj)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:get_outlet')

    return render(request, 'edit_outlet.html', {'form': form})

def get_outlet(request):
    outlets = Outlet.objects.all()
    
    all_fields = [field.name for field in Outlet._meta.get_fields()]
    outlet_data = []
    form = OutletForm()
    
    for outlet in outlets:
        outlet_dict = {}
        for field_name in all_fields:
            try:
                field = Outlet._meta.get_field(field_name)
                if field.is_relation and field.many_to_many:
                    related_objects = getattr(outlet, field_name).all()
                    outlet_dict[field_name] = ", ".join([str(obj) for obj in related_objects]) or "None"
                else:
                    outlet_dict[field_name] = getattr(outlet, field_name)
            except:
                outlet_dict[field_name] = "N/A"
        outlet_data.append((outlet, outlet_dict))
    
    return render(request, 'outlet_list.html', {
        'outlet_data': outlet_data,
        'fields': all_fields,
        'form': form,
        
    })

def delete_outlet(request):
    if request.method == 'POST':
        object_id = request.POST.get('object_id')

        if object_id is None:
            return JsonResponse({"error": "ID is required"}, status=400)

        obj = Outlet.objects.get(pk=object_id)
        obj.delete()
        return redirect('main:get_outlet')
    return JsonResponse({"error": "Invalid request method"}, status=405)


#-------------- end of Class Outlet ----------------

#-------------- CRUD methods for Class Menu ---------------
def create_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:get_menu')
    else:
        form = MenuForm()
    return render(request, 'create_menu.html', {'form': form})

def edit_menu(request, id):
    menu_obj = Menu.objects.get(pk=id)
    form = MenuForm(request.POST or None, instance=menu_obj)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:get_menu')

    return render(request, 'edit_menu.html', {'form': form})

def get_menu(request):
    menus = Menu.objects.all()
    
    all_fields = [field.name for field in Menu._meta.get_fields()]
    menu_data = []
    form = MenuForm()
    
    for menu in menus:
        menu_dict = {}
        for field_name in all_fields:
            try:
                field = Menu._meta.get_field(field_name)
                if field.is_relation and field.many_to_many:
                    related_objects = getattr(menu, field_name).all()
                    menu_dict[field_name] = ", ".join([str(obj) for obj in related_objects]) or "None"
                else:
                    menu_dict[field_name] = getattr(menu, field_name)
            except:
                menu_dict[field_name] = "N/A"
        menu_data.append((menu, menu_dict))
    
    return render(request, 'menu_list.html', {
        'menu_data': menu_data,
        'fields': all_fields,
        'form': form,
        
    })

def delete_menu(request):
    if request.method == 'POST':
        object_id = request.POST.get('object_id')

        if object_id is None:
            return JsonResponse({"error": "ID is required"}, status=400)

        obj = Menu.objects.get(pk=object_id)
        obj.delete()
        return redirect('main:get_menu')
    return JsonResponse({"error": "Invalid request method"}, status=405)


#-------------- end of Class Menu ----------------

#-------------- CRUD methods for Class ItemPesanan ---------------
def create_item_pesanan(request):
    if request.method == 'POST':
        form = ItemPesananForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:get_item_pesanan')
    else:
        form = ItemPesananForm()
    return render(request, 'create_itempesanan.html', {'form': form})

def edit_item_pesanan(request, id):
    item_pesanan_obj = ItemPesanan.objects.get(pk=id)
    form = ItemPesananForm(request.POST or None, instance=item_pesanan_obj)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:get_item_pesanan')

    return render(request, 'edit_itempesanan.html', {'form': form})

def get_item_pesanan(request):
    item_pesanans = ItemPesanan.objects.all()
    
    all_fields = [field.name for field in ItemPesanan._meta.get_fields()]
    item_pesanan_data = []
    form = ItemPesananForm()
    
    for item_pesanan in item_pesanans:
        item_pesanan_dict = {}
        for field_name in all_fields:
            try:
                field = ItemPesanan._meta.get_field(field_name)
                if field.is_relation and field.many_to_many:
                    related_objects = getattr(item_pesanan, field_name).all()
                    item_pesanan_dict[field_name] = ", ".join([str(obj) for obj in related_objects]) or "None"
                else:
                    item_pesanan_dict[field_name] = getattr(item_pesanan, field_name)
            except:
                item_pesanan_dict[field_name] = "N/A"
        item_pesanan_data.append((item_pesanan, item_pesanan_dict))
    
    return render(request, 'item_pesanan_list.html', {
        'item_pesanan_data': item_pesanan_data,
        'fields': all_fields,
        'form': form,
        
    })

def delete_item_pesanan(request):
    if request.method == 'POST':
        object_id = request.POST.get('object_id')

        if object_id is None:
            return JsonResponse({"error": "ID is required"}, status=400)

        obj = ItemPesanan.objects.get(pk=object_id)
        obj.delete()
        return redirect('main:get_item_pesanan')
    return JsonResponse({"error": "Invalid request method"}, status=405)


#-------------- end of Class ItemPesanan ----------------

#-------------- CRUD methods for Class Pesanan ---------------
def create_pesanan(request):
    if request.method == 'POST':
        form = PesananForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:get_pesanan')
    else:
        form = PesananForm()
    return render(request, 'create_pesanan.html', {'form': form})

def edit_pesanan(request, id):
    pesanan_obj = Pesanan.objects.get(pk=id)
    form = PesananForm(request.POST or None, instance=pesanan_obj)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:get_pesanan')

    return render(request, 'edit_pesanan.html', {'form': form})

def get_pesanan(request):
    pesanans = Pesanan.objects.all()
    
    all_fields = [field.name for field in Pesanan._meta.get_fields()]
    pesanan_data = []
    form = PesananForm()
    
    for pesanan in pesanans:
        pesanan_dict = {}
        for field_name in all_fields:
            try:
                field = Pesanan._meta.get_field(field_name)
                if field.is_relation and field.many_to_many:
                    related_objects = getattr(pesanan, field_name).all()
                    pesanan_dict[field_name] = ", ".join([str(obj) for obj in related_objects]) or "None"
                else:
                    pesanan_dict[field_name] = getattr(pesanan, field_name)
            except:
                pesanan_dict[field_name] = "N/A"
        pesanan_data.append((pesanan, pesanan_dict))
    
    return render(request, 'pesanan_list.html', {
        'pesanan_data': pesanan_data,
        'fields': all_fields,
        'form': form,
        
    })

def delete_pesanan(request):
    if request.method == 'POST':
        object_id = request.POST.get('object_id')

        if object_id is None:
            return JsonResponse({"error": "ID is required"}, status=400)

        obj = Pesanan.objects.get(pk=object_id)
        obj.delete()
        return redirect('main:get_pesanan')
    return JsonResponse({"error": "Invalid request method"}, status=405)


#-------------- end of Class Pesanan ----------------

#-------------- CRUD methods for Class Pelanggan ---------------
def create_pelanggan(request):
    if request.method == 'POST':
        form = PelangganForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:get_pelanggan')
    else:
        form = PelangganForm()
    return render(request, 'create_pelanggan.html', {'form': form})

def edit_pelanggan(request, id):
    pelanggan_obj = Pelanggan.objects.get(pk=id)
    form = PelangganForm(request.POST or None, instance=pelanggan_obj)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:get_pelanggan')

    return render(request, 'edit_pelanggan.html', {'form': form})

def get_pelanggan(request):
    pelanggans = Pelanggan.objects.all()
    
    all_fields = [field.name for field in Pelanggan._meta.get_fields()]
    pelanggan_data = []
    form = PelangganForm()
    
    for pelanggan in pelanggans:
        pelanggan_dict = {}
        for field_name in all_fields:
            try:
                field = Pelanggan._meta.get_field(field_name)
                if field.is_relation and field.many_to_many:
                    related_objects = getattr(pelanggan, field_name).all()
                    pelanggan_dict[field_name] = ", ".join([str(obj) for obj in related_objects]) or "None"
                else:
                    pelanggan_dict[field_name] = getattr(pelanggan, field_name)
            except:
                pelanggan_dict[field_name] = "N/A"
        pelanggan_data.append((pelanggan, pelanggan_dict))
    
    return render(request, 'pelanggan_list.html', {
        'pelanggan_data': pelanggan_data,
        'fields': all_fields,
        'form': form,
        
    })

def delete_pelanggan(request):
    if request.method == 'POST':
        object_id = request.POST.get('object_id')

        if object_id is None:
            return JsonResponse({"error": "ID is required"}, status=400)

        obj = Pelanggan.objects.get(pk=object_id)
        obj.delete()
        return redirect('main:get_pelanggan')
    return JsonResponse({"error": "Invalid request method"}, status=405)


#-------------- end of Class Pelanggan ----------------

#-------------- CRUD methods for Class AlamatPengiriman ---------------
def create_alamat_pengiriman(request):
    if request.method == 'POST':
        form = AlamatPengirimanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:get_alamat_pengiriman')
    else:
        form = AlamatPengirimanForm()
    return render(request, 'create_alamatpengiriman.html', {'form': form})

def edit_alamat_pengiriman(request, id):
    alamat_pengiriman_obj = AlamatPengiriman.objects.get(pk=id)
    form = AlamatPengirimanForm(request.POST or None, instance=alamat_pengiriman_obj)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:get_alamat_pengiriman')

    return render(request, 'edit_alamatpengiriman.html', {'form': form})

def get_alamat_pengiriman(request):
    alamat_pengirimans = AlamatPengiriman.objects.all()
    
    all_fields = [field.name for field in AlamatPengiriman._meta.get_fields()]
    alamat_pengiriman_data = []
    form = AlamatPengirimanForm()
    
    for alamat_pengiriman in alamat_pengirimans:
        alamat_pengiriman_dict = {}
        for field_name in all_fields:
            try:
                field = AlamatPengiriman._meta.get_field(field_name)
                if field.is_relation and field.many_to_many:
                    related_objects = getattr(alamat_pengiriman, field_name).all()
                    alamat_pengiriman_dict[field_name] = ", ".join([str(obj) for obj in related_objects]) or "None"
                else:
                    alamat_pengiriman_dict[field_name] = getattr(alamat_pengiriman, field_name)
            except:
                alamat_pengiriman_dict[field_name] = "N/A"
        alamat_pengiriman_data.append((alamat_pengiriman, alamat_pengiriman_dict))
    
    return render(request, 'alamat_pengiriman_list.html', {
        'alamat_pengiriman_data': alamat_pengiriman_data,
        'fields': all_fields,
        'form': form,
        
    })

def delete_alamat_pengiriman(request):
    if request.method == 'POST':
        object_id = request.POST.get('object_id')

        if object_id is None:
            return JsonResponse({"error": "ID is required"}, status=400)

        obj = AlamatPengiriman.objects.get(pk=object_id)
        obj.delete()
        return redirect('main:get_alamat_pengiriman')
    return JsonResponse({"error": "Invalid request method"}, status=405)


#-------------- end of Class AlamatPengiriman ----------------

#-------------- CRUD methods for Class Pembayaran ---------------
def create_pembayaran(request):
    if request.method == 'POST':
        form = PembayaranForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:get_pembayaran')
    else:
        form = PembayaranForm()
    return render(request, 'create_pembayaran.html', {'form': form})

def edit_pembayaran(request, id):
    pembayaran_obj = Pembayaran.objects.get(pk=id)
    form = PembayaranForm(request.POST or None, instance=pembayaran_obj)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:get_pembayaran')

    return render(request, 'edit_pembayaran.html', {'form': form})

def get_pembayaran(request):
    pembayarans = Pembayaran.objects.all()
    
    all_fields = [field.name for field in Pembayaran._meta.get_fields()]
    pembayaran_data = []
    form = PembayaranForm()
    
    for pembayaran in pembayarans:
        pembayaran_dict = {}
        for field_name in all_fields:
            try:
                field = Pembayaran._meta.get_field(field_name)
                if field.is_relation and field.many_to_many:
                    related_objects = getattr(pembayaran, field_name).all()
                    pembayaran_dict[field_name] = ", ".join([str(obj) for obj in related_objects]) or "None"
                else:
                    pembayaran_dict[field_name] = getattr(pembayaran, field_name)
            except:
                pembayaran_dict[field_name] = "N/A"
        pembayaran_data.append((pembayaran, pembayaran_dict))
    
    return render(request, 'pembayaran_list.html', {
        'pembayaran_data': pembayaran_data,
        'fields': all_fields,
        'form': form,
        
    })

def delete_pembayaran(request):
    if request.method == 'POST':
        object_id = request.POST.get('object_id')

        if object_id is None:
            return JsonResponse({"error": "ID is required"}, status=400)

        obj = Pembayaran.objects.get(pk=object_id)
        obj.delete()
        return redirect('main:get_pembayaran')
    return JsonResponse({"error": "Invalid request method"}, status=405)


#-------------- end of Class Pembayaran ----------------

#-------------- CRUD methods for Class KetersediaanMenu ---------------
def create_ketersediaan_menu(request):
    if request.method == 'POST':
        form = KetersediaanMenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:get_ketersediaan_menu')
    else:
        form = KetersediaanMenuForm()
    return render(request, 'create_ketersediaanmenu.html', {'form': form})

def edit_ketersediaan_menu(request, id):
    ketersediaan_menu_obj = KetersediaanMenu.objects.get(pk=id)
    form = KetersediaanMenuForm(request.POST or None, instance=ketersediaan_menu_obj)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:get_ketersediaan_menu')

    return render(request, 'edit_ketersediaanmenu.html', {'form': form})

def get_ketersediaan_menu(request):
    ketersediaan_menus = KetersediaanMenu.objects.all()
    
    all_fields = [field.name for field in KetersediaanMenu._meta.get_fields()]
    ketersediaan_menu_data = []
    form = KetersediaanMenuForm()
    
    for ketersediaan_menu in ketersediaan_menus:
        ketersediaan_menu_dict = {}
        for field_name in all_fields:
            try:
                field = KetersediaanMenu._meta.get_field(field_name)
                if field.is_relation and field.many_to_many:
                    related_objects = getattr(ketersediaan_menu, field_name).all()
                    ketersediaan_menu_dict[field_name] = ", ".join([str(obj) for obj in related_objects]) or "None"
                else:
                    ketersediaan_menu_dict[field_name] = getattr(ketersediaan_menu, field_name)
            except:
                ketersediaan_menu_dict[field_name] = "N/A"
        ketersediaan_menu_data.append((ketersediaan_menu, ketersediaan_menu_dict))
    
    return render(request, 'ketersediaan_menu_list.html', {
        'ketersediaan_menu_data': ketersediaan_menu_data,
        'fields': all_fields,
        'form': form,
        
    })

def delete_ketersediaan_menu(request):
    if request.method == 'POST':
        object_id = request.POST.get('object_id')

        if object_id is None:
            return JsonResponse({"error": "ID is required"}, status=400)

        obj = KetersediaanMenu.objects.get(pk=object_id)
        obj.delete()
        return redirect('main:get_ketersediaan_menu')
    return JsonResponse({"error": "Invalid request method"}, status=405)


#-------------- end of Class KetersediaanMenu ----------------


