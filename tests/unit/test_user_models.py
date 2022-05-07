from src.models import User
from flask import pyetest

def test_user_model():
    u = User('Flameboy', 'Tony', 'Le', 'GetBuckets919')
    assert u.username == 'Flameboy'
    assert u.firstname == 'Tony'
    assert u.lastname == 'Le'
    assert u.password == "GetBuckets919"

