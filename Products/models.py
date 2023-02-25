from django.db import models
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


class Products(models.Model):
    product_id = models.AutoField(primary_key=True, null=False)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(max_length=300)
    product_color = models.CharField(max_length=30)
    product_available = models.BooleanField(default=True)
    product_discount = models.CharField(max_length=20)
    product_added_date = models.DateTimeField(auto_now=True)
    product_search_image = models.ImageField(upload_to=env('SEARCH_IMAGE_DIR'))
    product_unique_array = models.JSONField(null=True)
    # product_search_image = models.ImageField()
    # product_images = models.ArrayField(
    #     model_container=models.ImageField
    # )

    # Foreign Key of Category Model
    # product_category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    # TODO
    # product_supplier_id

    # choice = models.CharField(
    #     max_length=100, choices=(("IT", "IT"), ("AI", "AI")))

    @property
    def sales_price(self):
        return "Sales Price will show here"

    def get_discount(self):
        return "Discount will show here"

    def __str__(self):
        return self.product_name + ""
