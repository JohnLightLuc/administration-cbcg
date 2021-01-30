from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


class SessionExpiredMiddleware:
    def process_request(request):
        last_activity = request.session['last_activity']
        now = datetime.now()
        print("last_activity")
        print(last_activity)
        """
        if (now - last_activity).minutes > 5:
            logout(request)
            return redirect('myadmin:connexion')

        if not request.is_ajax():
            # don't set this for ajax requests or else your
            # expired session checks will keep the session from
            # expiring :)
            request.session['last_activity'] = now
        """