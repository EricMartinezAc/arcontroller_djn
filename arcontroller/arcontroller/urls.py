
from django.contrib import admin
from django.urls import path
from members.views import members
from catalog.views import catalog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', members),
    path('catalog/', catalog) 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)