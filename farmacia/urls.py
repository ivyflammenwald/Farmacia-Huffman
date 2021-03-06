from django.urls import path, re_path
from . import views
from django.core.mail import EmailMessage
from django.contrib.auth.views import login, password_reset, password_reset_done, password_reset_confirm, \
    password_reset_complete

urlpatterns = [
    path('', views.index, name='inicio'),
    path('index/', views.index, name='inicio'),
    path('productos/agregar',views.productos, name='productos'),
    path('registro',views.registro ,name="registro"),
    path('sesion',views.sesion ,name="sesion"),
    path('administrador',views.administrador ,name="administrador"),
    path('productos',views.productos_all,name="productos_all"),
    path('productos/cambiar<folio>',views.producto_cambiar,name="producto_cambiar"),
    path('productos/eliminar<folio>',views.producto_eliminar,name="producto_eliminar"),
    path('facturas',views.factura,name="historia_facturas"),
    path('crearUsuario',views.registro,name="crear_usuario"),
    path('contacto',views.contacto,name="contacto"),
    path('promocion',views.promocion,name="promocion"),
    re_path(r'^reset/password_reset', password_reset,
        {'template_name': 'registration/password_reset_form.html',
         'email_template_name': 'registration/password_reset_email.html'},
        name='password_reset'),
    re_path(r'^password_reset_done', password_reset_done,
        {'template_name': 'registration/password_reset_done.html'},
        name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    re_path(r'^reset/done', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),
]
