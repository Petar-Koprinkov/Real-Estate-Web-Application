from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from real_estate_web_application import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('real_estate_web_application.common.urls')),
    path('account/', include('real_estate_web_application.accounts.urls')),
    path('real-estate/', include('real_estate_web_application.real_estate.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)