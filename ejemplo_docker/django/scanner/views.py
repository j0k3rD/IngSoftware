from django.views.generic import TemplateView
from django.http import HttpResponse

from .tasks import generate_csv

class ScanView(TemplateView):
    template_name = 'list.html'

    def post(self, request, *args, **kwargs):
        task_id = generate_csv.delay()
        return HttpResponse(task_id)

