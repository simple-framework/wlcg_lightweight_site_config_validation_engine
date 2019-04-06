from yamale.validators import DefaultValidators, Validator
from .constraints import EmailDomain
from validate_email import validate_email
from urlparse import urlparse
from math import ceil, floor


class Email(Validator):
    """Email Validator"""
    constraints = [EmailDomain]
    tag = 'email'

    def _is_valid(self, value):
        if ((str == type(value)) & (validate_email(value) is True)):
            return True
        return False

    def fail(self, value):
        return '%s is not a valid %s value. The acceptable value is \'%s\'' % (value, self.tag, 'example@cern.ch')


class Latitude(Validator):
    """Latitude Validator"""
    tag = 'latitude'

    def _is_valid(self, value):
        if(all(i in range(-90, 90) for i in [ceil(value), floor(value)])):
            return True
        else:
            return False

    def fail(self, value):
        return '\'%s\' is not a valid %s value. The acceptable range of values is %s' % (value, self.tag, '-90 to 90')


class Longitude(Validator):
    """Longitude Validator"""
    tag = 'longitude'

    def _is_valid(self, value):
        if(all(i in range(-180, 180) for i in [ceil(value), floor(value)])):
            return True
        else:
            return False

    def fail(self, value):
        return '\'%s\' is not a valid %s value. The acceptable range of values is %s' % (value, self.tag, '-180 to 180')


class URL(Validator):
    """URL Validator"""
    tag = 'url'

    def _is_valid(self, value):
        url = urlparse(value)
        if all([url.scheme, url.netloc]):
            return True
        return False


class ipAddress(Validator):
    """IP Address Validator"""
    tag = 'ip_address'

    def _is_valid(self, value):
        return value.count('.') == 3 and all(0 <= int(num) < 256 and ' ' not in num for num in value.rstrip().split('.'))


def all_config_validators():
    validators = DefaultValidators.copy()
    validators[Email.tag] = Email
    validators[Longitude.tag] = Longitude
    validators[Latitude.tag] = Latitude
    validators[URL.tag] = URL
    validators[ipAddress.tag] = ipAddress
    return validators
