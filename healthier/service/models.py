import datetime

from django.db import models
from django.utils.timezone import now
from config.utils import generate_id
from healthier.consumers.models import Consumer
from healthier.providers.models import Provider
from django_prices.models import MoneyField
from annoying.fields import JSONField

DAYS_AVAILABLE_TUPLE = (
    ('EVR', 'EVERYDAY'),
    ('MON', 'MONDAYS'),
    ('TUE', 'TUESDAYS',),
    ('WED', 'WEDNESDAYS'),
    ('THU', 'THURSDAYS'),
    ('FRI', 'FRIDAYS'),
    ('SAT', 'SATURDAYS'),
    ('SUN', 'SUNDAYS')
)


class ServiceGroupCategory(models.Model):
    category_name = models.CharField(max_length=200)
    category_description = models.TextField(max_length=1000)

    def __str__(self):
        return self.category_name


class ServiceGroup(models.Model):
    """Initial services for providers to use as template"""
    group_name = models.CharField(max_length=200)
    category = models.ForeignKey(ServiceGroupCategory, on_delete=models.CASCADE)
    group_description = models.CharField(max_length=1000)

    def __str__(self):
        """Return a string representation of the model."""
        return self.group_name


class HealthierService(models.Model):
    group = models.ForeignKey(ServiceGroup, on_delete=models.CASCADE, blank=True, null=True)
    service_name = models.CharField(max_length=200)
    details = models.CharField(max_length=1000, blank=False, default='')
    service_id = models.CharField(max_length=200, default=generate_id("service"))
    orders = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.service_name


class OrderedService(models.Model):
    """A paid for service request to the service organization"""
    ordered_by = models.ForeignKey(Consumer, on_delete=models.CASCADE, null=True)
    service = models.OneToOneField(HealthierService, on_delete=models.CASCADE, null=True)
    provided_by = models.ForeignKey(Provider, on_delete=models.CASCADE, blank=True, null=True)
    payment_status = models.BooleanField(default=False)
    order_id = models.CharField(max_length=200, default=generate_id("order"))
    promo_code = models.CharField(max_length=200)
    order_date = models.DateTimeField(auto_now=False, default=now)
    price = MoneyField(currency='NGN', decimal_places=2, max_digits=12, default=0.00)
    cancellation_time = models.CharField(default='', max_length=50)
    arrival_time = models.CharField(default='', max_length=50)
    arrival_date = models.CharField(default='', max_length=50)
    members = JSONField(default='', max_length=300)
    comment = models.TextField(default='', max_length=1000)
    is_active = models.BooleanField(default=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        """Return a string representation of the model."""
        return "Service Ordered by : {0}".format(self.ordered_by_id)


class ServiceRequests(models.Model):
    """A paid for service request to the service organization"""
    request_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=now)
    requested_by = models.ForeignKey(Provider, on_delete=models.CASCADE)
    price = MoneyField(currency='NGN', decimal_places=2, max_digits=12, default=0.00)
    service = models.ForeignKey(HealthierService, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    days_available = models.CharField(max_length=200, choices=DAYS_AVAILABLE_TUPLE, default='EVR')
    start_time_available = models.TimeField(max_length=200, default=datetime.time(16, 00))
    end_time_available = models.TimeField(max_length=200, default=datetime.time(16, 00))
    provision_description = models.TextField(max_length=500, default='')
    status = models.BooleanField(default=True)

    def __str__(self):
        """Return a string representation of the model."""
        return str(self.service)


class ServiceReport(models.Model):
    generated_on = models.DateTimeField(default=now)
    generated_for = models.ForeignKey(OrderedService)
    report_file = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True)
    lower_range_measured = models.CharField(max_length=200)
    upper_range_measured = models.CharField(max_length=200)
    measured_value_value = models.CharField(max_length=200)
    measured_value_key = models.CharField(max_length=200)
    fillers_name = models.CharField(max_length=500, blank=False)
    fillers_designation = models.CharField(max_length=300, blank=False)
    report_summary = models.CharField(max_length=500, blank=False)
    service_rendering_date = models.CharField(max_length=500, blank='')

    def __str__(self):
        return self.report_summary

    @property
    def file_url(self):
        if self.report_file and hasattr(self.report_file, 'url'):
            return self.report_file.url


class SuggestService(models.Model):
    service_name = models.CharField(max_length=300, default='', blank=False)
    service_group = models.CharField(max_length=300, default='', blank=False)
    service_description = models.CharField(max_length=3000, default='', blank=False)
    service_suggestion_reason = models.CharField(max_length=3000, default='', blank=False)

    def __str__(self):
        return "Suggested service: {}".format(self.service_name)
