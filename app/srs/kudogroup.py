# srs/kudogroup.py
# Model for KudoGroup records

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

    
# Define a contact data type
class KudoGroup(models.Model):
    name    = models.CharField (max_length=40)
    user    = models.ForeignKey(User)


    # Format a record as a string
    def __unicode__(self):
        return self.name

    # Back trace a url to a view
    def get_absolute_url(self):
        return reverse('kudogroup-detail', kwargs={'pk': self.pk})

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
def query_kudogroup(user=None):
    if user:
        objects = KudoGroup.objects.filter(user=user)
    else:
        objects = KudoGroup.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_kudogroup(user,id):
    a =  KudoGroup.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Print a kudogroup as a table of fields
def print_kudogroup(kudogroup):
    for x in kudogroup.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Show the object in several different forms
def show_kudogroup(kudogroup):
    print 'KudoGroup:', kudogroup.name
    print 'Fields:', kudogroup.fields()
    print 'Values:', kudogroup.values()
    print 'Table:', kudogroup.table()
    print_kudogroup(kudogroup)


# Generate a new record if needed
def add_fake_kudogroup(name):
    print 'Make kudogroup: ', name
    c = KudoGroup()
    #c.name = name
    #c.address = 'Here'
    #c.phone = '900-555-1212'
    c.save()
    return c


# Perform a test on this object type
def test_code():

    # Count current records
    num_kudogroups = len(query_kudogroup())
    print '%d KudoGroups' % num_kudogroups

    # Delete all records
    #KudoGroup.objects.all().delete()

    # If there are no kudogroups then make some
    if num_kudogroups<1:
        fake_names = [ 'Tom', 'Jerry', 'Billy', 'Bob' ]
        for c in fake_names:
            add_fake_kudogroup(c)

    # Print a list of all names
    all = KudoGroup.objects.all()
    print 'KudoGroup list:  %d records' % len(all)
    for c in all:
        print_kudogroup(c)

