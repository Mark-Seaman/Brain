# srs/company.py
# Model for Company records

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

    
# Define a contact data type
class Company(models.Model):
    name    = models.CharField (max_length=40)
    user    = models.ForeignKey(User)


    # Format a record as a string
    def __unicode__(self):
        return self.name

    # Back trace a url to a view
    def get_absolute_url(self):
        return reverse('company-detail', kwargs={'pk': self.pk})

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
def query_company(user=None):
    if user:
        objects = Company.objects.filter(user=user)
    else:
        objects = Company.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_company(user,id):
    a =  Company.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Print a company as a table of fields
def print_company(company):
    for x in company.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Show the object in several different forms
def show_company(company):
    print 'Company:', company.name
    print 'Fields:', company.fields()
    print 'Values:', company.values()
    print 'Table:', company.table()
    print_company(company)


# Generate a new record if needed
def add_fake_company(name):
    print 'Make company: ', name
    c = Company()
    #c.name = name
    #c.address = 'Here'
    #c.phone = '900-555-1212'
    c.save()
    return c


# Perform a test on this object type
def test_code():

    # Count current records
    num_companys = len(query_company())
    print '%d Companys' % num_companys

    # Delete all records
    #Company.objects.all().delete()

    # If there are no companys then make some
    if num_companys<1:
        fake_names = [ 'Tom', 'Jerry', 'Billy', 'Bob' ]
        for c in fake_names:
            add_fake_company(c)

    # Print a list of all names
    all = Company.objects.all()
    print 'Company list:  %d records' % len(all)
    for c in all:
        print_company(c)

