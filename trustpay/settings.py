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
TRUSTPAY_PAYMENT_SERVICE_URL_TEST = getattr(settings, 'TRUSTPAY_PAYMENT_SERVICE_URL_TEST', 'https://playground.trustpay.eu/mapi/pay.aspx')

# TrustPay PAYMENT SERVICE URL for LIVE environment
TRUSTPAY_PAYMENT_SERVICE_URL_LIVE = getattr(settings, 'TRUSTPAY_PAYMENT_SERVICE_URL_LIVE', 'https://ib.trustpay.eu/mapi/pay.aspx')

# TrustPay CARD PAYMENTS URL for TEST environment
TRUSTPAY_CARD_PAYMENTS_URL_TEST = getattr(settings, 'TRUSTPAY_CARD_PAYMENTS_URL_TEST', 'https://playground.trustpay.eu/mapi5/Card/Pay')

# TrustPay CARD PAYMENTS URL for LIVE environment
TRUSTPAY_CARD_PAYMENTS_URL_LIVE = getattr(settings, 'TRUSTPAY_CARD_PAYMENTS_URL_LIVE', 'https://ib.trustpay.eu/mapi5/Card/Pay')

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
