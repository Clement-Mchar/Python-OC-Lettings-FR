from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404, handler500
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("admin/", admin.site.urls),
]

handler404 = "oc_lettings_site.views.page_not_found"
handler500 = "oc_lettings_site.views.server_error"
