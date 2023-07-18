from django.db import models

# Create your models here.
class Feature:
    title: str
    user: str
    views: str
    time: int
    is_verified = bool
    
    img: str
    song: str