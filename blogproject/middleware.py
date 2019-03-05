from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
import re

class CheckLoginMiddleware(MiddlewareMixin):

    def process_request(self, request):

        if re.match('/tool/.+',request.path):
            if request.session.has_key('login_status'):
                if request.path in ['/tool/sign/','/tool/login/']:
                    return redirect('/tool/tool/')
                else:
                    return None
            else:
                if not request.path in ['/tool/sign/','/tool/login/']:
                    return redirect('/tool/sign/')
                else:
                    return None
        return None
