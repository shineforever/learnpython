from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name=u"出版社名称")
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = u"出版社"


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = u"作者"


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"书名")
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(verbose_name=u"出版日期")

    def __str__(self):
        return "《{}》".format(self.title)

    class Meta:
        verbose_name_plural = "书名"
