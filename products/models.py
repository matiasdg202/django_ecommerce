from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    section = models.ForeignKey(
        Section, related_name="categories", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="product_images/", blank=False, null=False)
    num_of_ratings = models.IntegerField(default=0, editable=False)
    sum_of_ratings = models.IntegerField(default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def average_rating(self):
        if self.num_of_ratings > 0:
            return self.sum_of_ratings / self.num_of_ratings
        else:
            return 0
