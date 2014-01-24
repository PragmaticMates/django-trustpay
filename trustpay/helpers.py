from django.utils import translation

import trustpay


def get_result_message(result_code):
    return dict(trustpay.RESULTS).get(result_code, result_code)


def get_language_code(request):
    try:
        language_code = request.LANGUAGE_CODE
    except AttributeError:
        language_code = translation.get_language()

    if language_code:
        if len(language_code) > 3:
            for delimiter in ['_', '-']:
                if delimiter in language_code:
                    language_code = language_code.split(delimiter)[0]
        language_code = language_code.lower()
        if language_code not in trustpay.SUPPORTED_LANGUAGES:
            return None
    return language_code
