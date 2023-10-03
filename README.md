TUGAS 2
A   
    1. Membuat direktori lokal dan repository kemudian meng-sinkronkan keduanya. Lalu menginstall env pada direktori lokal dan menginstall keperluan django yang ditulis dalam requirements.txt. Setelah itu mulai proyek django dengan perintah "django-admin startproject <nama proyek> ." Kemudian menginstall package main dan mulai menulis models, views, dan html serta memodifikasi settings. File django yang berhasil dibuat dapat di run dengan manage.py runserver
    2. Membuat aplikasi main dengan fitur python dengan perintah "python manage.py startapp main" pada terminal direktori lokal. setelahnya, akan ada direktori main dengan kelengkapannya.
    3. Routing dilakukan dengan cara menambahkan file urls.py yang berisi method path dari django.url yang ditempatkan dalam direktori main yang telah dibuat
    4. Deploy dengan Adaptable cukup mudah dilakukan. Cukup buka web Adaptable.io, Sign in pada akun github yang telah berisi direktori aplikasi yang kita buat, dan mulai deploy app. Disediakan berbagai pengaturan tentang bahasa apa yang kita gunakan dan lain lain. Setelah menunggu waktu deploy selesai, Adaptable akan memberi link url yang mengarah pada html yang telah kita buat.
    5. Menulis README.md cukup mudah. Pergi ke repostory kita lalu pencet tombol "Add File" dengan penamaan README format .md dan menuliskan jawaban setiap soal pada tugas 2 PBP
B.
    Bagan akan saya upload berupa file foto pada repository
C.
    Mengapa kita harus menggunakan virtual environment? agar mencegah terjadinya hal yang tidak diinginkan. Seperti: menghindari perbedaan versi paket python pada aplikasi yang akan kita buat, tidak merusak environment yang ada pada komputer kita, memastikan proyek yang kita buat berjalan sesuai dengan lingkungannya semisal terdapat perbedaan versi paket python pada komputer kita, menghindari konflik perbedaan versi python pada django dan komputer kita, dan lain sebagainya
D. 
    MVC, MVT, dan MVV adalah arsitektur perangkat lunak yang berfungsi untuk mengembangkan aplikasi dalam memisahkan tata cara pembuatan aplikasi berdasarkan logika dan representasi data.
    MVC adalah Model View Controler, artinya arsitektur program tersebut terbagi menjadi 3, yaitu model, view, dan controler. Model adalah komponen yang berperan sebagai badan dari variabel program tersebut. View adalah bagian yang berfungsi untuk mengatur tampilan data kepada penggunanya. Controler bertindak sebagai perantara diantara keduanya
    MVT adalah Model View Template. Sama seperti MVC, Model disini berperan sebagai otak logika yang mengatur data. View juga mengatur tampilan data. Sedangkan Template adalah bagian yang hampir sama dengan view, namun fokus pada tampilan bagian statis
    MVVM adalah Model View ViewModel. Model dan View sama seperti kedua arsitektur yang lain. Sedangkan ViewModel berperan untuk mengambil data dari Model untuk ditampilkan dengan View.
    Ketiganya memiliki perbedaan utama terkait kefokusan. MVC sering digunakan pada pengembangan aplikasi dekstop dan web biasa karena Controller dapat mengatur aliran aplikasi secara aktif. MVT lebih sering digunakan pada django dalam kerangka web python, sebagian besar logika diatur dalam Template. Sedangkan MVVM kerap digunakan dalam pengembangan aplikasi dengan User Interface yang kompleks seperti aplikasi mobile karena ViewModel memiliki peran penting dalam memisahkan logika dalam Models dan tampilan dalam View
    Ketiganya sama-sama bertujuan untuk memisahkan tata cara dalam pengembangan aplkikasi agar lebih mudah dan praktis, tergantung dengan kebutuhan dalam pengembangan aplikasi tersebut agar lebih mudah dikelola, dioptimalkan dan diperbarui secara berkala.

TUGAS 3

- 1. Dalam Django, perbedaan antara form POST dan form GET terletak pada cara data dikirim dari halaman web ke server. Saat menggunakan metode POST, data formulir dikemas dan dikirimkan secara tersembunyi dalam body permintaan HTTP, sehingga lebih aman untuk data sensitif. Di sisi lain, metode GET mengirimkan data sebagai bagian dari URL dalam parameter query string, yang membuatnya terlihat dalam URL dan cocok untuk permintaan yang tidak mengubah data di server. POST digunakan untuk mengirim data yang ingin dimasukkan atau dimodifikasi di server, sementara GET digunakan untuk mengambil data dari server. Dengan pemahaman ini, pengembang dapat memilih metode yang sesuai sesuai dengan kebutuhan keamanan dan tujuan aplikasi web mereka.
- 2. XML (Extensible Markup Language), JSON (JavaScript Object Notation), dan HTML (Hypertext Markup Language) adalah format yang berbeda yang digunakan untuk pengiriman data dalam konteks berbeda.

XML adalah format yang serbaguna dan dapat digunakan untuk menggambarkan struktur data yang kompleks dengan sangat baik. Ini terdiri dari elemen-elemen yang dikelilingi oleh tag, dan atribut-atribut dapat ditambahkan untuk memberikan informasi tambahan tentang elemen-elemen tersebut. XML sangat baik digunakan untuk pertukaran data antara aplikasi yang berbeda atau penyimpanan data yang kompleks. Namun, XML memiliki overhead yang cukup besar karena tag-tagnya dan oleh karena itu mungkin tidak efisien untuk data yang sangat besar.

