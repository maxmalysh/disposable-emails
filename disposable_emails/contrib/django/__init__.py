from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from disposable_emails import is_disposable_email, extract_domain


def disposable_validator(value):
    if is_disposable_email(value):
        raise ValidationError(
            _('%(value)s is a blacklisted email provider'),
            params={'value': extract_domain(value)},
        )
