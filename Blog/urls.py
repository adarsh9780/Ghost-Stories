from django.conf.urls import url
from .views import IndexPage, ContactPage, AboutPage

app_name = 'Blog'

urlpatterns = [
	url(r'^$', IndexPage.as_view(), name='Blog'),
	url(r'^contact/$', ContactPage.as_view(), name="contact"),
	url(r'^about/$', AboutPage.as_view(), name="about"),
]