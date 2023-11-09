from django.db import models

# Create your models here.
class Instrument(models.Model):
    # General Information
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='instrument_images/', null=True, blank=True)

    # Pricing and Availability
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.PositiveIntegerField()

    # Technical Details
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    condition = models.CharField(max_length=50)

    # Seller Information (if applicable)
    seller_name = models.CharField(max_length=255, null=True, blank=True)
    seller_contact = models.EmailField(null=True, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name