from django.contrib.auth.views import LoginView
from django.utils.http import url_has_allowed_host_and_scheme
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm


class CustomLoginView(LoginView):
    template_name = "registration/login.html"

    def get_redirect_url(self):
        """Return the user-originating redirect URL if it's safe."""
        redirect_to = "home"
        user = self.request.user
        if self.request.POST:
            if user.business_id and user.is_active:
                redirect_to = "/business/dashboard/"
            elif user.creator_id and user.is_active:
                redirect_to = "/creator/"
        url_is_safe = url_has_allowed_host_and_scheme(
            url=redirect_to,
            allowed_hosts=self.get_success_url_allowed_hosts(),
            require_https=self.request.is_secure(),
        )
        return redirect_to if url_is_safe else ""

      
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("user:login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
            for field in form.visible_fields():
                if field.errors:
                    field.errors.clear()
            return self.render_to_response(self.get_context_data(form=form))
