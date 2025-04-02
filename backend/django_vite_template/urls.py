from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index_view # Import your view serving base.html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    # Frontend Catch-all (serves the Vue app)
    # IMPORTANT: This must come AFTER admin and API routes
    # It matches any path that does NOT start with 'admin/', 'api/', 'static/', or 'media/'
    # Adjust the prefixes (e.g., 'api/') if your API lives elsewhere.
    re_path(r'^(?!api/|admin/|static/|media/).*$', index_view, name='index'),
]

# 4. Static and Media files (DEBUG mode only)
if settings.DEBUG:
    # Serve static files using Django's static serve view
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # Serve media files (user uploads) using Django's static serve view
    # Ensure MEDIA_URL and MEDIA_ROOT are set in settings.py if you use this
    if hasattr(settings, 'MEDIA_URL') and settings.MEDIA_URL:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
