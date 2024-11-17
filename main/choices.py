from django.db import models


class CouponType(models.IntegerChoices):
    CART_WISE = 1, 'cart-wise'
    PRODUCT_WISE = 2, 'product-wise'
    BxGy = 3, 'BxGy'


class DiscountType(models.IntegerChoices):
    PERCENTAGE = 1, 'Percentage'
    FIXED = 2, 'Fixed Amount'


class ConditionType(models.IntegerChoices):
    MAX_DISCOUNT_AMOUNT = 1, 'Max Discount Amount'


class CartStatus(models.IntegerChoices):
    ACTIVE = 1, 'Active'
    ORDER_PLACED = 2, 'Order Placed'
