from yamale.validators.constraints import Constraint
from email.utils import parseaddr

class EmailDomain(Constraint):
	keywords = {'domain': str}
	fail = '%s does not contain a valid domain. The acceptable domain value is %s'

	def _is_valid(self,value):
		name, email_addr = parseaddr(value)
		email_parts = email_addr.split(u'@')
		if (self.domain == email_parts[1]):
			return True
		else:
			return False

	def _fail(self,value):
		return self.fail % (value,self.domain)

class Ipv4Constraint(Constraint):

    def _is_valid(self, value):
        
        digits = map(int, value.split("."))
        if all(filter(lambda x: 0 <= x < 256, digits)):
            return True
        else:
            return False
