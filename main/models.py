from django.db import models

class CodeBlock(models.Model):
    title = models.CharField(max_length=32)
    code = models.TextField(blank=True, null=True, default=None)
    solution = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return self.title
