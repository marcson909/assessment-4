# Generated by Django 3.2.5 on 2021-07-16 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('craig_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent_cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='craig_app.category'),
        ),
    ]
