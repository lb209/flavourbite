from django.db import models
from django.contrib.auth.models import User

# آپ کے پرانے ماڈلز (ایسے ہی رہیں گے)
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    students = models.ManyToManyField(Student, related_name="books")

    def __str__(self):
        return self.book_name

# نیا ماڈل آرڈرز اور گراف کو ہینڈل کرنے کے لیے
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    card_number = models.CharField(max_length=11)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Completed')  # Completed, Ongoing, Cancelled
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - ${self.total_price}"