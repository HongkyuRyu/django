from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, db_column='UserID', blank=False)
    title = models.CharField(db_column='Title', max_length=32, blank=True, null=True)
    contents = models.TextField(db_column='Contents', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'Post'
        ordering = ['-created_at']
    def __str__(self) -> str:
        return self.title
    

    
