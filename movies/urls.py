from django.urls import path
from . import views
app_name='movie'
urlpatterns = [
    path('',views.home,name='home'),
    path('fav',views.fav,name='fav'),
    path('search',views.search,name='search'),
    path('about',views.about,name='about')
]
