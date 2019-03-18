from validators.validators import all_config_validators
import yamale
import argparse


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


if __name__ == "__main__":
    args = parse_args()
    data = args['data']
    schema = args['schema']
    validate(schema, data)
    pass