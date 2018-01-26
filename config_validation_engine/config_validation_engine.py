from .validators import validators
import yamale

def validate(schema, data):
    _validators = validators.all_config_validators()
    _schema = yamale.make_schema(schema, validators=_validators)
    _data = yamale.make_data(data)
    results = yamale.validate(_schema, _data)
    print(results)


        
