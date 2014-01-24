from django.contrib import admin

from models import Notification


class NotificationAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ['id', 'transaction_id', 'result', 'amount_and_currency', 'reference', 'signature',
                    #'trustpay_signature', 'merchant_signature',
                    'is_test', 'is_signed', 'is_safe', 'created']
    list_filter = ['result', 'currency', 'is_test', 'is_signed', 'is_safe',]
    search_fields = ['params_get', 'params_post']

    def has_add_permission(self, request):
        return False

    def amount_and_currency(self, obj):
        return u'%s %s' % (obj.amount, obj.currency)


admin.site.register(Notification, NotificationAdmin)

