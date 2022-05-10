from src.models import User
from flask import pyetest
from src.repositories.post_repository import post_repository_singleton


def test_user_model():
    U1 = User('Flameboy', 'Tony', 'Le', 'GetBuckets919')
    assert U1.username == 'Flameboy'
    assert U1.firstname == 'Tony'
    assert U1.lastname == 'Le'
    assert U1.password == "GetBuckets919"

    assert U1 in post_repository_singleton.create_user('Flameboy','Tony','Le','GetBuckets919')

    U1 = User('Chaosblaze', 'Shekar', 'Bala', 'ClashOfClans')
    assert U1.username == 'Chaosblaze'
    assert U1.firstname == 'Shekar'
    assert U1.lastname == 'Bala'
    assert U1.password == "ClashOfClans"

    assert U1 in post_repository_singleton.create_user('Chaosblaze','Shekar','Bala','ClashOfClans')