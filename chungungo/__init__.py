from flask import Flask

app = Flask(__name__)

# python -c "import os; print(repr(os.urandom(32)));"
app.config['SECRET_KEY'] = b'\x84\x06\xbfd\x03\x16\x80\xdbxU\xd0\xe5\xa0\xd26#\x12\x85\x06\xbbw\x16\xaeW\x85\xa7#6W\x86$\xf5'

from chungungo import views