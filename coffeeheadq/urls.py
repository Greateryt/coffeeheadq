
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views as auth_views
from . import views

urlpatterns = [
    path('',views.mainpage,name="mainpage"),
    path('admin/', admin.site.urls),
    path('mydiary/',include('mydiary.urls')),
    path('accounts/',include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