JSON, di sisi lain, adalah format ringkas yang digunakan untuk mengirimkan dan menyimpan data. Ini berbasis pada sintaks objek JavaScript dan terdiri dari pasangan kunci-nilai yang membuatnya mudah dipahami oleh manusia dan mudah diproses oleh komputer. JSON sangat umum digunakan dalam aplikasi web modern dan API (Application Programming Interface) untuk mentransfer data antara server dan klien. Ini lebih efisien daripada XML karena memiliki payload yang lebih ringan.

HTML, seperti XML, juga berisi struktur dengan elemen-elemen yang dikelilingi oleh tag, tetapi HTML memiliki tujuan yang berbeda. HTML digunakan untuk menggambarkan struktur konten pada halaman web, seperti teks, gambar, tautan, dan elemen-elemen lainnya. Ini adalah bahasa markup yang digunakan untuk membuat tampilan visual dalam web browser dan tidak digunakan untuk pertukaran data mentah antara aplikasi.

Jadi, perbedaan utama antara ketiganya adalah dalam tujuan penggunaannya: XML digunakan untuk merepresentasikan data kompleks, JSON digunakan untuk pertukaran data ringkas, dan HTML digunakan untuk membuat tampilan halaman web. Pilihan antara ketiganya tergantung pada kebutuhan aplikasi dan konteks penggunaannya.
- 3. JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena kesederhanaan dan fleksibilitasnya. Format JSON yang ringkas dan mudah dibaca oleh manusia menjadikannya pilihan yang nyaman untuk mengirim dan menerima data dalam format yang intuitif. Selain itu, JSON memiliki payload yang ringan, mengurangi penggunaan bandwidth dan mempercepat respons aplikasi. Kemampuannya untuk mendukung struktur data yang fleksibel memungkinkan representasi data yang kompleks, seperti objek bersarang dan larik, yang sering ditemukan dalam aplikasi modern. Kecocokannya dengan berbagai bahasa pemrograman dan dukungan yang luas dalam browser web menjadikan JSON sebagai stKitar de facto dalam pertukaran data antar aplikasi web, terutama dalam konteks pengembangan API RESTful yang semakin umum digunakan.
- 4. - Pertama, buat file forms.py yang menjadi badan dari input pengguna nantinya. File ini berisi tentang variabel model yang akan dimintakan input kepada pengguna dan sesuai dengan model yang ada pada models.py. Kemudian pada bagian view di file views.py tambahkan fungsi baru untuk membuat sebuah produk dari input, disini saya menggunakan nama fungsi create_product. Kemudian ubah bagian show_main di views.py agar menyimpan setiap produk yang ditambahkan. Setelah itu buat file create_product.html sebagai tampilan input product dengan tombol yang akan mengarahkan pada kolom form input produk yang nantinya ketika produk ditambahkan akan kembali ke layar utama dengan tampilan produk yang telah di input. Lalu lakukan routing pada create product dengan menambahkan import dan path pada urls.py
- Pertama, modifikasi file views.py dan tambahkan import: from django.http import HttpResponse
from django.core import serializers. Kemudian tambahkan 4 fungsi baru untuk XML, JSON, XML by ID, dan JSON by ID dengan fungsi: 
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
- Untuk melakukan routing fungsi-fungsi tersebut tinggal tambahkan import baru pada file urls.py yang ada pada direktori main. Lalu tambahkan path baru untuk memanggil fungsi pada url dengan cara menambahkan kode path:
path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),

<br><br>
***Tugas 4***

 `UserCreationForm` adalah bagian dari framework web Python yang populer yang disebut Django. Django adalah kerangka kerja pengembangan web yang kuat dan fleksibel yang digunakan untuk membangun situs web dan aplikasi web. `UserCreationForm` adalah salah satu dari banyak formulir bawaan yang disediakan oleh Django untuk memudahkan pengembangan aplikasi web yang melibatkan otentikasi pengguna.

`UserCreationForm` secara khusus digunakan untuk membuat formulir pendaftaran pengguna. Ini memungkinkan pengguna untuk membuat akun baru dengan mengisi informasi seperti username, password, dan alamat email. Kelebihan dan kekurangan dari `UserCreationForm` adalah sebagai berikut:

**Kelebihan:**

1. **Mudah Digunakan:** `UserCreationForm` adalah bagian dari Django's built-in forms, yang membuatnya mudah digunakan dan menghemat waktu dalam pengembangan aplikasi web yang melibatkan otentikasi pengguna. Kita hanya perlu mengimpor dan menggunakannya dalam proyek Kita.

2. **Validasi Otomatis:** Formulir ini dilengkapi dengan validasi otomatis untuk memeriksa apakah input yang dimasukkan oleh pengguna memenuhi persyaratan tertentu, seperti panjang kata sandi minimal, uniknya username, dan validitas alamat email.

3. **Dukungan untuk Customization:** Kita dapat dengan mudah menyesuaikan tampilan dan perilaku formulir ini sesuai dengan kebutuhan proyek Kita. Kita dapat menambahkan bidang tambahan atau mengubah pesan kesalahan sesuai kebijakan aplikasi Kita.

4. **Integrasi dengan Model Pengguna Django:** `UserCreationForm` terintegrasi dengan model pengguna bawaan Django, yang berarti Kita dapat dengan mudah menghubungkan formulir ini dengan model pengguna dan menyimpan data pengguna yang terdaftar dalam database.

**Kekurangan:**

1. **Tidak Mendukung Opsi Lainnya:** `UserCreationForm` dirancang untuk kasus pengguna yang sangat sederhana. Jika Kita memerlukan opsi pendaftaran yang lebih kompleks atau memiliki persyaratan yang berbeda, Kita mungkin perlu menyesuaikan formulir ini atau bahkan membuat formulir pendaftaran kustom Kita sendiri.

