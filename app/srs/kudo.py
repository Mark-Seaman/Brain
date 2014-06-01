# srs/kudo.py
# Model for Kudo records

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

    
# Define a contact data type
class Kudo(models.Model):
    name    = models.CharField (max_length=40)
    user    = models.ForeignKey(User)


    # Format a record as a string
    def __unicode__(self):
        return self.name

    # Back trace a url to a view
    def get_absolute_url(self):
        return reverse('kudo-detail', kwargs={'pk': self.pk})

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
def query_kudo(user=None):
    if user:
        objects = Kudo.objects.filter(user=user)
    else:
        objects = Kudo.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_kudo(user,id):
    a =  Kudo.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Print a kudo as a table of fields
def print_kudo(kudo):
    for x in kudo.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Show the object in several different forms
def show_kudo(kudo):
    print 'Kudo:', kudo.name
    print 'Fields:', kudo.fields()
    print 'Values:', kudo.values()
    print 'Table:', kudo.table()
    print_kudo(kudo)


# Generate a new record if needed
def add_fake_kudo(name):
    print 'Make kudo: ', name
    c = Kudo()
    #c.name = name
    #c.address = 'Here'
    #c.phone = '900-555-1212'
    c.save()
    return c


# Perform a test on this object type
def test_code():

    # Count current records
    num_kudos = len(query_kudo())
    print '%d Kudos' % num_kudos

    # Delete all records
    #Kudo.objects.all().delete()

    # If there are no kudos then make some
    if num_kudos<1:
        fake_names = [ 'Tom', 'Jerry', 'Billy', 'Bob' ]
        for c in fake_names:
            add_fake_kudo(c)

    # Print a list of all names
    all = Kudo.objects.all()
    print 'Kudo list:  %d records' % len(all)
    for c in all:
        print_kudo(c)

