from django.urls import include, path, re_path
from coco_app import views

app_name = 'coco_app'
urlpatterns = [
    path('',views.home_page, name = 'home_page'),
]
