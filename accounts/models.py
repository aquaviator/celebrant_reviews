from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    celebrant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')  # Link to the celebrant
    content = models.TextField()  # The content of the review
    author_name = models.CharField(max_length=100)  # The name of the client submitting the review
    date_posted = models.DateTimeField(auto_now_add=True)  # Automatically add the date of submission

    def __str__(self):
        return f'Review by {self.author_name} for {self.celebrant.username}'
