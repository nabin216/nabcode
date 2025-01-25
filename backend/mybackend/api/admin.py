from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Contact, Mail, ServiceType, Service, Serviceweb

class ServiceAdminForm(forms.ModelForm):
    details = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Service
        fields = '__all__'

class ServicewebAdminForm(forms.ModelForm):
    details = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Serviceweb
        fields = '__all__'

class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm

class ServicewebAdmin(admin.ModelAdmin):
    form = ServicewebAdminForm

# Register models only if they are not already registered
models_to_register = [Contact, Mail, Service, ServiceType, Serviceweb]
admin_classes = [None, None, ServiceAdmin, None, ServicewebAdmin]

for model, admin_class in zip(models_to_register, admin_classes):
    try:
        if admin_class:
            admin.site.register(model, admin_class)
        else:
            admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass