# srs/driver.py
# Model for Driver records

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

    
# Define a contact data type
class Driver(models.Model):
    name    = models.CharField (max_length=40)
    user    = models.ForeignKey(User)


    # Format a record as a string
    def __unicode__(self):
        return self.name

    # Back trace a url to a view
    def get_absolute_url(self):
        return reverse('driver-detail', kwargs={'pk': self.pk})

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
def query_driver(user=None):
    if user:
        objects = Driver.objects.filter(user=user)
    else:
        objects = Driver.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_driver(user,id):
    a =  Driver.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Print a driver as a table of fields
def print_driver(driver):
    for x in driver.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Show the object in several different forms
def show_driver(driver):
    print 'Driver:', driver.name
    print 'Fields:', driver.fields()
    print 'Values:', driver.values()
    print 'Table:', driver.table()
    print_driver(driver)


# Generate a new record if needed
def add_fake_driver(name):
    print 'Make driver: ', name
    c = Driver()
    #c.name = name
    #c.address = 'Here'
    #c.phone = '900-555-1212'
    c.save()
    return c


# Perform a test on this object type
def test_code():

    # Count current records
    num_drivers = len(query_driver())
    print '%d Drivers' % num_drivers

    # Delete all records
    #Driver.objects.all().delete()

    # If there are no drivers then make some
    if num_drivers<1:
        fake_names = [ 'Tom', 'Jerry', 'Billy', 'Bob' ]
        for c in fake_names:
            add_fake_driver(c)

    # Print a list of all names
    all = Driver.objects.all()
    print 'Driver list:  %d records' % len(all)
    for c in all:
        print_driver(c)

