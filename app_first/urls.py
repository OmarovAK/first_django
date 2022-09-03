from django.urls import path
from .views import first_page, current_time, list_files


app_name = 'first_pages'
urlpatterns = [
    path('',first_page, name='home'),
    path('current_time',current_time, name='current_time'),
    path('list_docs', list_files, name='list_pages')

]
