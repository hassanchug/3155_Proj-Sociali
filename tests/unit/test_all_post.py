from src.models import User
from flask import pyetest
from src.repositories.post_repository import post_repository_singleton


def test_get_all_post():
    temp1 = post_repository_singleton.create_post('1', 'Cancun Trip!', 'Glad you had fun', '50 likes')

    assert temp1.post_id == 1
    assert temp1.title == 'Cancun Trip!'
    assert temp1.replies == 'Glad you had fun'
    assert temp1.likes == '50 likes'

    temp2 = post_repository_singleton.create_post('2', 'Budapest', 'I wish I was there', '47 likes')

    assert temp2.post_id == 2
    assert temp2.title == 'Budapest'
    assert temp2.replies == 'I wish I was there'
    assert temp2.likes == '47 likes'