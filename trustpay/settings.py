from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse_lazy


# Site debug
TRUSTPAY_DEBUG = getattr(settings, 'DEBUG', False)

# Client's AID for TEST environment
TRUSTPAY_AID_TEST = getattr(settings, 'TRUSTPAY_AID_TEST', None)

# Client's AID for LIVE environment
TRUSTPAY_AID_LIVE = getattr(settings, 'TRUSTPAY_AID_LIVE', None)

# Client's Secret key for TEST environment
TRUSTPAY_SECRET_KEY_TEST = getattr(settings, 'TRUSTPAY_SECRET_KEY_TEST', None)

# Client's Secret key for LIVE environment
TRUSTPAY_SECRET_KEY_LIVE = getattr(settings, 'TRUSTPAY_SECRET_KEY_LIVE', None)

# TrustPay PAYMENT SERVICE URL for TEST environment
TRUSTPAY_PAYMENT_SERVICE_URL_TEST = getattr(settings, 'TRUSTPAY_API_URL_TEST', 'https://test.trustpay.eu/mapi/paymentservice.aspx')

# TrustPay PAYMENT SERVICE URL for LIVE environment
TRUSTPAY_PAYMENT_SERVICE_URL_LIVE = getattr(settings, 'TRUSTPAY_API_URL_LIVE', 'https://ib.trustpay.eu/mapi/paymentservice.aspx')

# TrustPay CLIENT REDIRECT URL for TEST environment
TRUSTPAY_CLIENT_REDIRECT_URL_TEST = getattr(settings, 'TRUSTPAY_API_URL_TEST', 'https://test.trustpay.eu/mapi/pay.aspx')

# TrustPay CLIENT REDIRECT URL for LIVE environment
TRUSTPAY_CLIENT_REDIRECT_URL_LIVE = getattr(settings, 'TRUSTPAY_API_URL_LIVE', 'https://ib.trustpay.eu/mapi/pay.aspx')

try:
    # Success return URL
    TRUSTPAY_SUCCESS_RETURN_URL = getattr(settings, 'TRUSTPAY_SUCCESS_RETURN_URL', u'%s%s' % (settings.HOST_URL, reverse_lazy('trustpay_success_return')))

    # Error return URL
    TRUSTPAY_ERROR_RETURN_URL = getattr(settings, 'TRUSTPAY_ERROR_RETURN_URL', u'%s%s' % (settings.HOST_URL, reverse_lazy('trustpay_error_return')))

    # Cancel return URL
    TRUSTPAY_CANCEL_RETURN_URL = getattr(settings, 'TRUSTPAY_CANCEL_RETURN_URL', u'%s%s' % (settings.HOST_URL, reverse_lazy('trustpay_cancel_return')))

    # Notification URL
    TRUSTPAY_NOTIFICATION_URL = getattr(settings, 'TRUSTPAY_NOTIFICATION_URL', u'%s%s' % (settings.HOST_URL, reverse_lazy('trustpay_notification')))
except AttributeError as e:
    raise ImproperlyConfigured(e)


# Notification email
try:
    TRUSTPAY_NOTIFICATION_EMAIL = getattr(settings, 'TRUSTPAY_NOTIFICATION_EMAIL', settings.ADMINS[0][0])
except (IndexError, AttributeError):
    TRUSTPAY_NOTIFICATION_EMAIL = None
