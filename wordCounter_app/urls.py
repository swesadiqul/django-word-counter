from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('blog/', views.blog, name="blog"),
	path('ajax-posting', views.ajax_posting, name='ajax_posting'),
]
