from django.shortcuts import render

from .models import Product

# Create your views here.
def show_main(request):
    product1 = Product(
        name = "Beras 5 kg",
        price = 50000,
        description = "Beras 5 kg asli dari petani, no plastik plastik, no campur, no kotor,\nno kuman, no virus, no bakteri, no corona, no covid, no apapun, 100% beras asli dari petani",
        amount = 1,
    )
    product2 = Product(
        name = "Rokok Surya 16",
        price = 30000,
        description = "Rokok dengan tembakau dan cengkih dalam negri.\nDengan Surya, hidup bercahaya",
        amount = 1,
    )
    product3 = Product(
        name = "Kopi Kapal Api",
        price = 1000,
        description = "Kopi dengan biji kopi dan campuran jagung,\nyang penting enak dan bisa bantu buka warung 24 jam",
        amount = 2,
    ) 
    return render(request, "main.html", {'data': product1, 'data2': product2, 'data3': product3})
