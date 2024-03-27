from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_view(request):
    html="""
    <h1>first_page </h1>
    <a href='second/'> ikkinchi_page </a>
    """
    return HttpResponse(html)


def second_view(request):
    html="""
    <h1>second_page</h1>
    <a href='../'> birinchi_page </a>
    """
    return HttpResponse(html)


def pages(request,page):
    html=f"""
    <h1>page:{page}</h1>
    <h1>bolim:{page}</h1>
    <a href='../'> birinchi_page </a>
    """
    return HttpResponse(html)