from django.contrib import admin
from django.urls import include, path, re_path
from . import views
import settings
from django.views.static import serve

urlpatterns = [
    path("", views.index, name="index"),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("admin/", admin.site.urls),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]

handler404 = "oc_lettings_site.views.page_not_found"
handler500 = "oc_lettings_site.views.server_error"
