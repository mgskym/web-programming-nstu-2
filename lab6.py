from flask import Blueprint, render_template, request, make_response
import psycopg2

lab6 = Blueprint('lab6', __name__)

