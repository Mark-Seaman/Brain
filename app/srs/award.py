# srs/award.py
# Model for Award records

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

    
# Define a contact data type
class Award(models.Model):
    name    = models.CharField (max_length=40)
    user    = models.ForeignKey(User)


    # Format a record as a string
    def __unicode__(self):
        return self.name

    # Back trace a url to a view
    def get_absolute_url(self):
        return reverse('award-detail', kwargs={'pk': self.pk})

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
def query_award(user=None):
    if user:
        objects = Award.objects.filter(user=user)
    else:
        objects = Award.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_award(user,id):
    a =  Award.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Print a award as a table of fields
def print_award(award):
    for x in award.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Show the object in several different forms
def show_award(award):
    print 'Award:', award.name
    print 'Fields:', award.fields()
    print 'Values:', award.values()
    print 'Table:', award.table()
    print_award(award)


# Generate a new record if needed
def add_fake_award(name):
    print 'Make award: ', name
    c = Award()
    #c.name = name
    #c.address = 'Here'
    #c.phone = '900-555-1212'
    c.save()
    return c


# Perform a test on this object type
def test_code():

    # Count current records
    num_awards = len(query_award())
    print '%d Awards' % num_awards

    # Delete all records
    #Award.objects.all().delete()

    # If there are no awards then make some
    if num_awards<1:
        fake_names = [ 'Tom', 'Jerry', 'Billy', 'Bob' ]
        for c in fake_names:
            add_fake_award(c)

    # Print a list of all names
    all = Award.objects.all()
    print 'Award list:  %d records' % len(all)
    for c in all:
        print_award(c)

