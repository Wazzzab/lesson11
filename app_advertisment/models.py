from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.


class Advertisement(models.Model):  # это класс-модель
    # он реализует таблицу Advertisement
    title = models.CharField("заголовок", max_length=128)
    text = models.TextField("описание")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField("цена")
    auction = models.BooleanField("торг", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    image = models.ImageField("image")

    class Meta:
        db_table = "advertisement"

    def __str__(self):
        return f"<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>"
