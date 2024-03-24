from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
language_choice=(
    ("solidity","solidity"),
    ("Next.js","Next.js"),
    ("solana","solana"),
    ("python","python"),
    ("django","django"),
    ("javascript","javascript"),
    ("react","react"),
    ("java","java")
 )
class sample(models.Model):
    topic=models.CharField(max_length=100)
    language=models.CharField(max_length=50,choices=language_choice,default="solidity")
    discription=models.TextField()
    information=RichTextField()
    def __str__(self):
        return self.topic
