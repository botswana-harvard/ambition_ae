from django.db import models
from edc_base.model_validators.date import date_not_future
from edc_base.utils import get_utcnow
from edc_constants.constants import NOT_APPLICABLE

from ..choices import AE_GRADE, AE_INTENSITY


class AeModelMixin(models.Model):

    ae_auto_created = models.BooleanField(
        max_length=25,
        default=False,
        editable=False)

    ae_auto_created_criteria = models.CharField(
        max_length=50,
        default=NOT_APPLICABLE,
        editable=False)

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow)

    ae_description = models.TextField(
        verbose_name='Adverse Event (AE) description')

    ae_awareness_date = models.DateField(
        verbose_name='AE Awareness date',
        default=get_utcnow,
        validators=[date_not_future])

    ae_start_date = models.DateField(
        verbose_name='Actual Start Date of AE',
        default=get_utcnow,
        validators=[date_not_future])

    ae_grade = models.CharField(
        verbose_name='Severity of AE',
        max_length=25,
        choices=AE_GRADE)

    ae_intensity = models.CharField(
        verbose_name='What is the intensity AE',
        max_length=25,
        choices=AE_INTENSITY)

    class Meta:
        abstract = True
