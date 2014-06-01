# srs/ideafeedback.py
# Model for IdeaFeedback records

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

    
# Define a contact data type
class IdeaFeedback(models.Model):
    name    = models.CharField (max_length=40)
    user    = models.ForeignKey(User)


    # Format a record as a string
    def __unicode__(self):
        return self.name

    # Back trace a url to a view
    def get_absolute_url(self):
        return reverse('ideafeedback-detail', kwargs={'pk': self.pk})

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
def query_ideafeedback(user=None):
    if user:
        objects = IdeaFeedback.objects.filter(user=user)
    else:
        objects = IdeaFeedback.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_ideafeedback(user,id):
    a =  IdeaFeedback.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Print a ideafeedback as a table of fields
def print_ideafeedback(ideafeedback):
    for x in ideafeedback.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Show the object in several different forms
def show_ideafeedback(ideafeedback):
    print 'IdeaFeedback:', ideafeedback.name
    print 'Fields:', ideafeedback.fields()
    print 'Values:', ideafeedback.values()
    print 'Table:', ideafeedback.table()
    print_ideafeedback(ideafeedback)


# Generate a new record if needed
def add_fake_ideafeedback(name):
    print 'Make ideafeedback: ', name
    c = IdeaFeedback()
    #c.name = name
    #c.address = 'Here'
    #c.phone = '900-555-1212'
    c.save()
    return c


# Perform a test on this object type
def test_code():

    # Count current records
    num_ideafeedbacks = len(query_ideafeedback())
    print '%d IdeaFeedbacks' % num_ideafeedbacks

    # Delete all records
    #IdeaFeedback.objects.all().delete()

    # If there are no ideafeedbacks then make some
    if num_ideafeedbacks<1:
        fake_names = [ 'Tom', 'Jerry', 'Billy', 'Bob' ]
        for c in fake_names:
            add_fake_ideafeedback(c)

    # Print a list of all names
    all = IdeaFeedback.objects.all()
    print 'IdeaFeedback list:  %d records' % len(all)
    for c in all:
        print_ideafeedback(c)

