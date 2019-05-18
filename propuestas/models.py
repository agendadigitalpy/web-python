from djongo import models

# Create your models here.
class Proposal(models.Model):
	"""docstring for Proposal"""
	name = models.TextField()
	email = models.EmailField()
	category = models.TextField()
	title = models.TextField()
	content = models.TextField()
	approved = models.BooleanField()

	def __str__(self):
		return self.name
		