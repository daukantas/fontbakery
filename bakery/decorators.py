# coding: utf-8
# Copyright 2013 The Font Bakery Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# See AUTHORS.txt for the list of Authors and LICENSE.txt for the License.

from functools import wraps
from flask import g, request, redirect, url_for, flash
from flask.ext.babel import gettext as _


def login_required(func):
    """ Decorator allow to access route only logged in user. Usage:

        @project.route('/test', methods=['GET'])
        @login_required
        def test():
            return "You are logged in"

    """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            flash(_('Login required'))
            return redirect(url_for('gitauth.login', next=request.url))
        return func(*args, **kwargs)
    return decorated_function


def cached(obj):
    cache = obj.cache = {}

    @wraps(obj)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]
    return memoizer
