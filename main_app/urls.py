
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paypal_integration.urls')),
    # Paypal URL
    path('paypal/',include('paypal.standard.ipn.urls'))
]
