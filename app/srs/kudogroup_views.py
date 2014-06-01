# views_dt.py
# KudoGroup views

#############################################################################
# DO NOT EDIT THIS FILE
# This Code will be replaced by the code generator
#############################################################################

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

from models import KudoGroup
from kudogroup import query_kudogroup, get_kudogroup


# Basic list view with using a template
@login_required(login_url='/login')
class KudoGroupList(ListView):
    model = KudoGroup
    template_name = 'kudogroup_list.html'

    # Filter the list of choices
    queryset = query_kudogroup()

    # Use the request user to match the items
    #def get_queryset(self):
    #    return KudoGroup.objects.filter(name=self.request.user.username)


# Basic detail view
@login_required(login_url='/login')
class KudoGroupDetail(DetailView):
    model = KudoGroup
    template_name = 'kudogroup_detail.html'

    # Call the base implementation first to get a context
    def get_context_data(self, **kwargs):
        context = super(KudoGroupDetail, self).get_context_data(**kwargs)
        id = context['object'].pk
        context['value_list'] = get_kudogroup(self.request.user,id)
        return context


# Create view
@login_required(login_url='/login')
class KudoGroupAdd(CreateView):
    model = KudoGroup
    template_name = 'kudogroup_edit.html'


# Update view
@login_required(login_url='/login')
class KudoGroupEdit(UpdateView):
    model = KudoGroup
    template_name = 'kudogroup_edit.html'


# Delete view
@login_required(login_url='/login')
class KudoGroupDelete(DeleteView):
    model = KudoGroup
    success_url = reverse_lazy('kudogroup_list')
    template_name = 'kudogroup_delete.html'

