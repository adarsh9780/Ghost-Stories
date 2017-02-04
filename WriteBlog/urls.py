from django.conf.urls import url
from .views import ViewBlogPage, WriteBlogPage
from django.conf import settings
from django.conf.urls.static import static

app_name = 'WriteBlog'

urlpatterns = [
	url(r'^home/$', ViewBlogPage.as_view(), name='home'),
	url(r'^writeblog/$', WriteBlogPage.as_view(), name="writeblog"),
]

# for development purpose only
# django dev. server will serve static files using below urlpatterns.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)