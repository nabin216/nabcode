from django.urls import path
from .views import contact_view, mail_view, service_list, ServiceTypeList

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('mail/', mail_view, name='mail'),
    path('services/', service_list, name='service-list'),
    path('service-types/', ServiceTypeList.as_view(), name='service-type-list'),

]