from django.db import models

class Author(models.Model):
    class Meta:
        app_label = "sep_search"

    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u"{0}, {1}".format(self.last_name, self.first_name)
