import hashlib
import hmac

from forms import TrustPayForm


class TrustPayClient(object):
    is_test = False

    def __init__(self, is_test):
        import settings
        self.is_test = is_test
        self.AID = settings.TRUSTPAY_AID_TEST if is_test else settings.TRUSTPAY_AID_LIVE
        self.PAYMENT_SERVICE_URL = settings.TRUSTPAY_PAYMENT_SERVICE_URL_TEST if is_test else settings.TRUSTPAY_PAYMENT_SERVICE_URL_LIVE
        self.CARD_PAYMENTS_URL = settings.TRUSTPAY_CARD_PAYMENTS_URL_TEST if is_test else settings.TRUSTPAY_CARD_PAYMENTS_URL_LIVE
        self.AID = settings.TRUSTPAY_AID_TEST if is_test else settings.TRUSTPAY_AID_LIVE
        self.SECRET_KEY = settings.TRUSTPAY_SECRET_KEY_TEST if is_test else settings.TRUSTPAY_SECRET_KEY_LIVE

    def create_merchant_signature(self, aid, amount, currency, reference):
        # A message is created as concatenation of parameter values in this specified order:
        # Merchant redirect to TrustPay: AID, AMT, CUR, and REF

        message = unicode(aid)
        message += unicode(amount)
        message += unicode(currency)
        message += unicode(reference)
        return self.sign(message)

    def create_trustpay_signature(self, aid, typ, amt, cur, ref, res, tid, oid, tss):
        # A message is created as concatenation of parameter values in this specified order:
        # TrustPay notification to Merchant: AID, TYP, AMT, CUR, REF, RES, TID, OID and TSS

        message = unicode(aid)
        message += unicode(typ)
        message += unicode(amt)
        message += unicode(cur)
        message += unicode(ref)
        message += unicode(res)
        message += unicode(tid)
        message += unicode(oid)
        message += unicode(tss)

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

    def get_form(self, amount, currency, reference, language=None, country=None, description=None, customer_email=None, card_payment=False):
        import settings
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
        form.action_url = self.CARD_PAYMENTS_URL if card_payment else self.PAYMENT_SERVICE_URL
        return form