2. **Terbatas dalam Desain:** Tampilan bawaan dari `UserCreationForm` mungkin terlalu sederhana dan perlu disesuaikan jika Kita ingin tampilan pendaftaran yang lebih kompleks atau menarik.

3. **Keamanan Tambahan Mungkin Diperlukan:** Meskipun `UserCreationForm` menyediakan validasi otomatis, keamanan tambahan seperti proteksi terhadap serangan CSRF dan XSS (Cross-Site Scripting) masih perlu ditambahkan secara terpisah dalam aplikasi Kita.

Secara keseluruhan, `UserCreationForm` adalah alat yang berguna untuk memulai dengan cepat dalam mengembangkan fitur pendaftaran pengguna dalam aplikasi web Django. Namun, untuk aplikasi yang lebih kompleks atau dengan persyaratan khusus, Kita mungkin perlu melakukan penyesuaian tambahan atau bahkan membuat formulir pendaftaran kustom Kita sendiri.

<br><br>
Autentikasi dan otorisasi adalah dua konsep yang sangat penting dalam konteks pengembangan aplikasi web, termasuk dalam kerangka kerja Django. Keduanya memiliki perbedaan yang signifikan dan memiliki peran yang berbeda dalam menjaga keamanan dan akses kontrol dalam sebuah aplikasi. Berikut adalah perbedaan antara autentikasi dan otorisasi, serta mengapa keduanya penting:

1. **Autentikasi:**
   - **Definisi:** Autentikasi adalah proses verifikasi identitas pengguna. Ini adalah tahap di mana pengguna membuktikan bahwa mereka adalah orang yang mereka klaim dengan cara yang aman, seperti dengan menggunakan kata sandi atau mekanisme otentikasi lainnya.
   - **Tujuan:** Autentikasi digunakan untuk memastikan bahwa pengguna yang mencoba mengakses aplikasi adalah mereka yang mengklaim diri mereka dan memiliki hak akses ke dalam sistem.
   - **Contoh dalam Django:** Django memiliki sistem autentikasi bawaan yang memungkinkan pengguna untuk mendaftar, masuk, dan mengelola akun mereka dengan aman. Ini melibatkan penggunaan kata sandi yang dihash dan token otentikasi untuk memverifikasi identitas pengguna.

2. **Otorisasi:**
   - **Definisi:** Otorisasi adalah proses menentukan apa yang diizinkan oleh pengguna yang sudah diotentikasi. Ini menentukan hak akses apa yang dimiliki pengguna terhadap sumber daya atau fitur tertentu dalam aplikasi.
   - **Tujuan:** Otorisasi digunakan untuk mengontrol apa yang dapat dilihat, dibaca, ditulis, atau diubah oleh pengguna yang sudah diotentikasi dalam aplikasi. Ini membantu menjaga privasi dan keamanan data.
   - **Contoh dalam Django:** Django memiliki sistem otorisasi yang memungkinkan pengembang untuk menentukan peran dan izin pengguna dalam aplikasi. Ini melibatkan penggunaan decorator dan mixin yang membatasi akses ke tampilan atau sumber daya tertentu berdasarkan peran pengguna.

Mengapa Keduanya Penting?
- **Keamanan Data:** Autentikasi dan otorisasi bekerja bersama-sama untuk menjaga keamanan data dalam aplikasi. Autentikasi memastikan hanya pengguna yang sah yang memiliki akses ke sistem, sedangkan otorisasi mengontrol akses pengguna ke data dan fitur tertentu.

- **Privasi Pengguna:** Autentikasi memungkinkan pengguna untuk mengakses akun mereka sendiri dengan aman, sementara otorisasi memastikan bahwa pengguna tidak dapat mengakses data atau fungsi yang bukan haknya.

- **Pengelolaan Hak Akses:** Otorisasi memungkinkan pengembang untuk mengelola peran dan izin pengguna dalam aplikasi dengan fleksibilitas. Ini memungkinkan untuk membuat sistem yang lebih terstruktur dan mengatur tingkat akses yang berbeda untuk berbagai peran pengguna.

- **Kepatuhan Regulasi:** Dalam beberapa kasus, seperti aplikasi yang berurusan dengan data sensitif atau informasi pribadi, autentikasi dan otorisasi diperlukan untuk mematuhi peraturan dan kebijakan keamanan yang berlaku.

Dalam ringkasan, autentikasi dan otorisasi adalah elemen penting dalam pengembangan aplikasi web yang membantu menjaga keamanan, privasi, dan pengelolaan akses pengguna. Keduanya harus diterapkan dengan benar dalam setiap aplikasi untuk menjaga integritas dan keamanannya.

<br><br>
Cookies adalah sejumlah kecil data yang disimpan oleh server web di komputer pengguna melalui browser web mereka. Data ini kemudian dapat diakses dan digunakan oleh server untuk berbagai tujuan saat pengguna mengunjungi situs web atau aplikasi web tertentu. Dalam konteks aplikasi web, cookies digunakan untuk mengelola data sesi pengguna, menyimpan preferensi pengguna, melacak riwayat penjelajahan, dan sebagainya.

Django, sebagai kerangka kerja pengembangan web Python, memiliki dukungan bawaan untuk mengelola cookies dan sesi pengguna. Berikut adalah cara Django menggunakan cookies untuk mengelola data sesi pengguna:

