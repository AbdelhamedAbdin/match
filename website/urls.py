from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('match.urls')),
    path('match_statistics/', include('match_statics.urls')),
    path('admin/', admin.site.urls),
]
