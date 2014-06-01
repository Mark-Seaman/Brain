# srs/group.py
# Model for Group records

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

    
# Define a contact data type
class Group(models.Model):
    name    = models.CharField (max_length=40)
    user    = models.ForeignKey(User)


    # Format a record as a string
    def __unicode__(self):
        return self.name

    # Back trace a url to a view
    def get_absolute_url(self):
        return reverse('group-detail', kwargs={'pk': self.pk})

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
def query_group(user=None):
    if user:
        objects = Group.objects.filter(user=user)
    else:
        objects = Group.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_group(user,id):
    a =  Group.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Print a group as a table of fields
def print_group(group):
    for x in group.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Show the object in several different forms
def show_group(group):
    print 'Group:', group.name
    print 'Fields:', group.fields()
    print 'Values:', group.values()
    print 'Table:', group.table()
    print_group(group)


# Generate a new record if needed
def add_fake_group(name):
    print 'Make group: ', name
    c = Group()
    #c.name = name
    #c.address = 'Here'
    #c.phone = '900-555-1212'
    c.save()
    return c


# Perform a test on this object type
def test_code():

    # Count current records
    num_groups = len(query_group())
    print '%d Groups' % num_groups

    # Delete all records
    #Group.objects.all().delete()

    # If there are no groups then make some
    if num_groups<1:
        fake_names = [ 'Tom', 'Jerry', 'Billy', 'Bob' ]
        for c in fake_names:
            add_fake_group(c)

    # Print a list of all names
    all = Group.objects.all()
    print 'Group list:  %d records' % len(all)
    for c in all:
        print_group(c)

