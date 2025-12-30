from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include("apps.auth.urls", namespace="auth")),
    path('api/users/', include("apps.users.urls", namespace="users"))
]