1. **Penyimpanan Data Sesi Pengguna:**
   - Django dapat menggunakan cookies untuk menyimpan data sesi pengguna. Data ini dapat mencakup informasi seperti ID sesi, preferensi pengguna, status masuk, dan lain-lain.
   - Data sesi pengguna disimpan di server Django, dan hanya ID sesi yang disimpan dalam cookie pengguna. Ini membantu menjaga keamanan data pengguna, karena data sebenarnya tidak ada di komputer pengguna.

2. **Middleware Django:**
   - Django menggunakan middleware untuk mengelola cookies dan sesi pengguna. Middleware adalah lapisan perantara yang dapat memodifikasi permintaan dan respons sebelum dan setelah mencapai aplikasi Django.
   - Middleware `SessionMiddleware` yang ada dalam Django bertanggung jawab untuk mengelola data sesi pengguna. Middleware ini akan memeriksa cookie pengguna untuk ID sesi, dan kemudian menghubungkan data sesi ini ke permintaan pengguna.

3. **Konfigurasi Cookie:**
   - Kita dapat mengkonfigurasi bagaimana Django menggunakan cookies dalam file `settings.py` proyek Kita. Kita dapat mengatur parameter seperti nama cookie, durasi cookie, domain yang diizinkan, dan lebih banyak lagi.
   - Contohnya, Kita dapat mengatur berapa lama cookie akan berlangsung dengan mengubah nilai `SESSION_COOKIE_AGE` dalam `settings.py`.

4. **Fungsi Bantu Django:**
   - Django menyediakan fungsi-fungsi bantu yang memudahkan penggunaan cookies. Beberapa contoh di antaranya adalah `request.session` untuk mengakses data sesi pengguna dan `response.set_cookie()` untuk mengatur nilai cookie dalam respons.

5. **Perlindungan Terhadap Serangan CSRF:**
   - Django secara otomatis melindungi cookies dari serangan CSRF (Cross-Site Request Forgery) dengan menyertakan token keamanan dalam setiap permintaan POST yang dilakukan oleh pengguna.

Penggunaan cookies dalam Django memungkinkan aplikasi web untuk menyimpan informasi sesi pengguna dan mengidentifikasi pengguna yang sudah masuk. Ini sangat penting untuk menghasilkan pengalaman pengguna yang personal, mengelola akses pengguna, dan menyimpan preferensi pengguna. Selain itu, Django secara otomatis mengelola banyak aspek terkait keamanan, seperti perlindungan terhadap serangan CSRF, untuk memastikan bahwa cookies digunakan dengan aman dalam aplikasi web Kita.

<br><br>
Penggunaan cookies dalam pengembangan web dapat menjadi alat yang sangat berguna untuk menyimpan informasi sesi pengguna, mengelola preferensi, dan meningkatkan pengalaman pengguna. Namun, seperti banyak teknologi, cookies juga memiliki potensi risiko yang harus diwaspadai. Berikut adalah beberapa pertimbangan keamanan yang perlu diperhatikan:

1. **Keamanan Data**: Data yang disimpan dalam cookies dapat menjadi target potensial bagi serangan jika tidak dienkripsi dengan benar. Misalnya, jika Kita menyimpan kata sandi dalam cookies atau data rahasia lainnya, ini dapat menjadi risiko keamanan yang serius jika cookies tersebut dicuri atau disusupi oleh pihak yang tidak sah.

2. **Serangan Terhadap Cookie**: Serangan seperti Cross-Site Scripting (XSS) atau Cross-Site Request Forgery (CSRF) dapat memungkinkan penyerang untuk mencuri atau memanipulasi cookies pengguna. Oleh karena itu, penting untuk mengimplementasikan langkah-langkah keamanan seperti menambahkan token anti-CSRF pada setiap permintaan POST.

3. **Informasi Pribadi**: Cookies yang berisi informasi pribadi seperti alamat email, nomor telepon, atau informasi keuangan harus dijaga dengan ketat dan hanya digunakan jika diperlukan. Selain itu, Kita perlu mematuhi regulasi dan hukum privasi data yang berlaku.

4. **Tracking Pengguna**: Cookies sering digunakan untuk melacak perilaku pengguna di seluruh situs web atau aplikasi. Sementara ini sering digunakan untuk meningkatkan pengalaman pengguna, juga dapat menjadi masalah privasi jika tidak ada pemberitahuan atau izin yang memadai dari pengguna.

5. **Cookie Theft**: Penyerang dapat mencuri cookies pengguna, terutama jika cookies disimpan dalam format yang tidak aman atau jika ada celah keamanan dalam aplikasi web. Ini dapat digunakan untuk mengambil alih sesi pengguna atau mendapatkan akses ilegal ke akun pengguna.

6. **Cookie Pernikahan Silang**: Dalam beberapa kasus, jika cookie terkait dengan satu domain, dapat ada risiko jika cookies tersebut disusupi atau dieksploitasi untuk mengakses domain lain yang menggunakan cookie yang sama.

7. **Cookie Persistence**: Cookies dapat memiliki masa berlaku (durasi) yang berbeda-beda. Jika sebuah cookie memiliki masa berlaku yang sangat lama, risiko penggunaan yang tidak sah menjadi lebih tinggi. Oleh karena itu, sebaiknya atur masa berlaku cookie sesuai dengan kebutuhan.

Penting untuk diingat bahwa penggunaan cookies yang aman sangat tergantung pada implementasi dan pengaturannya. Pengembang web harus memahami risiko potensial ini dan mengambil langkah-langkah keamanan yang sesuai untuk melindungi data pengguna. Selain itu, regulasi privasi data seperti GDPR di Uni Eropa atau CCPA di California juga mengatur penggunaan cookies dan mengharuskan pengembang untuk memberikan pemberitahuan dan persetujuan yang sesuai dari pengguna.

