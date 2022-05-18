from django.urls import path,re_path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add,name='madd'),
    path('demo/',views.demo_add2,name='demo'),
    path('demo/<int:sid>',views.demo_add2,name='demo1'),
    path('demo/<int:sid>/<str:name>',views.demo_add2,name='demo2'),
    path('demo/<int:sid>/<str:name>/<uuid:uid>',views.demo_add2,name='demo3'),
    re_path(r"^fun/([0-9]{1,4})/([0-9]{1,2})$",views.fun),
    re_path(r"^fun1/(?P<yy>[0-9]{1,4})/(?P<mm>[0-9]{1,2})$",views.fun1)
]