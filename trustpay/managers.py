from django.db import models
from django.db.models.query import QuerySet


class NotificationQuerySet(QuerySet):
    def create_from_request(self, request):
        #{
        #    u'TYP': [u'CRDT'],
        #    u'CUR': [u'EUR'],
        #    u'RES': [u'0'],
        #    u'OID': [u'0'],
        #    u'AMT': [u'12.40'],
        #    u'SIG': [u'9FC13BFFD2AD2CCF2AEEAE4477342E57180860913A93E5CAEBB175C987E43D53'],
        #    u'TID': [u'32209'],
        #    u'AID': [u'2107900972'],
        #    u'REF': [u'Test'],
        #    u'TSS': [u'N']
        #}

        # IP address
        ip = request.META.get('HTTP_X_FORWARDED_FOR', None)
        if ip:
            # X_FORWARDED_FOR returns client1, proxy1, proxy2,...
            ip = ip.split(', ')[0]
        else:
            ip = request.META.get('REMOTE_ADDR', None)

        return self.create(
            ip_address=ip,
            params_get=str(dict(request.GET)),
            params_post=str(dict(request.POST)),
            aid=request.GET.get('AID'),
            type=request.GET.get('TYP'),
            amount=request.GET.get('AMT'),
            currency=request.GET.get('CUR'),
            reference=request.GET.get('REF'),
            result=request.GET.get('RES'),
            signature=request.GET.get('SIG'),
            transaction_id=request.GET.get('TID'),
            order_id=request.GET.get('OID'),
            is_test=None,
            is_signed=request.GET.get('TSS') == 'Y',
            is_safe=None
        )


class NotificationManager(models.Manager):
    #######################
    # PROXIES TO QUERYSET #
    #######################
    def get_query_set(self):
        return NotificationQuerySet(self.model, using=self._db)

    def create_from_request(self, request):
        return self.get_query_set().create_from_request(request)
