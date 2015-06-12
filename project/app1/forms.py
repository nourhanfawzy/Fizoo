from django import forms
from django.forms import ModelForm
from app1.models import Book


class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = ['name', 'year', 'about']