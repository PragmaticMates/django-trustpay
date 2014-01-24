from django.conf.urls import patterns, url

from views import SuccessReturnView, ErrorReturnView, CancelReturnView, NotificationView


urlpatterns = patterns('',
    url(r'success-return/$', SuccessReturnView.as_view(), name='trustpay_success_return'),
    url(r'error-return/$', ErrorReturnView.as_view(), name='trustpay_error_return'),
    url(r'cancel-return/$', CancelReturnView.as_view(), name='trustpay_cancel_return'),
    url(r'notification/$', NotificationView.as_view(), name='trustpay_notification'),
)
