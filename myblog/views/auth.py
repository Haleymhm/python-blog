import functools
from os import error
from flask import(
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from myblog.models.user import User

from myblog import db

auth = Blueprint('auth', __name__, url_prefix='/auth')

#Registrar un usuario 
@auth.route('/register', methods=('GET','POST'))
def register():
    return render_template('auth/register.html')