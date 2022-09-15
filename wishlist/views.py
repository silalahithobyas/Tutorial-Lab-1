from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from wishlist.models import BarangWishlist

def show_wishlist(request):
    return render(request, "wishlist.html", context)
    
data_barang_wishlist = BarangWishlist.objects.all()

context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Thobyas'
}

def show_xml(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")