<br><br>
Pertama jalankan virtual environment agar tidak merusak package dalam komputer sendiri. Kemudian ubah file views.py dengan menambahkan fungsi register yang bertujuan untuk registrasi akun pengguna baru nantinya. Import package dari django yang sudah disediakan yaitu:
```py
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
```
package ini sudah disediakan django untuk memudahkan membuat form user pada website

fungsi register yang ditambahkan mengimplementasikan package UserCreationForm yaitu:
``` py
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

pesan pada messages bisa di custom sesuai keinginan, namun disini saya menggunakan pesan umum saja

kemudian kita perlu mengimplementasikan fungsi views.py tersebut pada laman html. disini saya membuat laman register.html pada direktori main/template

dengan isi:
```py
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}

<style>
    body {
        background-color: #fff;
        font-family: Arial, sans-serif;
    }

    .login {
        background-color: #fff;
        max-width: 400px;
        margin: 0 auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
    }

    h1 {
        color: #d9534f;
        text-align: center;
    }

    table {
        width: 100%;
    }

    td {
        padding: 10px;
    }

    .form-control {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 3px;
    }

    .btn {
        background-color: #d9534f;
        color: #fff;
        border: none;
        padding: 10px 20px;
        border-radius: 3px;
        cursor: pointer;
    }

    .btn.login_btn, .btn.register_btn {
        width: 100%;
    }

    ul {
        list-style: none;
        padding: 0;
    }

    li {
        color: #d9534f;
    }

    a {
        color: #d9534f;
        text-decoration: none;
    }
</style>

<div class="login">
    <h1>Register</h1>
    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td><input class="btn register_btn" type="submit" name="submit" value="Daftar"></td>
            </tr>
        </table>
    </form>
    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</div>

{% endblock content %}

```
implementasikan tampilan register pada register.html dan disini saya menghias sedikit dengan style css

agar laman dapat diakses oleh user, perlu dilakukan routing dan penambahan path pada urls.py

maka tambahkan import dan pathnya pada urls.py:
```py
from main.views import register 
...
path('register/', register, name='register'), 
...
```

Setelah register, buat fungsi login untuk mengakses akun yang telah dibuat. Django menyediakan package login dengan mengimport:
```py
from django.contrib.auth import authenticate, login
```
pada views.py

tambahkan implementasi kodenya dengan fungsi login:
```py
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
sama halnya dengan register, pesan dapat diatur sesuai selera. implementasi juga sama, perlu menambahkan file html baru, yaitu login.html di lokasi yang sama dengan register.html dengan kode:
```py
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<style>
    body {
        background-color: #fff;
        font-family: Arial, sans-serif;
    }

    .login {
        background-color: #fff;
        max-width: 400px;
        margin: 0 auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
    }

    h1 {
        color: #d9534f;
        text-align: center;
    }

    table {
        width: 100%;
    }

    td {
        padding: 10px;
    }

    .form-control {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 3px;
    }

    .btn {
        background-color: #d9534f;
        color: #fff;
        border: none;
        padding: 10px 20px;
        border-radius: 3px;
        cursor: pointer;
    }

    .btn.login_btn {
        width: 100%;
    }

    ul {
        list-style: none;
        padding: 0;
    }

    li {
        color: #d9534f;
    }

    a {
        color: #d9534f;
        text-decoration: none;
    }
</style>

<div class="login">
    <h1>Login</h1>
    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username:</td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
            <tr>
                <td>Password:</td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>
            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>
    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}
    Gak punya akun? Bilang dong <a href="{% url 'main:register' %}">Daftar klik disini</a>
</div>

{% endblock content %}

```

tentu ditambah juga style css yang senada dengan login.html

lakukan routing dengan langkah yang sama dengan register.py

Begitu juga dengan fungsi logout, Django juga punya packange dengan melakukan import dan implementasi fungsi baru pada views.py seperti:

```py
from django.contrib.auth import logout
...
def logout_user(request):
    logout(request)
    return redirect('main:login')
...
```
untuk logout tidak perlu laman baru, cukup tambahkan tombol logout yang berfungsi mengembalikan user ke halaman login dan mengeluarkan user dari akun tersebut dengan sedikit penambahan kode pada main.html
```py
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
```
sama dengan register dan login, logout juga perlu dilakukan routing dengan cara yang sama pada urls.py

<br><br>
Setelah semua selesai diimplementasikan, saya membuat 2 akun dummy dengan username pakmad dan pakmud dengan 3 data dummy di masing-masing akunnya. Cukup ikuti alur registrasi pada tombol buat akun, kemudian login dan tambahkan 3 item baru sesuai selera pada akun akun tersebut

<br><br>
Untuk menghubungkan hubungan antar product dan user dalam artian tiap user memiliki daftar profduct sendiri, perlu dilakukan penambahan sedikit kode pada main.html
```py
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
    ...
...
```
Namun sebelum itu, pastikan model User telah dibentuk, contohnya dengan kode:
```py
...
from django.contrib.auth.models import User
...
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
dan setelah menambah model pastikan melakukan migrasi seperti yang telah saya jelaskan pada tugas sebelumnya

ubah juga fungsi create_product pada views.py
```py
def create_product(request):
 form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
 ...
```
kode ini berfungsi agar data yang diinput tidak langsung dikirim ke server django, melainkan kita dapat memodifikasi data tersebut dengan penKita bahwa product yang diinput adalah product dari suatu user (ditKitain)

<br><br>
untuk menggunakan data cookies dan mengimplementasikannya untuk menampilkan last login, cukup modifikasi bagian views.py

tambahkan import dari django untuk mengambil data waktu dan cookies dengan import:
```py
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
implementasikan package tersebut pada fungsi login_user yang telah dibuat dengan kode:
```py
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```
dan tambahkan pada show main:
```py
context = {
    ...
    'last_login': request.COOKIES['last_login'],
}
```

