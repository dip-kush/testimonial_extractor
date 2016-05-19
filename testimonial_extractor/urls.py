from django.conf.urls import patterns, include, url
from views import start,sample, weasyprint_pdf
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testimonial_extractor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^roll/', start),
    url(r'^sample', sample),
    url(r'^pdf/(?P<rollno>.+)', weasyprint_pdf),
)
