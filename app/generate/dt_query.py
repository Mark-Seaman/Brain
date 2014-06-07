# module_name/data_type.py
# Model for Data_Type records

from django.contrib.auth.models import User

from data_type_model import Data_Type
#from faker import fake_name,fake_address,fake_phone_number,fake_company


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


# Print the object fields as a table
def print_data_type(data_type):
    for x in data_type.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Print the object list as a table
def print_data_type_list():
    all = Data_Type.objects.all()
    print 'Data_Type list:  %d records' % len(all)
    for c in all:
        print_data_type(c)


# Generate a new record if needed
def add_fake_data_type():
    c = Data_Type()
    # c.user = User.objects.get(username='TestRobot')
    # c.name = fake_name()
    # c.address = fake_address()
    # c.phone = fake_phone_number()
    c.save()
    return c


# Remove the all data_types from the database
def reset_data_type_list():
    Data_Type.objects.all().delete()


# Perform a test on data_type. If there are no data_types then make some.
def test_code():
    if len(Data_Type.objects.all())<1:
        how_many = 4
        for c in range(how_many):
            add_fake_data_type()
    print_data_type_list()
    

