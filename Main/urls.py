from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('about/', views.about, name='about-us'),
    
    path('blog/', views.blog, name='blog-masonry'),
    path('blogsecond/<str:itemSlug>/', views.blog_second, name='standard-blog-post-with-image'),
    
    path('gallery/', views.gallery, name='gallery'),
    path('tour/<str:itemSlug>/', views.tour, name='east-europe'),
    path('tourparis/', views.tourparis, name='paris'),
    path('tourclassic/', views.tourclassic, name='tour-classic-fullwidth'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
