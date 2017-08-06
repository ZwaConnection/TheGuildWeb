from django.http import HttpResponseRedirect

def anonymous_required(view, redirect_to= None):
    return AnonymousRequired(view, redirect_to)

class AnonymousRequired(object):
    def __init__(self, view, redirect_to):
        if redirect_to is None:
            from django.conf import settings
            redirect_to = settings.LOGIN_REDIRECT_URL
        self.view = view
        self.redirect_to = redirect_to

    def __call__(self, request, *args, **kwargs):
        if request.user is not None and request.user.is_authenticated:
            return HttpResponseRedirect(self.redirect_to)
        return self.view(request, *args, **kwargs)
