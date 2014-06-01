# srs/behavior.py
# Model for Behavior records

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

    
# Define a contact data type
class Behavior(models.Model):
    name    = models.CharField (max_length=40)
    user    = models.ForeignKey(User)


    # Format a record as a string
    def __unicode__(self):
        return self.name

    # Back trace a url to a view
    def get_absolute_url(self):
        return reverse('behavior-detail', kwargs={'pk': self.pk})

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
def query_behavior(user=None):
    if user:
        objects = Behavior.objects.filter(user=user)
    else:
        objects = Behavior.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_behavior(user,id):
    a =  Behavior.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Print a behavior as a table of fields
def print_behavior(behavior):
    for x in behavior.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Show the object in several different forms
def show_behavior(behavior):
    print 'Behavior:', behavior.name
    print 'Fields:', behavior.fields()
    print 'Values:', behavior.values()
    print 'Table:', behavior.table()
    print_behavior(behavior)


# Generate a new record if needed
def add_fake_behavior(name):
    print 'Make behavior: ', name
    c = Behavior()
    #c.name = name
    #c.address = 'Here'
    #c.phone = '900-555-1212'
    c.save()
    return c


# Perform a test on this object type
def test_code():

    # Count current records
    num_behaviors = len(query_behavior())
    print '%d Behaviors' % num_behaviors

    # Delete all records
    #Behavior.objects.all().delete()

    # If there are no behaviors then make some
    if num_behaviors<1:
        fake_names = [ 'Tom', 'Jerry', 'Billy', 'Bob' ]
        for c in fake_names:
            add_fake_behavior(c)

    # Print a list of all names
    all = Behavior.objects.all()
    print 'Behavior list:  %d records' % len(all)
    for c in all:
        print_behavior(c)

