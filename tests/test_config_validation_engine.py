from . import get_fixture

# import modules from the project for testing
from config_validation_engine.config_validation_engine import *

custom = {
    'schema': 'schema.yml',
    'bad': 'data_bad.yml',
    'good': 'data_good.yml'
}

def test_validate():
    print('Data')
    print(custom['schema'])
    # validate(custom['schema'], custom['good'])
    validate(get_fixture('schema.yml'),get_fixture('data_bad.yml'))

