# Generated by Django 3.0.4 on 2020-03-07 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Not to disclose')], default=2, max_length=2),
            preserve_default=False,
        ),
    ]
