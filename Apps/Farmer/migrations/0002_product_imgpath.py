from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farmer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imgPath',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
