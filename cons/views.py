from django.shortcuts import render
from django.http import HttpResponse
from django.core.files import File
from .models import Cup, Cup_out, Cup_1, Image
from django.template import RequestContext


# def cons1(request):
#     header = "Выберите тип кружки"  # обычная переменная
#     cup_type = Cup(type = 1)
#     cup_color = Cup(color = "Белый")
#     cup_surface = Cup(surface="Гладкая")
#     cup_size = Cup(size="Большой")
#     cup_image = Cup(image="1_aLvXjS4.png'")
#     #color = "Белый", surface = "Гладкая", size = "Большой", image = '1_aLvXjS4.png')
#
#     data = {"header": header, "cup_type": cup_type, "cup_color": cup_color, "cup_surface": cup_surface, "cup_size":cup_size,"cup_image": cup_image}
#     return render(request, "cons/home.html", context=data)

def cons1(request):
    header = "Выберите тип кружки"
    cup_type = Cup.objects.all()
    #cup_type1 = len(cup_type) # /media/images/2_tqPrEe9.png так отобразится картинка
    cup_1_image = "/media/images/1_M6skgwS.png"
    cup_2_image = "/media/images/2_tqPrEe9.png"
    data = {"header": header, "cup_type": cup_type,"cup_1_image": cup_1_image, "cup_2_image": cup_2_image}
    return render(request, "cons/home.html", context=data)