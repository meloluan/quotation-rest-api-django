# Generated by Django 2.2.1 on 2019-05-31 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190531_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='droidparts',
            name='user',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
