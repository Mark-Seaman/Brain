# srs/views_dt.py
# Behavior views for basic operations


#############################################################################
# DO NOT EDIT THIS FILE
# This Code will be replaced by the code generator
#############################################################################

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

from models import Behavior
from behavior import query_behavior, get_behavior


# Basic list view with using a template
class BehaviorList(ListView):
    model = Behavior
    template_name = 'behavior_list.html'

    # Filter the list of choices
    queryset = query_behavior()

    # Use the request user to match the items
    #def get_queryset(self):
    #    return Behavior.objects.filter(name=self.request.user.username)


# Basic detail view
class BehaviorDetail(DetailView):
    model = Behavior
    template_name = 'behavior_detail.html'

    # Call the base implementation first to get a context
    def get_context_data(self, **kwargs):
        context = super(BehaviorDetail, self).get_context_data(**kwargs)
        id = context['object'].pk
        context['value_list'] = get_behavior(self.request.user,id)
        return context


# Create view
class BehaviorAdd(CreateView):
    model = Behavior
    template_name = 'behavior_edit.html'


# Update view
#@login_required(login_url='/login')
class BehaviorEdit(UpdateView):
    model = Behavior
    template_name = 'behavior_edit.html'


# Delete view
class BehaviorDelete(DeleteView):
    model = Behavior
    success_url = reverse_lazy('behavior_list')
    template_name = 'behavior_delete.html'

