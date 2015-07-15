"""
Tagulous test app urls

Usage:
    class MyTestCase(TestCase):
        urls = 'tagulous.tests.app.urls'
"""

try:
    from django.conf.urls.defaults import include, patterns, url
except ImportError:
    from django.conf.urls import include, patterns, url

from tagulous.tests.app import models


urlpatterns = patterns('',
    url(r'^tagulous_tests_app/', include(patterns('',
        url(r'^autocomplete/SingleTagFieldOptionsModel/$',
            'tagulous.views.autocomplete',
            {'tag_model': models.SingleTagFieldOptionsModel},
            name='tagulous_tests_app-SingleTagFieldOptionsModel',
        ),
        url(r'^autocomplete/TagFieldOptionsModel/$',
            'tagulous.views.autocomplete',
            {'tag_model': models.TagFieldOptionsModel},
            name='tagulous_tests_app-TagFieldOptionsModel',
        ),
    )))
)
