# srs/ideagroup.py
# Model for IdeaGroup records

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

    
# Define a contact data type
class IdeaGroup(models.Model):
    name    = models.CharField (max_length=40)
    user    = models.ForeignKey(User)


    # Format a record as a string
    def __unicode__(self):
        return self.name

    # Back trace a url to a view
    def get_absolute_url(self):
        return reverse('ideagroup-detail', kwargs={'pk': self.pk})

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
def query_ideagroup(user=None):
    if user:
        objects = IdeaGroup.objects.filter(user=user)
    else:
        objects = IdeaGroup.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_ideagroup(user,id):
    a =  IdeaGroup.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Print a ideagroup as a table of fields
def print_ideagroup(ideagroup):
    for x in ideagroup.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Show the object in several different forms
def show_ideagroup(ideagroup):
    print 'IdeaGroup:', ideagroup.name
    print 'Fields:', ideagroup.fields()
    print 'Values:', ideagroup.values()
    print 'Table:', ideagroup.table()
    print_ideagroup(ideagroup)


# Generate a new record if needed
def add_fake_ideagroup(name):
    print 'Make ideagroup: ', name
    c = IdeaGroup()
    #c.name = name
    #c.address = 'Here'
    #c.phone = '900-555-1212'
    c.save()
    return c


# Perform a test on this object type
def test_code():

    # Count current records
    num_ideagroups = len(query_ideagroup())
    print '%d IdeaGroups' % num_ideagroups

    # Delete all records
    #IdeaGroup.objects.all().delete()

    # If there are no ideagroups then make some
    if num_ideagroups<1:
        fake_names = [ 'Tom', 'Jerry', 'Billy', 'Bob' ]
        for c in fake_names:
            add_fake_ideagroup(c)

    # Print a list of all names
    all = IdeaGroup.objects.all()
    print 'IdeaGroup list:  %d records' % len(all)
    for c in all:
        print_ideagroup(c)

