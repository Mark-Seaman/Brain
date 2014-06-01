# srs/views_dt.py
# Contact views for basic operations


#############################################################################
# DO NOT EDIT THIS FILE
# This Code will be replaced by the code generator
#############################################################################

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

from models import Contact
from contact import query_contact, get_contact


# Basic list view with using a template
class ContactList(ListView):
    model = Contact
    template_name = 'contact_list.html'

    # Filter the list of choices
    queryset = query_contact()

    # Use the request user to match the items
    #def get_queryset(self):
    #    return Contact.objects.filter(name=self.request.user.username)


# Basic detail view
class ContactDetail(DetailView):
    model = Contact
    template_name = 'contact_detail.html'

    # Call the base implementation first to get a context
    def get_context_data(self, **kwargs):
        context = super(ContactDetail, self).get_context_data(**kwargs)
        id = context['object'].pk
        context['value_list'] = get_contact(self.request.user,id)
        return context


# Create view
class ContactAdd(CreateView):
    model = Contact
    template_name = 'contact_edit.html'


# Update view
#@login_required(login_url='/login')
class ContactEdit(UpdateView):
    model = Contact
    template_name = 'contact_edit.html'


# Delete view
class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')
    template_name = 'contact_delete.html'

