from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple

from ..admin_site import ambition_ae_admin
from ..forms import AeInitialForm
from ..models import AeInitial
from .modeladmin_mixins import ModelAdminMixin


@admin.register(AeInitial, site=ambition_ae_admin)
class AeInitialAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = AeInitialForm

    fieldsets = (
        (None, {
            'fields': (
                'tracking_identifier',
                'subject_identifier',
                'regimen',
                'report_datetime',
                'ae_description',
                'ae_awareness_date',
                'ae_start_date',
                'ae_grade',
                'ae_intensity',
                'ae_study_relation_possibility',
                'ambisome_relation',
                'fluconazole_relation',
                'amphotericin_b_relation',
                'flucytosine_relation',
                'details_last_study_drug',
                'med_administered_datetime',
                'ae_cause',
                'ae_cause_other',
                'ae_treatment',
                'ae_cm_recurrence',
                'sae',
                'sae_reason',
                'susar',
                'susar_reported',
                'tmg_report_datetime')},
         ),
        audit_fieldset_tuple
    )

    radio_fields = {
        'ae_grade': admin.VERTICAL,
        'ae_intensity': admin.VERTICAL,
        'ae_study_relation_possibility': admin.VERTICAL,
        'ambisome_relation': admin.VERTICAL,
        'fluconazole_relation': admin.VERTICAL,
        'amphotericin_b_relation': admin.VERTICAL,
        'flucytosine_relation': admin.VERTICAL,
        'ae_cause': admin.VERTICAL,
        'ae_cm_recurrence': admin.VERTICAL,
        'sae': admin.VERTICAL,
        'sae_reason': admin.VERTICAL,
        'susar': admin.VERTICAL,
        'susar_reported': admin.VERTICAL}

    ordering = ['-tracking_identifier']

    list_display = ['identifier', 'dashboard',
                    'ae_awareness_date', 'ae_grade', 'sae', 'sae_reason',
                    'susar', 'susar_reported']

    list_filter = ['ae_awareness_date', 'ae_grade',
                   'ae_intensity', 'sae', 'sae_reason', 'susar',
                   'susar_reported']

    search_fields = ['tracking_identifier', 'subject_identifier']

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj=obj)
        return fields + ('tracking_identifier', )