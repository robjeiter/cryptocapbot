from django.conf.urls import include, url
from sapp import views
from .views import tbotview
from django.contrib import admin
from sapp.views import get_price

urlpatterns = [
	#url(r'^$',views.index,name='index'),
	url(r'^asdf123456/?$', tbotview.as_view()),
	url(r'^admin/', admin.site.urls),
	url(r'^trigger/', views.get_price, name='trigger'),
]