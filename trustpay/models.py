from django.core.validators import EMPTY_VALUES
from django.db import models
from django.utils.translation import ugettext_lazy as _

import trustpay
from client import TrustPayClient
from managers import NotificationManager


class Notification(models.Model):
    TYPE_CRDT = 'CRDT'
    TYPE_DBIT = 'DBIT'
    TYPES = (
        (TYPE_CRDT, _('Credit card')),
        (TYPE_DBIT, _('Debit')),
    )

    ip_address = models.IPAddressField(verbose_name=_(u'IP address'),
        blank=True, null=True, default=None)
    params_get = models.TextField(verbose_name=_(u'GET params'))
    params_post = models.TextField(verbose_name=_(u'POST params'))

    aid = models.CharField(verbose_name=_(u'Merchant account ID'), max_length=10)
    type = models.CharField(verbose_name=_(u'Type of transaction'), max_length=4, choices=TYPES)
    amount = models.CharField(verbose_name=_(u'Amount of the payment'), max_length=16)
    currency = models.CharField(verbose_name=_(u'Currency of the payment'), max_length=3)
    reference = models.CharField(verbose_name=_(u'Reference'), max_length=500)
    result = models.CharField(verbose_name=_(u'Result'), max_length=32, choices=trustpay.RESULTS)
    signature = models.CharField(verbose_name=_(u'Signature'), max_length=64)
    transaction_id = models.CharField(verbose_name=_(u'TrustPay Transaction ID'), max_length=10)
    order_id = models.CharField(verbose_name=_(u'TrustPay Order ID'), max_length=10)
    is_test = models.BooleanField(verbose_name=_(u'test'))
    is_signed = models.BooleanField(verbose_name=_(u'signed'))
    is_safe = models.BooleanField(verbose_name=_(u'safe'), help_text=_(u'signed and correct signature'))
    created = models.DateTimeField(verbose_name=_(u'created'), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_(u'created'), auto_now=True)
    objects = NotificationManager()

    class Meta:
        db_table = 'trustpay_notifications'
        verbose_name = _(u'notification')
        verbose_name_plural = _(u'notifications')
        ordering = ('-created', )

    def save(self, **kwargs):
        if self.is_test in EMPTY_VALUES:
            # Notification requests from Production environment are sent from IP 81.89.63.16
            # Notification requests from Test environment are sent from IP 81.89.63.19
            self.is_test = self.ip_address != '81.89.63.16'

        if self.is_signed in EMPTY_VALUES:
            self.is_signed = self.signature not in EMPTY_VALUES

        self.is_safe = TrustPayClient(is_test=self.is_test).check_trustpay_signature(
            self.signature, self.trustpay_signature)

        return super(Notification, self).save(**kwargs)

    @property
    def merchant_signature(self):
        return TrustPayClient(is_test=self.is_test).create_merchant_signature(
            self.aid, self.amount, self.currency, self.reference)

    @property
    def trustpay_signature(self):
        tss = 'Y' if self.is_signed else 'N'
        return TrustPayClient(is_test=self.is_test).create_trustpay_signature(
            self.aid, self.type, self.amount, self.currency, self.reference, self.result, self.transaction_id,
            self.order_id, tss
        )
