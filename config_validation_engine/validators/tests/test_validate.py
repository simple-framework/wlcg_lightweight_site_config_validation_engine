from config_validation_engine.validators import validators as val
import unittest
import yamale


class ValidatorTests(unittest.TestCase):

    def test_email(self):
        v = val.Email(self)
        assert not v.is_valid('random@')

    def test_latitude(self):
        v = val.Latitude()
        assert v.is_valid(23)
        assert v.is_valid(23.1)

    def test_URL(self):
        v = val.URL()
        assert not v._is_valid('test.com')
        assert v._is_valid('http://test.com')

    def test_site_object(self):
        schema = yamale.make_schema('./config_validation_engine/validators/schema/site_object_schema.yaml', validators=val.all_config_validators())
        data = yamale.make_data('./config_validation_engine/validators/tests/site_object_data.yaml')
        assert yamale.validate(schema, data)


if __name__ == '__main__':
    unittest.main()
