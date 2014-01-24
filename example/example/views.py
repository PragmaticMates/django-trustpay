from django.conf import settings
from django.views.generic import FormView

import trustpay
from trustpay.client import TrustPayClient
from trustpay.helpers import get_language_code


class HomeView(FormView):
    template_name = 'example/home.html'

    def dispatch(self, request, *args, **kwargs):
        self.trustpay_payment_data = {
            'amount': 123.45,
            'currency': trustpay.CURRENCY_EUR,
            'reference': u'ORDER-123',  # Don't put # sign in reference
            'language': get_language_code(request),
            'country': trustpay.COUNTRY_SLOVAK_REPUBLIC,
            'description': u'This is Trustpay test payment',
            'customer_email': u'example@example.net'
        }
        return super(HomeView, self).dispatch(request, *args, **kwargs)

    def get_form(self, form_class):
        return TrustPayClient(is_test=settings.DEBUG).get_form(**self.trustpay_payment_data)

    def get_context_data(self, **kwargs):
        context_data = super(HomeView, self).get_context_data(**kwargs)
        context_data['trustpay_payment_data'] = self.trustpay_payment_data
        return context_data
