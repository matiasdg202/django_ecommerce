from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="category_images/", blank=False, null=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category, related_name="subcategories", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="subcategory_images/", blank=False, null=False)

    class Meta:
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return self.name


class Product(models.Model):
    subcategory = models.ForeignKey(
        SubCategory, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product_images/", blank=False, null=False)
    num_of_ratings = models.IntegerField(default=0)
    sum_of_ratings = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def average_rating(self):
        if self.num_of_ratings > 0:
            return self.sum_of_ratings / self.num_of_ratings
        else:
            return 0
