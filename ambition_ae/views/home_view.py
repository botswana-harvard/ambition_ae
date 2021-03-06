from django.views.generic.base import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin


class HomeView(EdcBaseViewMixin, TemplateView):

    template_name = 'ambition_ae/home.html'