ini berfungsi untuk menyimpan data last login dengan cookies pengguna dan menyimpannya pada lastlogin yang ada pada fungsi show main

kemudian tambahkan kode pada fungsi logout_user:
```py
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
yang berfungsi sebagai reset cookies agar diganti dengan data yang baru nantinya

Jangan lupa untuk tampilkan last login pada main.html. disini saya menggunakan kode:
```py
<div class="top-bar">
            <h5 class="last-login">Sesi terakhir login: {{ last_login }}</h5>
            <a href="{% url 'main:logout' %}" class="logout-button">Logout</a>
        </div>
```
untuk menampilkan last login pengguna di pojok kiri atas

Untuk menulis readme.md saya belajar agar sedikit lebih rapi setelah lebih banyak belajar tentang penataan html dan css untuk keperluan estetika website di tugas saya.

<br><br>
Element selectors dalam CSS digunakan untuk memilih elemen HTML berdasarkan jenis elemen atau tag-nya. Setiap jenis elemen memiliki karakteristik unik, dan penggunaan element selectors memungkinkan Kita untuk mengubah tampilan atau gaya elemen-elemen tersebut. Berikut adalah beberapa element selectors beserta manfaat dan waktu yang tepat untuk menggunakannya:

1. **Universal Selector (*):**
   - **Manfaat:** Menggunakan `*` sebagai selektor akan memilih semua elemen pada halaman.
   - **Waktu yang Tepat:** Sebaiknya digunakan dengan hati-hati karena dapat mempengaruhi semua elemen pada halaman. Gunakan jika benar-benar diperlukan, misalnya untuk mengatur nilai margin dan padding secara umum.

2. **Type Selector (Element Selector):**
   - **Manfaat:** Memilih semua elemen dengan tipe tertentu (misalnya, `<p>`, `<h1>`, `<ul>`) untuk menerapkan gaya pada semua elemen tersebut.
   - **Waktu yang Tepat:** Digunakan ketika Kita ingin mengatur gaya dasar elemen HTML, seperti mengubah font atau warna teks pada semua paragraf.

3. **ID Selector (#):**
   - **Manfaat:** Memilih elemen dengan atribut ID tertentu. ID harus unik di dalam dokumen.
   - **Waktu yang Tepat:** Ketika Kita ingin mengidentifikasi dan mengubah tampilan elemen tertentu yang memiliki ID unik, seperti mengatur gaya elemen header atau footer.

4. **Class Selector (.):**
   - **Manfaat:** Memilih elemen yang memiliki kelas tertentu. Elemen-elemen dapat memiliki beberapa kelas.
   - **Waktu yang Tepat:** Digunakan ketika Kita ingin menggabungkan beberapa elemen dan menerapkan gaya yang sama pada mereka, seperti mengatur warna latar belakang untuk semua elemen dengan kelas "button".

5. **Attribute Selector ([]):**
   - **Manfaat:** Memilih elemen berdasarkan atribut atau nilai atribut tertentu.
   - **Waktu yang Tepat:** Ketika Kita ingin memilih elemen berdasarkan atribut seperti href, src, atau nilai lainnya. Contoh: memilih semua tautan eksternal dengan `a[href^="http"]`.

6. **Pseudo-class Selector (:):**
   - **Manfaat:** Memilih elemen berdasarkan keadaan atau interaksi pengguna, seperti `:hover`, `:active`, atau `:nth-child`.
   - **Waktu yang Tepat:** Digunakan ketika Kita ingin mengatur gaya elemen berdasarkan keadaan tertentu, seperti mengubah warna teks saat mouse berada di atas tautan (`a:hover`).

7. **Pseudo-element Selector (::):**
   - **Manfaat:** Memungkinkan Kita mengakses elemen yang ada dalam elemen lain, seperti `::before` dan `::after` untuk menambahkan konten sebelum atau setelah elemen.
   - **Waktu yang Tepat:** Ketika Kita ingin menambahkan konten tambahan atau efek styling sebelum atau setelah elemen tertentu.

Pemilihan selector yang tepat akan sangat bergantung pada tujuan Kita. Pemahaman yang baik tentang hierarki HTML dan kebutuhan desain web Kita akan membantu Kita memilih dan menggunakan selector dengan lebih efektif.

<br><br>
HTML5 Tag yang saya ketahui karena sering terpakai pada tugas membuat .html dan readme.md
1. **`<div>:`** Elemen `<div>` digunakan untuk mengelompokkan dan mengatur konten dalam blok. Ini adalah elemen kontainer umum yang sering digunakan dalam CSS untuk mengatur tata letak halaman.

2. **`<a>`:** Elemen `<a>` digunakan untuk membuat tautan atau hyperlink. Kita dapat mengarahkannya ke halaman web lain, file, atau bahkan ke bagian lain dari halaman yang sama.

3. **`<img>`:** Elemen `<img>` digunakan untuk menampilkan gambar di halaman web. Kita dapat menentukan sumber gambar dengan atribut `src`.

4. **`<p>`:** Elemen `<p>` digunakan untuk menampilkan teks dalam paragraf. Ini digunakan secara luas untuk mengorganisir dan memformat teks dalam dokumen.

5. **`<ul>` dan `<ol>`:** Elemen `<ul>` digunakan untuk membuat daftar tak terurut (unordered list), sementara `<ol>` digunakan untuk membuat daftar berurut (ordered list). Daftar tersebut diatur dengan elemen `<li>` (list item).

6. **`<h1>` hingga `<h6>`:** Elemen-elemen heading digunakan untuk memberikan struktur hierarki judul dalam halaman web. `<h1>` adalah yang paling penting, sementara `<h6>` adalah yang paling rendah dalam hierarki.

7. **`<span>`:** Elemen `<span>` digunakan untuk mengapit teks atau elemen lain tanpa memengaruhi tampilan atau tata letak secara besar-besaran. Ini sering digunakan untuk menerapkan gaya atau fungsi melalui CSS atau JavaScript.

8. **`<table>`:** Elemen `<table>` digunakan untuk membuat tabel di halaman web. Ini termasuk elemen-elemen seperti `<tr>` (table row), `<th>` (table header), dan `<td>` (table data cell).

9. **`<form>`:** Elemen `<form>` digunakan untuk membuat formulir yang memungkinkan pengguna untuk mengirimkan data ke server. Ini berisi berbagai elemen input seperti teks, kata sandi, checkbox, dan lainnya.

10. **`<br>:`** Elemen `<br>` digunakan untuk membuat pemisah baris (line break) dalam teks atau konten tanpa mengganti paragraf. Ini sering digunakan dalam teks yang tidak terstruktur atau dalam kasus-kasus tertentu di mana perlu ada pemisah baris.

Tag-tag ini adalah beberapa dari tag HTML5 yang paling umum digunakan dalam pengembangan web dan membentuk dasar dari hampir semua halaman web modern.

<br> <br>
Margin dan padding adalah dua konsep yang penting dalam CSS yang digunakan untuk mengatur tata letak dan tampilan elemen HTML. Namun, mereka memiliki fungsi yang berbeda dalam mengatur ruang di sekitar elemen tersebut:

1. **Margin:**
   - **Margin adalah ruang di luar elemen.** Ini adalah jarak antara elemen dan elemen-elemen lain di sekitarnya.
   - **Margin tidak memiliki latar belakang atau border.** Ini hanya memengaruhi jarak antara elemen tersebut dan elemen-elemen tetangganya.
   - **Margin secara default adalah transparan atau berwarna latar belakang elemen yang ada di bawahnya.**
   - **Mengatur margin dapat memengaruhi tata letak elemen dan posisinya di dalam halaman.**

   Contoh penggunaan margin:
   ```css
   .box {
     margin: 10px; /* Memberikan margin 10px ke semua sisi elemen */
   }
   ```

2. **Padding:**
   - **Padding adalah ruang di dalam elemen.** Ini adalah jarak antara batas elemen dan kontennya sendiri.
   - **Padding dapat memiliki latar belakang dan border.** Ini memengaruhi ruang di sekitar konten elemen tersebut.
   - **Padding biasanya digunakan untuk memberikan ruang antara konten dan batas elemen.**
   - **Mengatur padding tidak memengaruhi tata letak elemen di dalam halaman, hanya memengaruhi tampilan konten dalam elemen tersebut.**

   Contoh penggunaan padding:
   ```css
   .box {
     padding: 10px; /* Memberikan padding 10px ke semua sisi konten elemen */
   }
   ```

Sederhananya, margin mengontrol ruang di luar elemen, sementara padding mengontrol ruang di dalam elemen. Keduanya adalah alat penting dalam mengatur tata letak dan tampilan elemen dalam desain web, dan pemahaman yang baik tentang perbedaan antara keduanya akan membantu Kita merancang halaman web dengan lebih baik.

<br> <br>
Tailwind CSS dan Bootstrap adalah dua framework CSS yang populer digunakan dalam pengembangan web untuk mempermudah desain dan styling halaman web. Berikut adalah perbedaan utama antara keduanya serta kapan sebaiknya menggunakan Bootstrap daripada Tailwind, dan sebaliknya:

**Perbedaan antara Tailwind CSS dan Bootstrap:**

1. **Gaya Pendekatan:**
   - **Tailwind CSS:** Tailwind menggunakan gaya pendekatan "utility-first", di mana Kita membangun tampilan elemen dengan menggabungkan kelas-kelas utilitas ke dalam elemen HTML. Kita dapat mengkustomisasi tampilan dengan mengedit file konfigurasi.
   - **Bootstrap:** Bootstrap mengadopsi gaya pendekatan "framework-first", yang menyediakan banyak komponen siap pakai dan gaya bawaan yang telah ditentukan sebelumnya. Kita menggunakan kelas-kelas Bootstrap untuk membangun tampilan Kita.

2. **Ukuran File:**
   - **Tailwind CSS:** Tailwind cenderung menghasilkan file CSS yang lebih besar karena menghasilkan banyak kelas utilitas yang digunakan dalam HTML Kita.
   - **Bootstrap:** Bootstrap memiliki file CSS yang lebih besar karena mencakup banyak komponen dan gaya yang telah ditentukan sebelumnya.

3. **Kustomisasi:**
   - **Tailwind CSS:** Tailwind memungkinkan tingkat kustomisasi yang tinggi melalui file konfigurasi. Kita dapat menyesuaikan setiap aspek tampilan sesuai kebutuhan proyek.
   - **Bootstrap:** Bootstrap juga dapat disesuaikan, tetapi perlu usaha lebih besar dalam penyesuaian dibandingkan dengan Tailwind.

4. **Komponen:**
   - **Tailwind CSS:** Tailwind tidak menyediakan komponen siap pakai seperti Bootstrap. Kita harus membangun komponen Kita sendiri dengan menggunakan kelas utilitas.
   - **Bootstrap:** Bootstrap menyediakan banyak komponen siap pakai seperti navbar, card, modal, dll.

**Kapan sebaiknya menggunakan Bootstrap daripada Tailwind, dan sebaliknya:**

- **Gunakan Bootstrap jika:**
  - Kita ingin membangun situs dengan cepat menggunakan komponen siap pakai.
  - Kita tidak perlu tingkat kustomisasi yang tinggi dan dapat mengikuti desain Bootstrap yang ada.
  - Kita lebih suka pendekatan "framework-first" yang menyediakan struktur dan tampilan yang telah ditentukan sebelumnya.

- **Gunakan Tailwind CSS jika:**
  - Kita ingin tingkat kustomisasi yang tinggi dan ingin mengontrol setiap aspek tampilan.
  - Kita suka pendekatan "utility-first" yang memungkinkan Kita membuat tampilan dengan kelas-kelas utilitas.
  - Kita ingin mengurangi ukuran file CSS yang dihasilkan dan hanya mengirimkan gaya yang benar-benar digunakan.

Ketika memilih antara Tailwind CSS dan Bootstrap, pertimbangkan kebutuhan proyek Kita, tingkat kustomisasi yang Kita inginkan, dan preferensi pribadi dalam gaya pengembangan. Kedua framework memiliki kelebihan dan kekurangan masing-masing, dan pilihan tergantung pada kasus-kasus khusus.

<br><br>
Untuk kustomisasi main.html dengan bootstrap, saya menggunakan implementasi navbar yang berisi tombol home dan logout agar tampilan menjadi lebih menarik. Untuk halaman login dan register tampilan hanya saya ubah bagian tombol, gaya font, dan penempatannya saja agar terlihat lebih elegan.

Bagian inventori pada main.html saya simpan dalam table agar terlihat lebih rapi.

Semua komponen sebisa mungkin saya beri warna dan gaya (pada tombol agar tidk kotak misalnya) dengan menambahkan style CSS pada bagian bawah kode. 

Semua halaman seperti login, register, main, dll saya implementasikan tema yang serupa dengan pallete warna yang sama. Kurang lebih kode main.html saya jadi seperti ini:
```html
{% extends 'base.html' %}

