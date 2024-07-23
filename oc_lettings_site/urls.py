from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler500

from . import views


def trigger_error(request):
    return 1 / 0


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]

handler500 = 'oc_lettings_site.views.custom_error_500'
