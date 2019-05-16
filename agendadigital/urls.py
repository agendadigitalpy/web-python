from django.conf.urls import url
from django.contrib import admin
from . import views #importamos el archivo views.py
#Los archivos estaticos se definen en settings.py en la linea 120 se agrego 
#STATICFILES_DIRS = (
#  os.path.join(BASE_DIR, 'assets'),
#) para que funcione
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls), # r'^ regular epresion /aslasdfasfadmin igual entra a admin. $ lo mismo r'^ pero alrevez
    url(r'^$', views.homepage), #url para el index.html
    url(r'^documentacion/$', views.documentacion),
    url(r'^seguimiento/$', views.seguimiento),
    url(r'^solicitudes/$', views.solicitudes),
    url(r'^gobierno-digital/$', views.gobiernodigital),
    url(r'^economia-digital/$', views.economiadigital),
    url(r'^conectividad/$', views.conectividad),
    url(r'^fortalecimiento-institucional/$', views.fortalecimientoinstitucional),
]

urlpatterns += staticfiles_urlpatterns()