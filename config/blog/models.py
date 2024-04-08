from django.db import models
import os
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/', null=True)

    def __str__(self):
        return self.title

    #부모 클래스 즉, models.Model 클래스가 갖고 있는 delete()메소드를 오버라이딩하여 image일 경우를 추가
    #또한 이미지가 아닐 땐 부모객체를 super를 통해 불러와 delete() 메소드 그대로 사용
    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(Blog, self).delete(*args, **kargs)