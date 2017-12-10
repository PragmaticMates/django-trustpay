# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib
import hmac

from django.utils.encoding import force_text

from .forms import TrustPayForm


class TrustPayClient(object):
    is_test = False

    def __init__(self, is_test):
        from . import settings
        self.is_test = is_test
        self.AID = settings.TRUSTPAY_AID_TEST if is_test else settings.TRUSTPAY_AID_LIVE
        self.PAYMENT_SERVICE_URL = settings.TRUSTPAY_PAYMENT_SERVICE_URL_TEST if is_test else settings.TRUSTPAY_PAYMENT_SERVICE_URL_LIVE
        self.CLIENT_REDIRECT_URL = settings.TRUSTPAY_CLIENT_REDIRECT_URL_TEST if is_test else settings.TRUSTPAY_CLIENT_REDIRECT_URL_LIVE
        self.AID = settings.TRUSTPAY_AID_TEST if is_test else settings.TRUSTPAY_AID_LIVE
        self.SECRET_KEY = settings.TRUSTPAY_SECRET_KEY_TEST if is_test else settings.TRUSTPAY_SECRET_KEY_LIVE
        self.ACTION_URL = settings.TRUSTPAY_CLIENT_REDIRECT_URL_TEST if is_test else settings.TRUSTPAY_CLIENT_REDIRECT_URL_LIVE


    def create_merchant_signature(self, aid, amount, currency, reference):
        # A message is created as concatenation of parameter values in this specified order:
        # Merchant redirect to TrustPay: AID, AMT, CUR, and REF

        message = force_text(aid)
        message += force_text(amount)
        message += force_text(currency)
        message += force_text(reference)
        return self.sign(message)

    def create_trustpay_signature(self, aid, typ, amt, cur, ref, res, tid, oid, tss):
        # A message is created as concatenation of parameter values in this specified order:
        # TrustPay notification to Merchant: AID, TYP, AMT, CUR, REF, RES, TID, OID and TSS

        message = force_text(aid)
        message += force_text(typ)
        message += force_text(amt)
        message += force_text(cur)
        message += force_text(ref)
        message += force_text(res)
        message += force_text(tid)
        message += force_text(oid)
        message += force_text(tss)

        return self.sign(message)

    def check_trustpay_signature(self, signature, trustpay_signature):
        return trustpay_signature == signature

    def sign(self, message):
        try:
            key = self.SECRET_KEY

            # HMAC-SHA-256 code (32 bytes) is generated using a key obtained from TrustPay
            code = hmac.new(key, message, hashlib.sha256)

            # Then the code is converted to a string to be a hexadecimal representation of the code
            hex = code.hexdigest()

            # Return 64 upper chars
            return hex.upper()
        except TypeError:
            return None

    def get_form(self, amount, currency, reference, language=None, country=None, description=None, customer_email=None):
        from . import settings
        initial = {
            'AID': self.AID,
            'AMT': amount,
            'CUR': currency,
            'REF': reference,
            'SIG': self.create_merchant_signature(self.AID, amount, currency, reference),
            #'URL': None  # unimportant,
            'RURL': settings.TRUSTPAY_SUCCESS_RETURN_URL,
            'CURL': settings.TRUSTPAY_CANCEL_RETURN_URL,
            'EURL': settings.TRUSTPAY_ERROR_RETURN_URL,
            'NURL': settings.TRUSTPAY_NOTIFICATION_URL,
            'LNG': language,
            'CNT': country,
            'DSC': description,
            'EMA': customer_email
        }
        form = TrustPayForm(initial=initial)
        form.action_url = self.ACTION_URL
        return form
