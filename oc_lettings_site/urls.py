from django.contrib import admin
from django.urls import path

import profiles.views
import lettings.views

urlpatterns = [
    path('', lettings.views.index, name='index'),
    path('lettings/', lettings.views.lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', lettings.views.letting, name='letting'),
    path('profiles/', profiles.views.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profiles.views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
