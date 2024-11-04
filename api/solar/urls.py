from django.urls import path
from solar.views import CreateView


urlpatterns = [
    path("solar/", CreateView.as_view(), name="solar"),
]