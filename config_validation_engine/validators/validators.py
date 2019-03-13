import yamale
from yamale.validators import DefaultValidators, Validator
from email.utils import parseaddr

class Email(Validator):
    """Email Validator"""
    tag = 'email'
    def _is_valid(self,value):
        parseaddr(value)

class Latitude(Validator):
    """Latitude Validator"""
    tag = 'latitude'
    def _is_valid(self,value):
        if(value in range(-90,90)):
            return True
        else:
            return False

    def fail(self, value):
        return '\'%s\' is not a valid %s value. The acceptable range of values is %s' % (value, self.tag, '-90 to 90')

class Longitude(Validator):
    """Longitude Validator"""
    tag = 'longitude'
    def _is_valid(self,value):
        if(value in range(-180,180)):
            return True
        else:
            return False

    def fail(self, value):
        return '\'%s\' is not a valid %s value. The acceptable range of values is %s' % (value, self.tag, '-180 to 180')

class URL(Validator):
    """URL Validator"""
    tag = 'url'
    def _is_valid(self,value):
        return false

def all_config_validators():
    validators = DefaultValidators.copy()
    validators[Email.tag] = Email
    validators[Longitude.tag] = Longitude
    validators[Latitude.tag] = Latitude
    validators[URL.tag] = URL
    return validators

