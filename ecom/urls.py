from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('store.urls')),  # Routing to the store app

    path('cart/', include('cart.urls')),  # Routing to the cart app

    path('payment/', include('payment.urls')),  # Routing to the payment app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
