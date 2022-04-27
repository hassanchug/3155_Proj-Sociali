import os

from dotenv import load_dotenv
from flask import Flask, abort, redirect, render_template, request

from src.models import db

load_dotenv()

app = Flask(__name__)
