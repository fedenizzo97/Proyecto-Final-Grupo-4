from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path('inicio', views.inicio, name='inicio'),
    path('acercademi', views.acerca_de_mi, name='acercademi'),
    path('vacunas', views.vacunas, name="vacunas"),
    path('barbijos', views.barbijos, name="barbijos"),
    path('oximetros', views.oximetros, name="oximetros"),
    path('vacunaFormulario', views.vacunaFormulario, name="vacunaFormulario"),
    
    path('eliminarVacuna/<vacuna_proveedor>/', views.eliminarVacunas, name='eliminarVacuna'),
    
    path('vacuna/list', views.VacunaList.as_view(), name = "List"),
    path(r'^(?P<pk>\d+)$', views.VacunaDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.VacunaCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.VacunaUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.VacunaDelete.as_view(), name='Delete'),

    path('barbijo/list', views.BarbijosList.as_view(), name = "ListB"),
    path(r'^detail/(?P<pk>\d+)$', views.BarbijosDetalle.as_view(), name='DetailB'),
    path(r'^add$', views.BarbijosCreacion.as_view(), name='NewB'),
    path(r'^edit/(?P<pk>\d+)$', views.BarbijosUpdate.as_view(), name='EditB'),
    path(r'^delete/(?P<pk>\d+)$', views.BarbijosDelete.as_view(), name='DeleteB'),
    

    path('oximetro/list', views.OximetrosList.as_view(), name = "ListO"),
    path(r'^detailO/(?P<pk>\d+)$', views.OximetrosDetalle.as_view(), name='DetailO'),
    path(r'^addO$', views.OximetrosCreacion.as_view(), name='NewO'),
    path(r'^editO/(?P<pk>\d+)$', views.OximetrosUpdate.as_view(), name='EditO'),
    path(r'^deleteO/(?P<pk>\d+)$', views.OximetrosDelete.as_view(), name='DeleteO'),
    
     
    path('login', views.login_request, name = 'Login'), 
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    
]   