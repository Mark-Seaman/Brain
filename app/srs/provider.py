# srs/provider.py
# Model for Provider records

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

    
# Define a contact data type
class Provider(models.Model):
    name    = models.CharField (max_length=40)
    user    = models.ForeignKey(User)


    # Format a record as a string
    def __unicode__(self):
        return self.name

    # Back trace a url to a view
    def get_absolute_url(self):
        return reverse('provider-detail', kwargs={'pk': self.pk})

    # Object field handling
    def __iter__(self):
        for i in self.fields():
            yield (i, getattr(self, i))

    # Enumerate the fields
    def fields(self):
        return [ f.name for f in self._meta.fields ]

    # List of values
    def values(self):
        return [ v for f,v in self ]

    # Table of field labels and values
    def table(self):
        return zip(self.fields(),self.values())

#---------------------------------------------------------

# Get a table listing from the database
def query_provider(user=None):
    if user:
        objects = Provider.objects.filter(user=user)
    else:
        objects = Provider.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_provider(user,id):
    a =  Provider.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Print a provider as a table of fields
def print_provider(provider):
    for x in provider.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Show the object in several different forms
def show_provider(provider):
    print 'Provider:', provider.name
    print 'Fields:', provider.fields()
    print 'Values:', provider.values()
    print 'Table:', provider.table()
    print_provider(provider)


# Generate a new record if needed
def add_fake_provider(name):
    print 'Make provider: ', name
    c = Provider()
    #c.name = name
    #c.address = 'Here'
    #c.phone = '900-555-1212'
    c.save()
    return c


# Perform a test on this object type
def test_code():

    # Count current records
    num_providers = len(query_provider())
    print '%d Providers' % num_providers

    # Delete all records
    #Provider.objects.all().delete()

    # If there are no providers then make some
    if num_providers<1:
        fake_names = [ 'Tom', 'Jerry', 'Billy', 'Bob' ]
        for c in fake_names:
            add_fake_provider(c)

    # Print a list of all names
    all = Provider.objects.all()
    print 'Provider list:  %d records' % len(all)
    for c in all:
        print_provider(c)

