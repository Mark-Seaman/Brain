# srs/kudofeedback.py
# Model for KudoFeedback records

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

    
# Define a contact data type
class KudoFeedback(models.Model):
    name    = models.CharField (max_length=40)
    user    = models.ForeignKey(User)


    # Format a record as a string
    def __unicode__(self):
        return self.name

    # Back trace a url to a view
    def get_absolute_url(self):
        return reverse('kudofeedback-detail', kwargs={'pk': self.pk})

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
def query_kudofeedback(user=None):
    if user:
        objects = KudoFeedback.objects.filter(user=user)
    else:
        objects = KudoFeedback.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_kudofeedback(user,id):
    a =  KudoFeedback.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Print a kudofeedback as a table of fields
def print_kudofeedback(kudofeedback):
    for x in kudofeedback.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Show the object in several different forms
def show_kudofeedback(kudofeedback):
    print 'KudoFeedback:', kudofeedback.name
    print 'Fields:', kudofeedback.fields()
    print 'Values:', kudofeedback.values()
    print 'Table:', kudofeedback.table()
    print_kudofeedback(kudofeedback)


# Generate a new record if needed
def add_fake_kudofeedback(name):
    print 'Make kudofeedback: ', name
    c = KudoFeedback()
    #c.name = name
    #c.address = 'Here'
    #c.phone = '900-555-1212'
    c.save()
    return c


# Perform a test on this object type
def test_code():

    # Count current records
    num_kudofeedbacks = len(query_kudofeedback())
    print '%d KudoFeedbacks' % num_kudofeedbacks

    # Delete all records
    #KudoFeedback.objects.all().delete()

    # If there are no kudofeedbacks then make some
    if num_kudofeedbacks<1:
        fake_names = [ 'Tom', 'Jerry', 'Billy', 'Bob' ]
        for c in fake_names:
            add_fake_kudofeedback(c)

    # Print a list of all names
    all = KudoFeedback.objects.all()
    print 'KudoFeedback list:  %d records' % len(all)
    for c in all:
        print_kudofeedback(c)

