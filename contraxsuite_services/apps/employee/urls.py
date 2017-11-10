# Future imports
from __future__ import absolute_import, unicode_literals

# Django imports
from django.conf.urls import url

# Project imports
from apps.common.utils import create_standard_urls
from apps.employee import views
from apps.employee.models import Employee, Employer, EmployerUsage

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2017, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-contraxsuite/blob/1.0.1/LICENSE"
__version__ = "1.0.1"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


# URL pattern list
urlpatterns = []


def register(model, view_types):
    """
    Convenience method for global URL registration.
    :param model:
    :param view_types:
    :return:
    """
    global urlpatterns
    urlpatterns += create_standard_urls(model, views, view_types)


# Register views through helper method
register(Employee, view_types=('list', 'detail'))
register(Employer, view_types=('list', 'detail'))


# Add hard-coded URL mappings
urlpatterns += [
    url(
        r'^employee-provision/$',
        views.ProvisionListView.as_view(),
        name='provision-list',
    ),
    url(
        r'^employee-geo-chart/$',
        views.EmployeeGeoChartView.as_view(),
        name='employee-geo-chart',
    ),
    url(
        r'^employee-timeline-chart/$',
        views.EmployeeTimelineChartView.as_view(),
        name='employee-timeline-chart',
    ),

]
