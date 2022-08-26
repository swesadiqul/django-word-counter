from django.urls import path
from . import views
# from . import context_processors

urlpatterns = [
	path('', views.home, name="home"),
	path('blog/', views.blog, name="blog"),
	# path('counter/', context_processors.counter, name='counter'),
]
