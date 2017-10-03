from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .views import DashboardView, FinancesView, CustomerListView, AccountSettingsView,\
    ServiceConfiguration, ProfileView, ServiceRequestConfiguration, UserServicesListView, AllServiceListView, \
    ServiceDetailView, SuggestServiceView

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'profile^$', ProfileView.as_view(), name='profile'),
    url(r'^finances$', FinancesView.as_view(), name='finance'),
    url(r'^customers$', CustomerListView.as_view(), name='customers'),
    url(r'^services(?P<service_id>\d+)$', ServiceDetailView.as_view(), name='service_details'),
    url(r'^services/me$', UserServicesListView.as_view(),
        name='dashboard_my_services'),
    url(r'^services/all$', AllServiceListView.as_view(),
        name='dashboard_all_services'),
    url(r'^service/report$', AccountSettingsView.as_view(), name='service_report'),
    url(r'^service/render', login_required(ServiceRequestConfiguration.as_view()),
        name='service_request_configuration'),
    url(r'^service/configure$', login_required(ServiceConfiguration.as_view()),
        name='service_configuration'),
    url(r'^services/suggest_new$', SuggestServiceView.as_view(),
        name='dashboard_suggest_new_service'),
    url(r'^settings/account$', AccountSettingsView.as_view(),
        name='account_settings'),
    url(r'^settings/finance$', AccountSettingsView.as_view(), name='finance_settings'),
    url(r'^settings/consumer$', AccountSettingsView.as_view(), name='consumer_settings'),
    url(r'^settings/service$', AccountSettingsView.as_view(), name='service_settings'),
]