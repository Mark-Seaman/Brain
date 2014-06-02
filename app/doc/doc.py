# srs/doc.py
# Model for Doc records

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

    
# Define a contact data type
class Doc(models.Model):
    user    = models.ForeignKey(User)
    path    = models.CharField (max_length=200)
    title   = models.CharField (max_length=200)
    text    = models.TextField ()

    # Format a record as a string
    def __unicode__(self):
        return self.name

    # Back trace a url to a view
    def get_absolute_url(self):
        return reverse('doc-detail', kwargs={'pk': self.pk})

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
def query_doc(user=None):
    if user:
        objects = Doc.objects.filter(user=user)
    else:
        objects = Doc.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_doc(user,id):
    a =  Doc.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Print a doc as a table of fields
def print_doc(doc):
    for x in doc.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Show the object in several different forms
def show_doc(doc):
    print 'Doc:', doc.name
    print 'Fields:', doc.fields()
    print 'Values:', doc.values()
    print 'Table:', doc.table()
    print_doc(doc)


# Generate a new record if needed
def add_fake_doc(name):
    print 'Make doc: ', name
    c = Doc()
    c.user = User.objects.get(username='TestRobot')
    c.path = 'My Path'
    c.title = 'My Title'
    c.text = 'None'
    c.save()
    return c


# Perform a test on this object type
def test_code():

    # Count current records
    num_docs = len(query_doc())
    print '%d Docs' % num_docs

    # Delete all records
    #Doc.objects.all().delete()

    # If there are no docs then make some
    if num_docs<1:
        fake_names = [ 'Tom', 'Jerry', 'Billy', 'Bob' ]
        for c in fake_names:
            add_fake_doc(c)

    # Print a list of all names
    all = Doc.objects.all()
    print 'Doc list:  %d records' % len(all)
    for c in all:
        print_doc(c)

