# Data types to create for this application

data_types = {

   #-----------------------------------------------------------------------------

    'Doc': {
        'module': 'doc',
        'class': 
'''
class Doc(models.Model):

    user    = models.ForeignKey(User)
    path    = models.CharField (max_length=200)
    title   = models.CharField (max_length=200)
    text    = models.TextField ()
    time    = models.DateTimeField(auto_now=True)  
'''

    },

    #-----------------------------------------------------------------------------

    'Time': {
        'module': 'time',
        'class': 
'''
class Time(models.Model):

    user    = models.ForeignKey(User)
    name    = models.CharField (max_length=200)
    task    = models.CharField (max_length=40)
    date    = models.DateField(auto_now_add=True)  
    minutes = models.IntegerField(default='60')
'''

    },

}
