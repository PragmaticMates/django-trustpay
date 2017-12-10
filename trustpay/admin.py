# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ['id', 'transaction_id', 'result', 'amount_and_currency', 'reference', 'signature',
                    #'trustpay_signature', 'merchant_signature',
                    'is_live', 'is_signed', 'is_safe', 'created']
    list_filter = ['result', 'currency', 'is_test', 'is_signed', 'is_safe',]
    search_fields = ['params_get', 'params_post']

    def has_add_permission(self, request):
        return False

    def amount_and_currency(self, obj):
        return '%s %s' % (obj.amount, obj.currency)

    def is_live(self, obj):
        return not obj.is_test
    is_live.boolean = True
    is_live.short_description = _('Live')


admin.site.register(Notification, NotificationAdmin)
