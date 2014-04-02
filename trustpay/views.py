from django.http import HttpResponse
from django.views.generic import View, TemplateView

from helpers import get_result_message
from models import Notification


class SuccessReturnView(TemplateView):
    template_name = 'trustpay/success_return.html'


class ErrorReturnView(TemplateView):
    template_name = 'trustpay/error_return.html'

    def get_context_data(self, **kwargs):
        context_data = super(ErrorReturnView, self).get_context_data(**kwargs)
        context_data['error_message'] = get_result_message(self.request.GET.get('RES', None))
        return context_data


class CancelReturnView(TemplateView):
    template_name = 'trustpay/cancel_return.html'


class NotificationView(View):
    def dispatch(self, request, *args, **kwargs):
        Notification.objects.create_from_request(request)
        return HttpResponse()
