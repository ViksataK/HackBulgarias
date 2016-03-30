from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def login_required(redirect_url):
    def accepter(func):
        def decorated(*args):
            session_username = args[0].session.get('username', False)
            if session_username:
                return func(*args)
            return redirect(reverse(redirect_url))
        return decorated
    return accepter
