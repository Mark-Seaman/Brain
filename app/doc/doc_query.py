# doc/doc_query.py
# Model for Doc records

#from django.contrib.auth.models import User

from doc_model import Doc

from faker import fake_name


# Get a table listing from the database
def select_doc(user=None):
    if user:
        return Doc.objects.filter(user=user)
    else:
        return Doc.objects.all()
    return [ f.values() for f in objects ]


# Get a table listing from the database
def query_doc(user=None):
    return [ f.values() for f in select_doc(user) ]


# Return a single contact
def get_doc(user,id):
    a =  Doc.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Count the saved Doc records
def count():
    return len(Doc.objects.all())


# Print the object fields as a table
def print_doc(doc):
    for x in doc.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Print the object list as a table
def print_list():
    all = Doc.objects.all()
    print 'Doc list:  %d records' % len(all)
    for c in all:
        print_doc(c)


# Remove the all docs from the database
def reset_list():
    Doc.objects.all().delete()


# Add a new record from a file
def add_doc(data):
    o =  Doc.objects.filter(name=data[0])
    if len(o)==1:
        c = o[0]
    else:
        c = Doc()
    #c.name, c.address, c.phone = data
    c.save()
    return c


# Add some fake Doc records
def add_fake_doc(num=1):
    for i in range(num):
        data = [fake_name()]
        add_doc(data)


# Test Doc code
def test_doc():
    if count()<10:
        add_fake_doc(1)


