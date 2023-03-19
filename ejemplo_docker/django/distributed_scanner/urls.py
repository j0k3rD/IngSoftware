
from django.urls import re_path
from django.contrib import admin

from scanner.views import ScanView

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^scan/', ScanView.as_view()),
]