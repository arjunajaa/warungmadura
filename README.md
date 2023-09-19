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

1. Dalam Django, perbedaan antara form POST dan form GET terletak pada cara data dikirim dari halaman web ke server. Saat menggunakan metode POST, data formulir dikemas dan dikirimkan secara tersembunyi dalam body permintaan HTTP, sehingga lebih aman untuk data sensitif. Di sisi lain, metode GET mengirimkan data sebagai bagian dari URL dalam parameter query string, yang membuatnya terlihat dalam URL dan cocok untuk permintaan yang tidak mengubah data di server. POST digunakan untuk mengirim data yang ingin dimasukkan atau dimodifikasi di server, sementara GET digunakan untuk mengambil data dari server. Dengan pemahaman ini, pengembang dapat memilih metode yang sesuai sesuai dengan kebutuhan keamanan dan tujuan aplikasi web mereka.
2. XML (Extensible Markup Language), JSON (JavaScript Object Notation), dan HTML (Hypertext Markup Language) adalah format yang berbeda yang digunakan untuk pengiriman data dalam konteks berbeda.

XML adalah format yang serbaguna dan dapat digunakan untuk menggambarkan struktur data yang kompleks dengan sangat baik. Ini terdiri dari elemen-elemen yang dikelilingi oleh tag, dan atribut-atribut dapat ditambahkan untuk memberikan informasi tambahan tentang elemen-elemen tersebut. XML sangat baik digunakan untuk pertukaran data antara aplikasi yang berbeda atau penyimpanan data yang kompleks. Namun, XML memiliki overhead yang cukup besar karena tag-tagnya dan oleh karena itu mungkin tidak efisien untuk data yang sangat besar.

JSON, di sisi lain, adalah format ringkas yang digunakan untuk mengirimkan dan menyimpan data. Ini berbasis pada sintaks objek JavaScript dan terdiri dari pasangan kunci-nilai yang membuatnya mudah dipahami oleh manusia dan mudah diproses oleh komputer. JSON sangat umum digunakan dalam aplikasi web modern dan API (Application Programming Interface) untuk mentransfer data antara server dan klien. Ini lebih efisien daripada XML karena memiliki payload yang lebih ringan.

HTML, seperti XML, juga berisi struktur dengan elemen-elemen yang dikelilingi oleh tag, tetapi HTML memiliki tujuan yang berbeda. HTML digunakan untuk menggambarkan struktur konten pada halaman web, seperti teks, gambar, tautan, dan elemen-elemen lainnya. Ini adalah bahasa markup yang digunakan untuk membuat tampilan visual dalam web browser dan tidak digunakan untuk pertukaran data mentah antara aplikasi.

Jadi, perbedaan utama antara ketiganya adalah dalam tujuan penggunaannya: XML digunakan untuk merepresentasikan data kompleks, JSON digunakan untuk pertukaran data ringkas, dan HTML digunakan untuk membuat tampilan halaman web. Pilihan antara ketiganya tergantung pada kebutuhan aplikasi dan konteks penggunaannya.
3. JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena kesederhanaan dan fleksibilitasnya. Format JSON yang ringkas dan mudah dibaca oleh manusia menjadikannya pilihan yang nyaman untuk mengirim dan menerima data dalam format yang intuitif. Selain itu, JSON memiliki payload yang ringan, mengurangi penggunaan bandwidth dan mempercepat respons aplikasi. Kemampuannya untuk mendukung struktur data yang fleksibel memungkinkan representasi data yang kompleks, seperti objek bersarang dan larik, yang sering ditemukan dalam aplikasi modern. Kecocokannya dengan berbagai bahasa pemrograman dan dukungan yang luas dalam browser web menjadikan JSON sebagai standar de facto dalam pertukaran data antar aplikasi web, terutama dalam konteks pengembangan API RESTful yang semakin umum digunakan.
4. - Pertama, buat file forms.py yang menjadi badan dari input pengguna nantinya. File ini berisi tentang variabel model yang akan dimintakan input kepada pengguna dan sesuai dengan model yang ada pada models.py. Kemudian pada bagian view di file views.py tambahkan fungsi baru untuk membuat sebuah produk dari input, disini saya menggunakan nama fungsi create_product. Kemudian ubah bagian show_main di views.py agar menyimpan setiap produk yang ditambahkan. Setelah itu buat file create_product.html sebagai tampilan input product dengan tombol yang akan mengarahkan pada kolom form input produk yang nantinya ketika produk ditambahkan akan kembali ke layar utama dengan tampilan produk yang telah di input. Lalu lakukan routing pada create product dengan menambahkan import dan path pada urls.py
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