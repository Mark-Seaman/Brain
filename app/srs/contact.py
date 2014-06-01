# srs/contact.py
# Model for Contact records

# Django imports
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
 
# SRS imports

    
# Define a contact data type
class Contact(models.Model):
    name    = models.CharField (max_length=40)
    address = models.CharField (max_length=100)    
    phone   = models.CharField (max_length=15)
    user    = models.ForeignKey(User)


    # Format a record as a string
    def __unicode__(self):
        return self.name + ',' + self.phone + ',' + self.address

    # Back trace a url to a view
    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})

    # Object field handling
    def __iter__(self):
        for i in self.fields():
            yield (i, getattr(self, i))
    def fields(self):
        return [ f.name for f in self._meta.fields ]
    def values(self):
        return [ v for f,v in self ]
    def table(self):
        return zip(self.fields(),self.values())



# Get a table listing from the database
def query_contact(user=None):
    if user:
        objects = Contact.objects.filter(user=user)
    else:
        objects =  Contact.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_contact(user,id):
    a =  Contact.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Print a contact as a table of fields
def print_contact(contact):
    for x in contact.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Show the object in several different forms
def show_contact(contact):
    print 'Contact:', contact.name
    print 'Fields:', contact.fields()
    print 'Values:', contact.values()
    print 'Table:', contact.table()
    print_contact(contact)


# Generate a new record if needed
def add_fake_contact(name):
    print 'Make contact: ', name
    c = Contact()
    c.name = name
    c.user = User.objects.get(username='TestRobot')
    c.address = 'Here'
    c.phone = '900-555-1212'
    c.save()
    return c


# Perform a test on this object type
def test_code():

    # Count current records
    num_contacts = len(query_contact())
    print '%d Contacts' % num_contacts

    # Delete all records
    #Contact.objects.all().delete()

    # If there are no contacts then make some
    if num_contacts<1:
        fake_names = [ 'Tom', 'Jerry', 'Billy', 'Bob' ]
        for c in fake_names:
            add_fake_contact(c)

    # Print a list of all names
    all = Contact.objects.all()
    print 'Contact list:  %d records' % len(all)
    for c in all:
        print_contact(c)

