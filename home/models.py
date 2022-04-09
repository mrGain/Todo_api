from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now_add = True)

    class Meta:
        abstract = True


class Todo(BaseModel):
    todo_title = models.CharField(max_length=100)
    todo_description = models.TextField()
    is_done = models.BooleanField(default=False)
