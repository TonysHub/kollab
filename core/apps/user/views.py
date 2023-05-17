from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login, REDIRECT_FIELD_NAME
from django.utils.http import url_has_allowed_host_and_scheme

class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    
    def get_redirect_url(self):
        """Return the user-originating redirect URL if it's safe."""
        redirect_to = 'home'
        user = self.request.user
        if self.request.POST:
            if user.business_id and user.is_active:
                redirect_to = '/business/dashboard/'
            elif user.creator_id and user.is_active:
                redirect_to = '/creator/'
        url_is_safe = url_has_allowed_host_and_scheme(
            url=redirect_to,
            allowed_hosts=self.get_success_url_allowed_hosts(),
            require_https=self.request.is_secure(),
        )
        return redirect_to if url_is_safe else ""
    
