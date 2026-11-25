# Experiment Low Code Tools: BESSER vs MoTxT

Perbandingan dua low code tools yang men-generate project **Django** dari UML class diagram yang sama (sistem pemesanan kebab, 10 class).

| Folder | Tool | Editor model | Hasil |
| --- | --- | --- | --- |
| [`BESSER/`](BESSER) | [BESSER](https://github.com/BESSER-PEARL/BESSER) 8.10.1 | Web interface (Low Code) | Models + Django Admin (Jazzmin) |
| [`MoTxT/`](MoTxT) | [MoTxT](https://motxt.ppl.cs.ui.ac.id) | BigUML editor di VS Code | Models + CRUD views, forms, templates (Tailwind) |

Class pada model: `Pengguna`, `Pelanggan`, `Koki`, `Outlet`, `Menu`, `KetersediaanMenu`, `Pesanan`, `ItemPesanan`, `AlamatPengiriman`, `Pembayaran`.

## Cara Menjalankan

Butuh Python 3.10+. Command untuk Windows (PowerShell).

### BESSER

```powershell
cd BESSER
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Buka http://127.0.0.1:8000/admin/ lalu login dengan akun superuser.

### MoTxT

```powershell
cd MoTxT
.\run.bat
```

`run.bat` otomatis membuat venv, install dependencies, migrate, dan menjalankan server. Linux/macOS: `./run.sh`.

Buka http://127.0.0.1:8000/ (landing page) dan http://127.0.0.1:8000/dashboard/.

> Untuk menjalankan keduanya bersamaan, pakai port berbeda, misalnya `python manage.py runserver 8001`.

## Perbedaan Utama

| Aspek | BESSER | MoTxT |
| --- | --- | --- |
| Langsung jalan setelah generate | Ya | Tidak, perlu 4 perbaikan manual |
| Views / UI | Tidak ada, hanya Django Admin | CRUD lengkap per entity + landing page + dashboard |
| Penamaan field | camelCase (`totalHarga`) | snake_case + akhiran FK (`total_harga`, `outletFK`) |
| Multiplicity 0..1 | Dihormati (`null=True`) | Diabaikan, semua FK wajib |
| `on_delete` | `PROTECT` / `SET_NULL` | `RESTRICT` |
| `__str__`, `Meta`, admin register | Ada | Tidak ada |
| Atribut bertipe waktu | Hilang (`None`) | `TextField` |
| Login | Wajib (admin) | Tidak ada |

## Perbaikan pada MoTxT

Kode asli hasil generate MoTxT ada di commit pertama MoTxT. Perbaikannya ada di commit terpisah, jadi before/after bisa dilihat di riwayat commit.

1. **`NameError: name 'Outlet' is not defined`**: class direferensikan sebelum didefinisikan. Referensi relasi diubah menjadi string (`'Outlet'`).
2. **`fields.E302/E303`**: relasi 1..1 Pesanan–Pembayaran dibuat di dua sisi. Field `Pesanan.pembayaran` dihapus.
3. **`fields.E331/E340`**: association class `KetersediaanMenu` dibuat dua kali dan M2M dibuat di dua sisi. Digabung menjadi satu tabel penghubung, M2M hanya di `Outlet` (`blank=True`).
4. **`TemplateDoesNotExist`**: nama template di `views.py` tidak cocok dengan nama file. Nama disesuaikan dan `edit_koki.html` ditambahkan.
