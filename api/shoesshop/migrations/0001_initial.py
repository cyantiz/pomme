# Generated by Django 4.1.2 on 2022-11-20 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100)),
                ('province_id', models.PositiveBigIntegerField()),
                ('district_id', models.PositiveBigIntegerField()),
                ('commune_id', models.PositiveBigIntegerField()),
                ('status', models.IntegerField(choices=[(0, 'in progress'), (1, 'shipping'), (2, 'done')], default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('salePercent', models.FloatField()),
                ('in_stock', models.PositiveBigIntegerField()),
                ('sold', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('shoe_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Both')], default=0)),
                ('series', models.CharField(max_length=100)),
                ('shape', models.BooleanField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoes', to='shoesshop.product')),
            ],
        ),
        migrations.CreateModel(
            name='UserLoveProduct',
            fields=[
                ('user_love_product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_love_products', to='shoesshop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_love_products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserCartProduct',
            fields=[
                ('user_cart_product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_cart_products', to='shoesshop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_cart_products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeChild',
            fields=[
                ('shoe_child_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('in_stock', models.PositiveBigIntegerField()),
                ('size', models.PositiveBigIntegerField()),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoe_childs', to='shoesshop.shoe')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('order_product_id', models.AutoField(primary_key=True, serialize=False)),
                ('price_at_order', models.PositiveBigIntegerField()),
                ('quantity', models.PositiveBigIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='shoesshop.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='shoesshop.product')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_thumbnail', models.BooleanField()),
                ('url', models.URLField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shoesshop.product')),
            ],
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('clothes_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.IntegerField(choices=[(0, 'Tee'), (1, 'Hoodie'), (2, 'Sweatshirt')], default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes', to='shoesshop.product')),
            ],
        ),
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('accessory_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.IntegerField(choices=[(0, 'Shock'), (1, 'Tote'), (2, 'Backpack'), (3, 'Shoelace')], default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accessories', to='shoesshop.product')),
            ],
        ),
    ]
