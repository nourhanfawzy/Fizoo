from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Library(models.Model):
	name = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	def __unicode__(self):
		return unicode(self.name)
	def get_absolute_url(self):
		return reverse('library-detail', kwargs={'pk': self.pk})



class Book(models.Model):
	name = models.CharField(max_length=50)
	year = models.IntegerField(blank=False)
	about = models.CharField(max_length=500)
	library = models.ForeignKey(Library, null=True)
	def __unicode__(self):
		return unicode(self.name)
	def get_absolute_url(self):
		return reverse('book-detail', kwargs={'pk': self.pk})
