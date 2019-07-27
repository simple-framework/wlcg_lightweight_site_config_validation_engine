from yamale.validators.constraints import Constraint
from email.utils import parseaddr
import string 
import re

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

class CharContains(Constraint):
	keywords = {'contains': list}
	fail = "{} contains invalid chartacters. String should contain characters from group(s) {}"

	def _is_valid(self, value):
		allowed = self.allowed_chars(self.contains)

		if len(set(value) - allowed):
			return False

		else:
			return True

	def _fail(self, value):
		return self.fail.format(value, self.contains)

	def allowed_chars(self, groups):
		allowed = []

		for group in groups:
			if group == "a-z":
				allowed.extend(list(string.ascii_lowercase))

			elif group == "A-Z":
				allowed.extend(list(string.ascii_uppercase))

			elif group == "0-9":
				allowed.extend(list(string.digits))

			else:
				allowed.append(group)

		return set(allowed)

class RegexMatch(Constraint):
	keywords = {'regex': str}
	fail = "{} doesn't match the regex {}"

	def _is_valid(self, value):
		pattern = re.compile("(?:" + self.regex + r")\Z")

		return pattern.match(str(value))

	def _fail(self, value):
		return self.fail.format(value, self.regex)
