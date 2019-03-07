from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home/', views.home, name='home'),
    path('list/', views.list, name='list'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('write/', views.write, name='write'),
    path('create/', views.create, name='create'),
    path('newblog/', views.blogpost, name="newblog"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
