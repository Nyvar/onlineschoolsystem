from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def role_required(*roles):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('/')
            # Flatten if passed as a single list or tuple
            if len(roles) == 1 and isinstance(roles[0], (list, tuple)):
                allowed_roles = roles[0]
            else:
                allowed_roles = roles
            if request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You do not have permission.")
        return _wrapped_view
    return decorator

