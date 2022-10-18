from django.db import models
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

# category_status = models.BigIntegerField(default=0)
class SubCategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    subcategory_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.PROTECT)
    def __str__(self):
        return self.subcategory_name


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=50)
    book_category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.PROTECT)
    book_quantity = models.BigIntegerField(default=0)
    book_price = models.BigIntegerField(default=0)
    book_oldprice = models.BigIntegerField(default=0)
    book_author = models.CharField(max_length=50)
    book_year = models.BigIntegerField(default=0)
    book_language = models.CharField(max_length=50)
    book_publisher = models.CharField(max_length=50)
    book_status = models.BigIntegerField(default=0)
    book_desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics', default=0)
    def __str__(self):
        return self.book_name
# Create your models here.
