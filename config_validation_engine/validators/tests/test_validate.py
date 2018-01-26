from config_validation_engine.validators import validators as val

def test_email():
    v = val.Email()
    assert not v.is_valid('random@')

def test_latitude():
    v = val.Latitude()
    assert v.is_valid(23)
    assert not v.is_valid(23.1)
    