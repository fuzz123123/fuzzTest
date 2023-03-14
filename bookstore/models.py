from django.db import models


class Publisher(models.Model):
    """出版社"""
    name = models.CharField('名称', max_length=50, unique=True)

    class Meta:
        db_table = 'publisher'


# Create your models here.
class Book(models.Model):
    title = models.CharField('书名', max_length=50, default='', unique=True)
    price = models.DecimalField('价格', max_digits=7, decimal_places=2)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, default=None)
    market_price = models.DecimalField('图书零售价', max_digits=7, decimal_places=2, default=0.0)
    is_active = models.BooleanField('数据是否有效', default=True)

    class Meta:
        db_table = 'book'
        verbose_name = 'a_funny_name'
        verbose_name_plural = 'funny_names'

    def __str__(self):
        return '%s_%s_%s_%s' % (self.title, self.price, self.publisher.name, self.market_price)


class Author(models.Model):
    name = models.CharField('姓名', max_length=11, default='')
    age = models.IntegerField('年龄', default=1)
    email = models.EmailField('邮箱', null=True)
    book = models.ManyToManyField(Book)

    class Meta:
        db_table = 'author'


class Wife(models.Model):
    """作家妻子类"""
    name = models.CharField("妻子", max_length=50)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'wife'



