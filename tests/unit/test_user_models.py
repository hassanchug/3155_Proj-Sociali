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

    U2 = User('Chaosblaze', 'Shekar', 'Bala', 'ClashOfClans')
    assert U2.username == 'Chaosblaze'
    assert U2.firstname == 'Shekar'
    assert U2.lastname == 'Bala'
    assert U2.password == "ClashOfClans"

    assert U2 in post_repository_singleton.create_user('Chaosblaze','Shekar','Bala','ClashOfClans')