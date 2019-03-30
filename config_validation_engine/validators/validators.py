from yamale.validators import DefaultValidators, Validator
from email.utils import parseaddr
from .constraints import EmailDomain, Ipv4Constraint
from validate_email import validate_email
from urlparse import urlparse
from math import ceil, floor
import re

class Email(Validator):
    """Email Validator"""
    constraints = [EmailDomain]
    tag = 'email'

    def _is_valid(self,value):
        if ((str == type(value)) & (validate_email(value) == True)):
            return True
        else:
            return False

    def fail(self,value):
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

class Domain(Validator):
    """Domain Validator"""
    tag = 'domain'

    def _is_valid(self, value):
        m = re.match("[A-Za-z0-9_]{1,256}.[A-Za-z0-9_]{1,256}.[A-Za-z0-9_]{1,256}",
                value)
        if m:
            return True
        else:
            return False

    def fail(self, value):
        return '\'%s\' is not a valid %s value. The acceptable range of values is %s' % (value, self.tag, 'lightweight_component01.cern.ch')

class IpV4(Validator):
    """IPV4 address validator"""
    constraints = [Ipv4Constraint]
    tag = 'ipv4'

    def _is_valid(self, value):
        m = re.match("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", value)
        if m:
            return True
        else:
            return False

    def fail(self, value):
        return '\'%s\' is not a valid %s value. The acceptable range of values is %s' % (value, self.tag, '0.0.0.0 to 255.255.255.255')


def all_config_validators():
    validators = DefaultValidators.copy()
    validators[Email.tag] = Email
    validators[Longitude.tag] = Longitude
    validators[Latitude.tag] = Latitude
    validators[URL.tag] = URL
    validators[Domain.tag] = Domain
    validators[IpV4.tag] = IpV4
    return validators
