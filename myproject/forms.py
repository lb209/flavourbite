
from django import forms

from home.models import Student, Book


class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = ['name', 'email']


class BookForm(forms.ModelForm):

    class Meta:

        model = Book

        fields = ['book_name', 'author', 'price']

