# doc/doc.py
# Model for Doc records

from django.contrib.auth.models import User

from doc_model import Doc


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


# Generate a new record if needed
def add_fake_doc(name):
    print 'Make doc: ', name
    c = Doc()
    #c.user = User.objects.get(name='TestRobot')
    #c.name = name
    #c.address = 'Here'
    #c.phone = '900-555-1212'
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
