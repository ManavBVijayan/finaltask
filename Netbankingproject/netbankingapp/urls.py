from django.urls import path
from . import views
app_name='netbankingapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('appform/',views.getdata,name='appform'),
    path('final/',views.final,name='final'),
]