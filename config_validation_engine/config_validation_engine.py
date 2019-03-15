from validators.validators import all_config_validators
import yamale
import argparse
from email.utils import parseaddr


def validate(schema, data):
    _validators = all_config_validators()
    _schema = yamale.make_schema(schema, validators=_validators)
    _data = yamale.make_data(data)
    results = yamale.validate(_schema, _data)
    print(results)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data')
    parser.add_argument('-s', '--schema')
    args = parser.parse_args()
    return {
        'data': args.data,
        'schema': args.schema
    }


def email_domain_validator(domain, addresses):
    for address in addresses:
        name, email_addr = parseaddr(address)
        email_parts = email_addr.split(u'@')
        if (domain == email_parts[1]):
            print("Valid email address: ",email_addr)
        else:
            print("Invalid email address: ",email_addr)


if __name__ == "__main__":
    args = parse_args()
    data = args['data']
    schema = args['schema']
    # email_domain_validator('cern.ch',['example.example@cern.ch','example@gmail.com'])
    validate(schema, data)
    pass