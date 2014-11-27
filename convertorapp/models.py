import os
import uuid

from django.db import models
from django.contrib.auth.models import User
from convertor.settings import MEDIA_ROOT

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(MEDIA_ROOT,filename)

class Details(models.Model):
	user = models.ForeignKey(User)
	file_name = models.FileField(upload_to=get_file_path)
	output_text = models.TextField()