from django.urls import path

from . import views, text2info

app_name = 'NLP'
urlpatterns = [
    path('', views.home, name='home'),
    path('maps/',views.maps,name='maps'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('test/',views.index,name='index'),
    path('upload/',views.upload,name='upload'),
    path('manual_entry/', views.manual_entry, name='manual_entry'),
    path('audio_data/', views.audio_data, name='audio_data'),
    path('new_profile/',views.update_profile,name='new_profile'),
    path('create_profile/',views.create_profile,name='create_profile')
]