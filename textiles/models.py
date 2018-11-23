from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    INSTANT = 0
    IN_DAYS = 1
    IN_A_WEEK = 2
    IN_A_MONTH = 3
    
    YEAR_IN_SCHOOL_CHOICES = (
        (INSTANT, 'Instant'),
        (IN_DAYS, 'In 1-2 Days'),
        (IN_A_WEEK, 'In 7-8 Days'),
        (IN_A_MONTH, 'In 30 days'),
    )
    
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"
    EXTRA_LARGE = "XL"
    DOUBLE_EXTRA_LARGE = "XXL"
    TRIPLE_EXTRA_LARGE = "XXXL"
    
    
    SIZE_CHOICES = (
        (SMALL, "S"),
        (MEDIUM, 'M'),
        (LARGE, "L"),
        (EXTRA_LARGE, "XL"),
        (DOUBLE_EXTRA_LARGE, "XXL"),
        (TRIPLE_EXTRA_LARGE, "XXXL"),
        
    )
    SEMI_STICHED = "SS"
    STICHED = "S"
    UNSTICHED = "US"
    
    
    
    STICHING_CHOICES = (
        (SEMI_STICHED, "SS"),
        (STICHED, "S"),
        (UNSTICHED, "US"),
        
    )
    product_name = models.CharField(max_length=500)
    product_id = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    product_detail = models.CharField(max_length = 5000)
    length = models.DecimalField(max_digits=5, decimal_places=4)
    size = models.CharField(choices=SIZE_CHOICES, max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    stiched_type = models.CharField(choices=STICHING_CHOICES, max_length=100, null=True, blank=True)
    material = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount_rate = models.IntegerField()
    discount_percent = models.DecimalField(max_digits=5, decimal_places=4)
    stock_balance = models.PositiveIntegerField()
    dispatch_in = models.PositiveIntegerField(choices=YEAR_IN_SCHOOL_CHOICES, null=True, blank=True)
    free_shipping = models.BooleanField(default=False)
    care = models.CharField(max_length=100)
    

    def __str__(self):
        return self.product_name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='product_image', on_delete=models.CASCADE)
    image = models.ImageField()
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label


class SubProduct(models.Model):
    product = models.ForeignKey(Product, related_name='sub_product', on_delete=models.CASCADE)
    sub_product_name = models.CharField(max_length=500)
    material = models.CharField(max_length=100)
    length = models.DecimalField(max_digits=5, decimal_places=4)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_product_name 

# class PaytmHistory(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rel_payment_paytm', on_delete=models.CASCADE)
#     ORDERID = models.CharField('ORDER ID', max_length=30)
#     TXNDATE = models.DateTimeField('TXN DATE', default=timezone.now)
#     TXNID = models.IntegerField('TXN ID')
#     BANKTXNID = models.IntegerField('BANK TXN ID', null=True, blank=True)
#     BANKNAME = models.CharField('BANK NAME', max_length=50, null=True, blank=True)
#     RESPCODE = models.IntegerField('RESP CODE')
#     PAYMENTMODE = models.CharField('PAYMENT MODE', max_length=10, null=True, blank=True)
#     CURRENCY = models.CharField('CURRENCY', max_length=4, null=True, blank=True)
#     GATEWAYNAME = models.CharField("GATEWAY NAME", max_length=30, null=True, blank=True)
#     MID = models.CharField(max_length=40)
#     RESPMSG = models.TextField('RESP MSG', max_length=250)
#     TXNAMOUNT = models.FloatField('TXN AMOUNT')
#     STATUS = models.CharField('STATUS', max_length=12)

#     # class Meta:
#     #     app_label = 'paytm'

#     def __str__(self):
#         return self.STATUS