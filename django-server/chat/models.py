
from django.contrib.auth.models import User



from django.db import models


class Chat(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name="chats")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_message = models.ForeignKey("Message", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    chat_id = models.ForeignKey(Chat, on_delete=models.PROTECT, related_name="messages")
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name="messages")
    is_system = models.BooleanField(default=False)
    data = models.JSONField(null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.username} - {self.content[:20]}"