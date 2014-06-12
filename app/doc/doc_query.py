# doc/doc.py
# Model for Doc records

from django.contrib.auth.models import User
from os.path import exists,isdir
from os import listdir

from doc_model import Doc
from faker import fake_name,fake_address,fake_phone_number,fake_company


DOC_ROOT = '/home/seaman/Documents/MyBook'


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
    for x in doc.table()[:-1]:
        print '    %-10s:  %s' % (x[0],x[1])
    x =  doc.table()[-1]
    print '    %-10s:  %d characters' % (x[0],len(x[1]))
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


# Lookup the user by name
def get_user(name):
    return  User.objects.get(username=name)


# Find the record if it exists
def lookup_doc(path):
    o =  Doc.objects.filter(path=path)
    if len(o)==1:
       return o[0]


# Show the record for a document
def show_doc(user, path):
    u = get_user('seaman')
    print 'User:', u.username
    x = lookup_doc(path)
    if x:
        print_doc(x)
    print 
    print  x.table()[-1][1]
    print


# Add a new doc record
def add_doc(user, path, title, content):
    o =  Doc.objects.filter(path=path)
    if len(o)==1:
        c = o[0]
    else:
        c = Doc()
    c.user = user
    c.path = path
    c.title = title
    c.text = content
    c.save()
    return c


# Remove the all docs from the database
def reset_doc_list():
    Doc.objects.all().delete()


# Get the doc path within the doc tree
def get_path(path):
    return path.replace(DOC_ROOT+'/','')


# Extract the page title from the content
def get_title(content):
  t = content.split('\n')[0]
  t = t.replace('-*-muse-*-','')
  t = t.replace('*','')
  return t.strip()


# Read the contents of a file
def get_content(path):
    return open(path).read()


# Create a record by reading a file
def import_doc(path):
    if exists(path):
        if isdir(path):
            print 'Directory:',path
            for f in listdir(path):
                import_doc(path+'/'+f)
        else:
            content = get_content(path)
            d = add_doc( get_user('seaman'), get_path(path),get_title(content),content)
            print 'import_doc : ', get_title(content)
    else:
        print 'No file:',path


# Perform a test on doc. If there are no docs then make some.
def test_code():
    reset_doc_list()
    if len(Doc.objects.all())<1:
       how_many = 4
       for c in range(how_many):
           add_fake_doc()
    print '%d Doc Records'%(len(query_doc()))

