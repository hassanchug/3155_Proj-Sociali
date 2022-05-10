from flask import Flask
import pytest, unittest
from src.repositories import post_repository
from src.repositories.post_repository import PostRepository

def test_get_all_posts():
    temp = PostRepository()
    temp_list = PostRepository.get_all_posts(self=temp)
    assert len(temp_list) == 0

    temp.create_post('1', 'Cancun Trip!', 'Glad you had fun', '50 likes')
    temp_list = PostRepository.get_all_posts(self=temp)

    assert len(temp_list) == 1
    temp.create_post('2', 'Going to Cali', 'Nice pic', '38 likes')
    temp.create_post('3', 'Budapest', 'I wish I was there', '47 likes')
    temp_list = PostRepository.get_all_posts(self=temp)

    assert len(temp_list) == 3




