from flask import Flask
import pytest, unittest
from src.repositories import post_repository
from src.repositories.post_repository import PostRepository

def test_get_all_posts():
    temp = PostRepository()
    temp_list = PostRepository.get_all_posts(self=temp)
    assert len(temp_list) == 0


