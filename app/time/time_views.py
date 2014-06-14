# time/views_dt.py
# Time views for basic operations


#############################################################################
# DO NOT EDIT THIS FILE
# This Code will be replaced by the code generator
#############################################################################

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

from time_model import Time
from time_query import query_time, get_time


# Basic list view with using a template
class TimeList(ListView):
    model = Time
    template_name = 'time_list.html'

    # Filter the list of choices
    queryset = query_time()

    # Use the request user to match the items
    #def get_queryset(self):
    #    return Time.objects.filter(name=self.request.user.username)


# Basic detail view
class TimeDetail(DetailView):
    model = Time
    template_name = 'time_detail.html'

    # Call the base implementation first to get a context
    def get_context_data(self, **kwargs):
        context = super(TimeDetail, self).get_context_data(**kwargs)
        id = context['object'].pk
        context['value_list'] = get_time(self.request.user,id)
        return context


# Create view
class TimeAdd(CreateView):
    model = Time
    template_name = 'time_edit.html'


# Update view
#@login_required(login_url='/login')
class TimeEdit(UpdateView):
    model = Time
    template_name = 'time_edit.html'


# Delete view
class TimeDelete(DeleteView):
    model = Time
    success_url = reverse_lazy('time_list')
    template_name = 'time_delete.html'
