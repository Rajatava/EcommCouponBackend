# Generated by Django 4.2.7 on 2024-11-17 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Order Placed')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('type', models.IntegerField(choices=[(1, 'cart-wise'), (2, 'product-wise'), (3, 'BxGy')])),
                ('is_active', models.BooleanField(default=True)),
                ('discount_type', models.CharField(choices=[(1, 'Percentage'), (2, 'Fixed Amount')], max_length=10, null=True)),
                ('discount_value', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CouponProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupon_products_details', to='main.coupon')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicable_coupons', to='main.product')),
            ],
        ),
        migrations.CreateModel(
            name='CouponCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition_type', models.IntegerField(choices=[(1, 'Max Discount Amount')])),
                ('condition_value', models.CharField(max_length=50)),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conditions', to='main.coupon')),
            ],
        ),
        migrations.CreateModel(
            name='CouponCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_cart_total', models.PositiveIntegerField(default=0)),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupon_cart_details', to='main.coupon')),
            ],
        ),
        migrations.CreateModel(
            name='CouponBxGy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_product_count', models.PositiveIntegerField()),
                ('get_product_count', models.PositiveIntegerField()),
                ('buy_products', models.ManyToManyField(related_name='buy_bxgy_coupons', to='main.product')),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupon_bxgy_details', to='main.coupon')),
                ('get_products', models.ManyToManyField(related_name='get_bxgy_coupons', to='main.product')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='main.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='main.product')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='main.user'),
        ),
        migrations.CreateModel(
            name='AppliedCoupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_coupons', to='main.cart')),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_carts', to='main.coupon')),
            ],
        ),
    ]