from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the api app's URLs
    path('blog/', include('blog.urls')),  # Include the blog app's URLs
    path('ckeditor/', include('ckeditor_uploader.urls')),  # Include the CKEditor URLS
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
