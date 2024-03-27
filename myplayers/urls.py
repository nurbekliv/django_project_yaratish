from django.urls import path
from .views import pages,first_views

urlpatterns=[
    path('', first_views, name='first_page'),
    path('pages/<str:page>', pages, name="pages"),
]