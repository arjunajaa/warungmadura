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
- 3. JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena kesederhanaan dan fleksibilitasnya. Format JSON yang ringkas dan mudah dibaca oleh manusia menjadikannya pilihan yang nyaman untuk mengirim dan menerima data dalam format yang intuitif. Selain itu, JSON memiliki payload yang ringan, mengurangi penggunaan bandwidth dan mempercepat respons aplikasi. Kemampuannya untuk mendukung struktur data yang fleksibel memungkinkan representasi data yang kompleks, seperti objek bersarang dan larik, yang sering ditemukan dalam aplikasi modern. Kecocokannya dengan berbagai bahasa pemrograman dan dukungan yang luas dalam browser web menjadikan JSON sebagai standar de facto dalam pertukaran data antar aplikasi web, terutama dalam konteks pengembangan API RESTful yang semakin umum digunakan.
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

1. **Mudah Digunakan:** `UserCreationForm` adalah bagian dari Django's built-in forms, yang membuatnya mudah digunakan dan menghemat waktu dalam pengembangan aplikasi web yang melibatkan otentikasi pengguna. Anda hanya perlu mengimpor dan menggunakannya dalam proyek Anda.

2. **Validasi Otomatis:** Formulir ini dilengkapi dengan validasi otomatis untuk memeriksa apakah input yang dimasukkan oleh pengguna memenuhi persyaratan tertentu, seperti panjang kata sandi minimal, uniknya username, dan validitas alamat email.

3. **Dukungan untuk Customization:** Anda dapat dengan mudah menyesuaikan tampilan dan perilaku formulir ini sesuai dengan kebutuhan proyek Anda. Anda dapat menambahkan bidang tambahan atau mengubah pesan kesalahan sesuai kebijakan aplikasi Anda.

4. **Integrasi dengan Model Pengguna Django:** `UserCreationForm` terintegrasi dengan model pengguna bawaan Django, yang berarti Anda dapat dengan mudah menghubungkan formulir ini dengan model pengguna dan menyimpan data pengguna yang terdaftar dalam database.

**Kekurangan:**

1. **Tidak Mendukung Opsi Lainnya:** `UserCreationForm` dirancang untuk kasus pengguna yang sangat sederhana. Jika Anda memerlukan opsi pendaftaran yang lebih kompleks atau memiliki persyaratan yang berbeda, Anda mungkin perlu menyesuaikan formulir ini atau bahkan membuat formulir pendaftaran kustom Anda sendiri.

2. **Terbatas dalam Desain:** Tampilan bawaan dari `UserCreationForm` mungkin terlalu sederhana dan perlu disesuaikan jika Anda ingin tampilan pendaftaran yang lebih kompleks atau menarik.

3. **Keamanan Tambahan Mungkin Diperlukan:** Meskipun `UserCreationForm` menyediakan validasi otomatis, keamanan tambahan seperti proteksi terhadap serangan CSRF dan XSS (Cross-Site Scripting) masih perlu ditambahkan secara terpisah dalam aplikasi Anda.

Secara keseluruhan, `UserCreationForm` adalah alat yang berguna untuk memulai dengan cepat dalam mengembangkan fitur pendaftaran pengguna dalam aplikasi web Django. Namun, untuk aplikasi yang lebih kompleks atau dengan persyaratan khusus, Anda mungkin perlu melakukan penyesuaian tambahan atau bahkan membuat formulir pendaftaran kustom Anda sendiri.

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
   - Anda dapat mengkonfigurasi bagaimana Django menggunakan cookies dalam file `settings.py` proyek Anda. Anda dapat mengatur parameter seperti nama cookie, durasi cookie, domain yang diizinkan, dan lebih banyak lagi.
   - Contohnya, Anda dapat mengatur berapa lama cookie akan berlangsung dengan mengubah nilai `SESSION_COOKIE_AGE` dalam `settings.py`.

4. **Fungsi Bantu Django:**
   - Django menyediakan fungsi-fungsi bantu yang memudahkan penggunaan cookies. Beberapa contoh di antaranya adalah `request.session` untuk mengakses data sesi pengguna dan `response.set_cookie()` untuk mengatur nilai cookie dalam respons.

5. **Perlindungan Terhadap Serangan CSRF:**
   - Django secara otomatis melindungi cookies dari serangan CSRF (Cross-Site Request Forgery) dengan menyertakan token keamanan dalam setiap permintaan POST yang dilakukan oleh pengguna.

Penggunaan cookies dalam Django memungkinkan aplikasi web untuk menyimpan informasi sesi pengguna dan mengidentifikasi pengguna yang sudah masuk. Ini sangat penting untuk menghasilkan pengalaman pengguna yang personal, mengelola akses pengguna, dan menyimpan preferensi pengguna. Selain itu, Django secara otomatis mengelola banyak aspek terkait keamanan, seperti perlindungan terhadap serangan CSRF, untuk memastikan bahwa cookies digunakan dengan aman dalam aplikasi web Anda.

<br><br>
Penggunaan cookies dalam pengembangan web dapat menjadi alat yang sangat berguna untuk menyimpan informasi sesi pengguna, mengelola preferensi, dan meningkatkan pengalaman pengguna. Namun, seperti banyak teknologi, cookies juga memiliki potensi risiko yang harus diwaspadai. Berikut adalah beberapa pertimbangan keamanan yang perlu diperhatikan:

1. **Keamanan Data**: Data yang disimpan dalam cookies dapat menjadi target potensial bagi serangan jika tidak dienkripsi dengan benar. Misalnya, jika Anda menyimpan kata sandi dalam cookies atau data rahasia lainnya, ini dapat menjadi risiko keamanan yang serius jika cookies tersebut dicuri atau disusupi oleh pihak yang tidak sah.

2. **Serangan Terhadap Cookie**: Serangan seperti Cross-Site Scripting (XSS) atau Cross-Site Request Forgery (CSRF) dapat memungkinkan penyerang untuk mencuri atau memanipulasi cookies pengguna. Oleh karena itu, penting untuk mengimplementasikan langkah-langkah keamanan seperti menambahkan token anti-CSRF pada setiap permintaan POST.

3. **Informasi Pribadi**: Cookies yang berisi informasi pribadi seperti alamat email, nomor telepon, atau informasi keuangan harus dijaga dengan ketat dan hanya digunakan jika diperlukan. Selain itu, Anda perlu mematuhi regulasi dan hukum privasi data yang berlaku.

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
kode ini berfungsi agar data yang diinput tidak langsung dikirim ke server django, melainkan kita dapat memodifikasi data tersebut dengan penanda bahwa product yang diinput adalah product dari suatu user (ditandain)

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