from django.db import models

class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')  # Images will be saved to 'images/' folder inside media directory
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title