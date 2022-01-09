from django.http.response import HttpResponseRedirect
from django.urls import reverse


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("dataentry",))
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func