{% block content %}
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container">
            <a class="navbar-brand" href="{% url 'main:show_main' %}">WarMad</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'main:create_product' %}">
                            Add New Product
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'main:logout' %}">
                            Logout
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    
    <div class="container mt-4">
        <header>
            <h1>Warung Madura</h1>
            <p class="author">by: arjunaja PBP-F (bukan orang Madura)</p>
        </header>
        <div class="top-bar">
            <h5 class="last-login">Sesi terakhir login: {{ last_login }}</h5>
        </div>
        <div class="product-count">
            <p>Tersedia {{ products|length }} barang cong</p>
        </div>

        <div class="product-list">
            <table>
                <tr>
                    <th>Nama Barang</th>
                    <th>Harga</th>
                    <th>Tersedia</th>
                    <th>Deskripsi</th>
                    <th>Tanggal Ditambahkan</th>
                </tr>
            
                {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}
            
                {% for product in products %}
                    <tr>
                        <td>{{product.name}}</td>
                        <td>{{product.price}}</td>
                        <td>
                            {{product.amount}}
                            <a href="{% url 'main:inc_dec_product' product.id 'dec' %}"><button type="submit" class="button small">-</button></a>
                            <a href="{% url 'main:inc_dec_product' product.id 'inc' %}"><button type="submit" class="button small">+</button></a>
                        </td>
                        <td>{{product.description}}</td>
                        <td>{{product.date_added}}
                            <a href="{% url 'main:delete_product' product.id %}"><button type="submit" class="button small">Delete</button></a>
                        </td>
                    </tr>
                {% endfor %}
            </table>
        </div>
    </div>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        header {
            background-color: #333;
            color: #fff;
            padding: 20px 0;
            text-align: center;
        }
        h1 {
            margin: 0;
        }
        .author {
            margin-top: 5px;
        }
        .product-list table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        .product-list th, .product-list td {
            border: 1px solid #ccc;
            padding: 10px;
            text-align: left;
        }
        .product-list th {
            background-color: #333;
            color: #fff;
        }
        .product-list tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        .add-product {
            text-align: center;
            margin-top: 20px;
        }
        .add-button {
            padding: 10px 20px;
            background-color: #ff5733;
            color: #fff;
            border: none;
            border-radius: 5px;
            font-weight: bold;
            text-decoration: none;
            cursor: pointer;
        }
        .add-button:hover {
            background-color: #e44e2e;
        }
        .product-list {
            margin-top: 30px;
        }
        .product-list table {
            border-collapse: separate;
            border-spacing: 10px;
        }
        .product-list th, .product-list td {
            border: 1px solid #ccc;
            padding: 10px;
            text-align: left;
            background-color: #fff;
            box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
        }
        .product-list th {
            background-color: #ff5733;
            color: #fff;
        }
        .product-list tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        .top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .last-login {
            color: #333;
        }
        .logout-button {
            padding: 10px 20px;
            background-color: #ff5733;
            color: #fff;
            border: none;
            border-radius: 5px;
            font-weight: bold;
            text-decoration: none;
            cursor: pointer;
        }
        .logout-button:hover {
            background-color: #e44e2e;
        }
    </style>
</div>
{% endblock content %}
```

kode-kode style tersebut saya dapat dari laman internet dari berbagai sumber. Beberapa kustomisasi juga saya coba sebagai bentuk _trial and error_ pada **situs PBP** di bagian **_Play Ground_**
