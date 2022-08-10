from unicodedata import name
from.views import home_page_view
from django.urls import path
urlpatterns=[path('',home_page_view.as_view(),name='home')
]