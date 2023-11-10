from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from instruments.views import InstrumentViewSet
from django.conf import settings
from django.conf.urls.static import static

# create a new router
router = routers.DefaultRouter()
# register our viewsets
router.register(r'instruments', InstrumentViewSet) #register "/instruments" routes


urlpatterns = [
    # add all of our router urls
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)