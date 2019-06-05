from django.db import models

class Post(models.Model):
    content = models.TextField(max_length=140, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d')

    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_content(self):
        print('self: ', self.content.all())
        return self.content.all()
