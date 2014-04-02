django-trustpay
===============

Django app for TrustPayClient payment gateway API.

Tested on Django 1.4.5.


Requirements
------------
- Django


Recommendations
---------------
- django-detective (It is useful, but no necessary. It tracks all site requests.)



Installation
------------

1. Install python library using pip: ``pip install django-trustpay``

2. Add ``trustpay`` to ``INSTALLED_APPS`` in your Django settings file

3. Add ``trustpay.urls`` to ``urls.py`` in your Django project

4. Set ``HOST_URL`` to be your host name with http/https protocol prefix. For example: ``https://www.mysite.com``

5. Set TrustPay settings. See below.

6. Sync your database



Settings
--------
TRUSTPAY_AID_TEST
    Client's AID for TEST environment.

TRUSTPAY_AID_LIVE
    Client's AID for LIVE environment.

TRUSTPAY_SECRET_KEY_TEST
    Client's Secret key for TEST environment.

TRUSTPAY_SECRET_KEY_LIVE
    Client's Secret key for LIVE environment.

TRUSTPAY_PAYMENT_SERVICE_URL_TEST
    TrustPay PAYMENT SERVICE URL for TEST environment. Default: ``'https://test.trustpay.eu/mapi/paymentservice.aspx'``

TRUSTPAY_PAYMENT_SERVICE_URL_LIVE
    TrustPay PAYMENT SERVICE URL for LIVE environment. Default: ``'https://ib.trustpay.eu/mapi/paymentservice.aspx'``

TRUSTPAY_CLIENT_REDIRECT_URL_TEST
    TrustPay CLIENT REDIRECT URL for TEST environment. Default: ``'https://test.trustpay.eu/mapi/pay.aspx'``

TRUSTPAY_CLIENT_REDIRECT_URL_LIVE
    TrustPay CLIENT REDIRECT URL for LIVE environment. Default: ``'https://ib.trustpay.eu/mapi/pay.aspx'``

TRUSTPAY_SUCCESS_RETURN_URL
    Success return URL. Default: ``u'%s%s' % (settings.HOST_URL, reverse_lazy('trustpay_success_return'))``

TRUSTPAY_ERROR_RETURN_URL
    Error return URL. Default: ``u'%s%s' % (settings.HOST_URL, reverse_lazy('trustpay_error_return'))``

TRUSTPAY_CANCEL_RETURN_URL
    Cancel return URL. Default: ``u'%s%s' % (settings.HOST_URL, reverse_lazy('trustpay_cancel_return'))``

TRUSTPAY_NOTIFICATION_URL
    Notification URL. Default: ``u'%s%s' % (settings.HOST_URL, reverse_lazy('trustpay_notification'))``

TRUSTPAY_NOTIFICATION_EMAIL
    Notification email. Default: ``ADMINS[0][0] or None``


Usage
-----


Prepare payment data
''''''''''''''''''''
In your checkout view prepare TrustPay payment data::

    trustpay_payment_data = {
        # required
        'amount': 123.45,
        'currency': trustpay.CURRENCY_EUR,
        'reference': u'ORDER-123',  # Don't put # sign in reference. It will be returned back as GET parameter.

        # not required
        'language': get_language_code(request),
        'country': trustpay.COUNTRY_SLOVAK_REPUBLIC,
        'description': u'This is Trustpay test payment',
        'customer_email': u'example@example.net'
    }


and create TrustPay form with hidden fields and 'Pay' submit button::

    trustpayform = TrustPayClient(is_test=settings.DEBUG).get_form(**trustpay_payment_data)


Render payment form
'''''''''''''''''''
Put TrustPay form to your template::

    {% include 'trustpay/helpers/form.html' with form=trustpayform submit_label='Pay with TrustPay' %}


Handle return views
'''''''''''''''''''
By default, ``SuccessReturnView``, ``ErrorReturnView``, ``CancelReturnView`` simply print request data and error message if any.
You should override templates ``trustpay/success_return.html``, ``trustpay/error_return.html`` and
``trustpay/cancel_return.html`` or define your own return views. If you decide to use your own return views,
don't forget to set ``TRUSTPAY_SUCCESS_RETURN_URL``, ``TRUSTPAY_ERROR_RETURN_URL`` and ``TRUSTPAY_CANCEL_RETURN_URL``
settings.


Handle notification view
''''''''''''''''''''''''
``trustpay.views.NotificationView`` stores every notification from TrustPay service to database.
You shouldn't have set BasicAuth or any other authentication on this view (``reverse('trustpay_notification')``),
because TrustPay won't be able to access it.

I recommend you to create a cron job which will handle each safe notification (with flag ``is_safe`` - it means
the payment request from merchant was signed and return signature is correct).


Helpers
'''''''
``get_result_message(result_code)``
    returns result message by result code

``get_language_code(request)``
    returns TrustPay supported language code by request


Constants
'''''''''
``trustpay`` package contains all TrustPay supported currencies and countries.


Authors
-------

Library is by `Erik Telepovsky` from `Pragmatic Mates`_. See `our other libraries`_.

.. _Pragmatic Mates: http://www.pragmaticmates.com/
.. _our other libraries: https://github.com/PragmaticMates
