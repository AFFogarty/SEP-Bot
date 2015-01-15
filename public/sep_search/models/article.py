from django.db import models

class Article(models.Model):
    class Meta:
        app_label = "sep_search"
    # The title of the article
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField()
    # Summary from top of page
    summary = models.TextField(blank=True, null=True)
    # Headings
    headings = models.TextField(blank=True, null=True)
    # Content
    content = models.TextField(blank=True, null=True)
    # The author of the article
    author = models.ForeignKey("sep_search.Author", blank=True, null=True)
    # The last time this entry was updated in the system.
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{0}. "{1}".'.format(self.author, self.title)
