from django.db import models
from main.choices import *


class User(models.Model):

    id = models.BigAutoField(db_column='ID', primary_key=True)
    email = models.CharField(max_length=100, null=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)


class Cart(models.Model):
    user = models.ForeignKey(User, related_name="carts",
                             on_delete=models.CASCADE)
    status = models.IntegerField(
        default=CartStatus.ACTIVE, choices=CartStatus.choices)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items",
                             on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="cart_items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


# Basic Details of all type of coupons
class Coupon(models.Model):

    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20, unique=True)
    type = models.IntegerField(choices=CouponType.choices)
    is_active = models.BooleanField(default=True)
    discount_type = models.CharField(
        max_length=10, choices=DiscountType.choices, null=True)
    discount_value = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)


# Conditions, not used in db query, but in business login
# Different conditions can be added in future according to requirement
class CouponCondition(models.Model):
    coupon = models.ForeignKey(
        Coupon, related_name="conditions", on_delete=models.CASCADE)
    condition_type = models.IntegerField(choices=ConditionType.choices)
    condition_value = models.CharField(max_length=50)

# Cart wise coupon details


class CouponCart(models.Model):
    coupon = models.ForeignKey(
        Coupon, related_name="coupon_cart_details", on_delete=models.CASCADE)
    min_cart_total = models.PositiveIntegerField(default=0)


# Product wise coupon details
class CouponProduct(models.Model):
    coupon = models.ForeignKey(
        Coupon, related_name="coupon_products_details", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="applicable_coupons", on_delete=models.CASCADE)

# But X Get Y coupon details


class CouponBxGy(models.Model):
    coupon = models.ForeignKey(
        Coupon, related_name="coupon_bxgy_details", on_delete=models.CASCADE)
    buy_products = models.ManyToManyField(
        Product, related_name="buy_bxgy_coupons")
    buy_product_count = models.PositiveIntegerField()
    get_products = models.ManyToManyField(
        Product, related_name="get_bxgy_coupons")
    get_product_count = models.PositiveIntegerField()

# Coupon Application History


class AppliedCoupon(models.Model):
    cart = models.ForeignKey(
        Cart, related_name="applied_coupons", on_delete=models.CASCADE)
    coupon = models.ForeignKey(
        Coupon, related_name="applied_carts", on_delete=models.CASCADE)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
