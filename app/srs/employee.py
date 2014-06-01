# srs/employee.py
# Model for Employee records

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

    
# Define a contact data type
class Employee(models.Model):
    name    = models.CharField (max_length=40)
    user    = models.ForeignKey(User)


    # Format a record as a string
    def __unicode__(self):
        return self.name

    # Back trace a url to a view
    def get_absolute_url(self):
        return reverse('employee-detail', kwargs={'pk': self.pk})

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
def query_employee(user=None):
    if user:
        objects = Employee.objects.filter(user=user)
    else:
        objects = Employee.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_employee(user,id):
    a =  Employee.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Print a employee as a table of fields
def print_employee(employee):
    for x in employee.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Show the object in several different forms
def show_employee(employee):
    print 'Employee:', employee.name
    print 'Fields:', employee.fields()
    print 'Values:', employee.values()
    print 'Table:', employee.table()
    print_employee(employee)


# Generate a new record if needed
def add_fake_employee(name):
    print 'Make employee: ', name
    c = Employee()
    #c.name = name
    #c.address = 'Here'
    #c.phone = '900-555-1212'
    c.save()
    return c


# Perform a test on this object type
def test_code():

    # Count current records
    num_employees = len(query_employee())
    print '%d Employees' % num_employees

    # Delete all records
    #Employee.objects.all().delete()

    # If there are no employees then make some
    if num_employees<1:
        fake_names = [ 'Tom', 'Jerry', 'Billy', 'Bob' ]
        for c in fake_names:
            add_fake_employee(c)

    # Print a list of all names
    all = Employee.objects.all()
    print 'Employee list:  %d records' % len(all)
    for c in all:
        print_employee(c)

