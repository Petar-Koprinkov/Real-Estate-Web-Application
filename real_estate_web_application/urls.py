from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from real_estate_web_application import settings

urlpatterns = [

    #DRF-spectacular
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('properties-api/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('admin/', admin.site.urls),
    path('', include('real_estate_web_application.common.urls')),
    path('account/', include('real_estate_web_application.accounts.urls')),
    path('real-estate/', include('real_estate_web_application.real_estate.urls')),

    #Django REST Framework
    path('properties/', include('real_estate_web_application.properties_api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
