# doc/doc.py
# Model for Doc records

from django.contrib.auth.models import User

from doc_model import Doc
from faker import fake_name,fake_address,fake_phone_number,fake_company


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


# Print the object fields as a table
def print_doc(doc):
    for x in doc.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Print the object list as a table
def print_doc_list():
    all = Doc.objects.all()
    print 'Doc list:  %d records' % len(all)
    for c in all:
        print_doc(c)


# Generate a new record if needed
def add_fake_doc():
    c = Doc()
    c.user = User.objects.get(username='TestRobot')
    name = fake_name()
    c.path = name
    c.title = name
    c.text = ' '.join([ fake_name() for n in range(20) ])
    c.save()
    return c


# Remove the all docs from the database
def reset_doc_list():
    Doc.objects.all().delete()


# Perform a test on doc. If there are no docs then make some.
def test_code():
    reset_doc_list()
    if len(Doc.objects.all())<1:
       how_many = 4
       for c in range(how_many):
           add_fake_doc()
    print_doc_list()
    print 'hey'

