from django.utils.translation import ugettext_lazy as _


# returned via redirect, email notification, http notification
RESULT_SUCCESS = '0'
RESULT_AUTHORIZED_ONLY = '5'

# returned only via email notification, http notification
RESULT_ANNOUNCED = '2'
RESULT_AUTHORIZED = '3'
RESULT_PROCESSING = '4'

# returned only via redirect
RESULT_PENDING = '1'
RESULT_INVALID_REQUEST = '1001'
RESULT_UNKNOWN_ACCOUNT = '1002'
RESULT_MERCHANT_ACCOUNT_DISABLED = '1003'
RESULT_INVALID_SIGN = '1004'
RESULT_USER_CANCEL = '1005'
RESULT_INVALID_AUTHENTICATION = '1006'
RESULT_DISPOSABLE_BALANCE = '1007'
RESULT_SERVICE_NOT_ALLOWED = '1008'
RESULT_PAYSAFECARD_TIMEOUT = '1009'
RESULT_GENERAL_ERROR = '1100'
RESULT_UNSUPPORTED_CURRENCY_CONVERSION = '1101'

RESULTS = (
    (RESULT_SUCCESS, _(u'Success')),
    (RESULT_PENDING, _(u'Pending')),
    (RESULT_ANNOUNCED, _(u'Announced')),
    (RESULT_AUTHORIZED, _(u'Authorized')),
    (RESULT_PROCESSING, _(u'Processing')),
    (RESULT_AUTHORIZED_ONLY, _(u'Authorized only')),
    (RESULT_INVALID_REQUEST, _(u'Invalid request')),
    (RESULT_UNKNOWN_ACCOUNT, _(u'Unknown account')),
    (RESULT_MERCHANT_ACCOUNT_DISABLED, _(u'Merchant account disabled')),
    (RESULT_INVALID_SIGN, _(u'Invalid sign')),
    (RESULT_USER_CANCEL, _(u'User cancel')),
    (RESULT_INVALID_AUTHENTICATION, _(u'Invalid authentication')),
    (RESULT_DISPOSABLE_BALANCE, _(u'Disposable balance')),
    (RESULT_SERVICE_NOT_ALLOWED, _(u'Service not allowed')),
    (RESULT_PAYSAFECARD_TIMEOUT, _(u'PaySafeCard timeout')),
    (RESULT_GENERAL_ERROR, _(u'General Error')),
    (RESULT_UNSUPPORTED_CURRENCY_CONVERSION, _(u'Unsupported currency conversion'))
)

# Supported currencies
# The following is a list of currencies (according to ISO 4217) supported by TrustPay.

CURRENCY_CZK = 'CZK'  # Czech koruna
CURRENCY_EUR = 'EUR'  # Euro
CURRENCY_GBP = 'GBP'  # Pound Sterling
CURRENCY_HUF = 'HUF'  # Forint
CURRENCY_PLN = 'PLN'  # Zloty
CURRENCY_USD = 'USD'  # US Dollar
CURRENCY_RON = 'RON'  # Romanian new leu
CURRENCY_BGN = 'BGN'  # Bulgarian lev
CURRENCY_HRK = 'HRK'  # Croatian Kuna
CURRENCY_LTL = 'LTL'  # Lithuanian litas
CURRENCY_TRY = 'TRY'  # Turkish lira


# Supported countries
# The following is a list of customer countries (according to ISO 3166-1 alpha-2) supported by TrustPay.
COUNTRY_CZECH_REPUBLIC = 'CZ'
COUNTRY_HUNGARY = 'HU'
COUNTRY_POLAND = 'PL'
COUNTRY_SLOVAK_REPUBLIC = 'SK'
COUNTRY_ESTONIA = 'EE'
COUNTRY_BULGARIA = 'BG'
COUNTRY_ROMANIA = 'RO'
COUNTRY_CROATIA = 'HR'
COUNTRY_LATVIA = 'LV'
COUNTRY_LITHUANA = 'LT'
COUNTRY_SLOVENIA = 'SI'
COUNTRY_TURKEY = 'TR'


# Supported languages
# The following is a list of languages (according to ISO 639-1) supported by TrustPay.
SUPPORTED_LANGUAGES = ['bg', 'bs', 'cs', 'de', 'en', 'es', 'et', 'hr', 'hu', 'it',
                       'lt', 'lv', 'pl', 'ro', 'ru', 'sk', 'sl', 'sr', 'uk']
