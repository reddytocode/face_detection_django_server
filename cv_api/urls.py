"""cv_api URL Configuration"""
from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from face_detector import views as face_det
urlpatterns = [
    url(r'face_detection/detect/$', face_det.detect),
    url(r'admin', admin.site.urls)
]
# curl -X POST 'http://localhost:8000/face_detection/detect/' -d 'url=https://www.pyimagesearch.com/wp-content/uploads/2015/05/obama.jpg' ; echo ""

"""
urlpatterns = patterns('',
    url(r'^face_detection/detect/$', 'face_detector.views.detect'),
    url(r'^admin/', include(admin.site.urls)),
)
"""