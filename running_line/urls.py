from django.urls import path
from .views import serve_video, static_page

app_name = 'running_line'

urlpatterns = [
    path('page/', static_page, name='static_page'),
    path('video/', serve_video, name='serve_video'),
]
