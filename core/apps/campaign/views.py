from core.apps.user.models import KollabUser
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CampaignCreateForm
from django.contrib import auth
from django.shortcuts import redirect
from django.urls import reverse_lazy


class CampaignHome(TemplateView):
    template_name = "campaign/campaign_home.html"


# V2
# @login_required
# def campaign_create(request):
#     if not auth.get_user(request).is_authenticated:
#         return redirect('login')
#     if request.method == 'POST':
#         form = CampaignCreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             # must be a cleaner way of getting the business_id...
#             business_id = KollabUser.objects.filter(id=auth.get_user(request).id).values()[0]["business_id"]
#             form.instance.business_id = business_id
#             form.save()
#             return HttpResponseRedirect('/campaign/')
#     else:
#         form = CampaignCreateForm()
#     return render(request, 'campaign/campaign_create.html', {'form': form})


# V1
class CampaignCreate(LoginRequiredMixin, CreateView):
    form_class = CampaignCreateForm
    template_name = "campaign/campaign_create.html"
    success_url = reverse_lazy("campaign-home")

    def form_valid(self, form):
        if not auth.get_user(self.request).is_authenticated:
            return redirect("login")
        # must be a cleaner way of getting the business_id...
        business_id = KollabUser.objects.filter(
            id=auth.get_user(self.request).id
        ).values()[0]["business_id"]
        form.instance.business_id = business_id
        return super().form_valid(form)
