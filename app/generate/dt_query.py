# module_name/data_type.py
# Model for Data_Type records

from django.contrib.auth.models import User

from data_type_model import Data_Type


# Get a table listing from the database
def query_data_type(user=None):
    if user:
        objects = Data_Type.objects.filter(user=user)
    else:
        objects = Data_Type.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_data_type(user,id):
    a =  Data_Type.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Generate a new record if needed
def add_fake_data_type(name):
    print 'Make data_type: ', name
    c = Data_Type()
    #c.user = User.objects.get(name='TestRobot')
    #c.name = name
    #c.address = 'Here'
    #c.phone = '900-555-1212'
    c.save()
    return c


# Perform a test on this object type
def test_code():

    # Count current records
    num_data_types = len(query_data_type())
    print '%d Data_Types' % num_data_types

    # Delete all records
    #Data_Type.objects.all().delete()

    # If there are no data_types then make some
    if num_data_types<1:
        fake_names = [ 'Tom', 'Jerry', 'Billy', 'Bob' ]
        for c in fake_names:
            add_fake_data_type(c)

    # Print a list of all names
    all = Data_Type.objects.all()
    print 'Data_Type list:  %d records' % len(all)
    for c in all:
        print_data_type(c)

