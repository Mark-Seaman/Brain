
data_types = {

    #-----------------------------------------------------------------------------

    'Contact': {
        'module': brain,
        'class': 
'''

# Contact
class Contact(models.Model):
    name    = models.CharField (max_length=40)
    address = models.CharField (max_length=100)    
    phone   = models.CharField (max_length=15)
    user    = models.ForeignKey(User)

'''

    },

    #-----------------------------------------------------------------------------

    'Doc': {
        'module': doc,
        'class': 
'''

# Doc
class doc(models.Model):
    user    = models.ForeignKey(User)
    path    = models.CharField (max_length=200)
    title   = models.CharField (max_length=200)
    text    = models.TextField ()

'''

    },

}

