from django.shortcuts import render

# Create your views here.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', include('test.urls', namespace='test'))

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
