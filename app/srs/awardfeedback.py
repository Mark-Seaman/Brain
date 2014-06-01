# srs/awardfeedback.py
# Model for AwardFeedback records

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

    
# Define a contact data type
class AwardFeedback(models.Model):
    name    = models.CharField (max_length=40)
    user    = models.ForeignKey(User)


    # Format a record as a string
    def __unicode__(self):
        return self.name

    # Back trace a url to a view
    def get_absolute_url(self):
        return reverse('awardfeedback-detail', kwargs={'pk': self.pk})

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
def query_awardfeedback(user=None):
    if user:
        objects = AwardFeedback.objects.filter(user=user)
    else:
        objects = AwardFeedback.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_awardfeedback(user,id):
    a =  AwardFeedback.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Print a awardfeedback as a table of fields
def print_awardfeedback(awardfeedback):
    for x in awardfeedback.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Show the object in several different forms
def show_awardfeedback(awardfeedback):
    print 'AwardFeedback:', awardfeedback.name
    print 'Fields:', awardfeedback.fields()
    print 'Values:', awardfeedback.values()
    print 'Table:', awardfeedback.table()
    print_awardfeedback(awardfeedback)


# Generate a new record if needed
def add_fake_awardfeedback(name):
    print 'Make awardfeedback: ', name
    c = AwardFeedback()
    #c.name = name
    #c.address = 'Here'
    #c.phone = '900-555-1212'
    c.save()
    return c


# Perform a test on this object type
def test_code():

    # Count current records
    num_awardfeedbacks = len(query_awardfeedback())
    print '%d AwardFeedbacks' % num_awardfeedbacks

    # Delete all records
    #AwardFeedback.objects.all().delete()

    # If there are no awardfeedbacks then make some
    if num_awardfeedbacks<1:
        fake_names = [ 'Tom', 'Jerry', 'Billy', 'Bob' ]
        for c in fake_names:
            add_fake_awardfeedback(c)

    # Print a list of all names
    all = AwardFeedback.objects.all()
    print 'AwardFeedback list:  %d records' % len(all)
    for c in all:
        print_awardfeedback(c)

