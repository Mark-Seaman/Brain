# Data types to create for this application

data_types = {

   #-----------------------------------------------------------------------------

    'Doc': {
        'module': 'doc',
        'class': 
'''
from datetime import datetime

class Doc(models.Model):

    user    = models.ForeignKey(User)
    path    = models.CharField (max_length=200)
    title   = models.CharField (max_length=200)
    text    = models.TextField ()
    name    = models.CharField (max_length=40)
    time    = models.DateTimeField(default=datetime.now())  
'''

    },

    #-----------------------------------------------------------------------------

}
