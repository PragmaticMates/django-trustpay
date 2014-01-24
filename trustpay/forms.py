from django import forms


class TrustPayForm(forms.Form):
    action_url = None

    # required fields
    AID = forms.CharField(required=True, widget=forms.HiddenInput(), max_length=10)  # Merchant account ID assigned by TrustPay
    AMT = forms.DecimalField(required=True, widget=forms.HiddenInput(), decimal_places=2)  # Amount of the payment exactly 2 decimal places
    CUR = forms.CharField(required=True, widget=forms.HiddenInput(), max_length=3)  # Currency of the payment same as currency of merchant account
    REF = forms.CharField(required=True, widget=forms.HiddenInput(), max_length=500)  # Reference, Merchant's payment identification
    SIG = forms.CharField(required=True, widget=forms.HiddenInput(), max_length=64)  # Data sign

    # not required fields
    URL = forms.CharField(widget=forms.HiddenInput(), max_length=256)  # Return URL overrides any default Return URL, can be overridden further by RURL, CURL, EURL
    RURL = forms.CharField(widget=forms.HiddenInput(), max_length=256)  # Return URL overrides default Success Return URL
    CURL = forms.CharField(widget=forms.HiddenInput(), max_length=256)  # Return URL overrides default Cancel Return URL
    EURL = forms.CharField(widget=forms.HiddenInput(), max_length=256)  # Return URL overrides default Error Return URL
    NURL = forms.CharField(widget=forms.HiddenInput(), max_length=256)  # Notification URL overrides default Notification URL
    LNG = forms.CharField(widget=forms.HiddenInput(), max_length=2)  # Language
    CNT = forms.CharField(widget=forms.HiddenInput(), max_length=2)  # Country
    DSC = forms.CharField(widget=forms.HiddenInput(), max_length=256)  # Description, free text that will be displayed to the user
    EMA = forms.EmailField(widget=forms.HiddenInput(), max_length=254)  # Customer email, prefills the email address fields for the customer when redirected to TrustPay
