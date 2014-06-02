
data_types = {
    'Contact': {
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

}

