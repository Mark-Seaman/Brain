# srs/idea.py
# Model for Idea records

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

    
# Define a contact data type
class Idea(models.Model):
    name    = models.CharField (max_length=40)
    user    = models.ForeignKey(User)


    # Format a record as a string
    def __unicode__(self):
        return self.name

    # Back trace a url to a view
    def get_absolute_url(self):
        return reverse('idea-detail', kwargs={'pk': self.pk})

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
def query_idea(user=None):
    if user:
        objects = Idea.objects.filter(user=user)
    else:
        objects = Idea.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_idea(user,id):
    a =  Idea.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Print a idea as a table of fields
def print_idea(idea):
    for x in idea.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Show the object in several different forms
def show_idea(idea):
    print 'Idea:', idea.name
    print 'Fields:', idea.fields()
    print 'Values:', idea.values()
    print 'Table:', idea.table()
    print_idea(idea)


# Generate a new record if needed
def add_fake_idea(name):
    print 'Make idea: ', name
    c = Idea()
    #c.name = name
    #c.address = 'Here'
    #c.phone = '900-555-1212'
    c.save()
    return c


# Perform a test on this object type
def test_code():

    # Count current records
    num_ideas = len(query_idea())
    print '%d Ideas' % num_ideas

    # Delete all records
    #Idea.objects.all().delete()

    # If there are no ideas then make some
    if num_ideas<1:
        fake_names = [ 'Tom', 'Jerry', 'Billy', 'Bob' ]
        for c in fake_names:
            add_fake_idea(c)

    # Print a list of all names
    all = Idea.objects.all()
    print 'Idea list:  %d records' % len(all)
    for c in all:
        print_idea(c)

