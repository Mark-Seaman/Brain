# doc/doc.py
# Model for Doc records


#############################################################################
# DO NOT EDIT THIS FILE
# This Code will be replaced by the code generator
#############################################################################

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


    
class Doc(models.Model):

    user    = models.ForeignKey(User)
    path    = models.CharField (max_length=200)
    title   = models.CharField (max_length=200)
    text    = models.TextField ()
    time    = models.DateTimeField(auto_now=True)  


    # Format a record as a string
    def __unicode__(self):
        return self.name

    # Back trace a url to a view
    def get_absolute_url(self):
        return reverse('doc-detail', kwargs={'pk': self.pk})

    # Object field handling
    def __iter__(self):
        for i in self.fields():
            yield (i, getattr(self, i))

    # Enumerate the fields
    def fields(self):
        return [ f.name for f in self._meta.fields ]

    # List of values
    def values(self):
        return [ v for f,v in self ]

    # Table of field labels and values
    def table(self):
        return zip(self.fields(),self.values())

