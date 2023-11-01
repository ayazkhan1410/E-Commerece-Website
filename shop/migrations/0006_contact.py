# Generated by Django 4.2.5 on 2023-10-30 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=' ', max_length=50)),
                ('email', models.EmailField(default=' ', max_length=60)),
                ('phone', models.CharField(default=' ', max_length=50)),
                ('desc', models.CharField(default=' ', max_length=500)),
            ],
        ),
    ]