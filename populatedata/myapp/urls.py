from django.urls import path
from .views import uploadfromhtml, uploadfunction

urlpatterns = [
    path('upload/', uploadfunction, name='upload_csv'),
    path('upload-form/', uploadfromhtml, name='upload_form'),
]
