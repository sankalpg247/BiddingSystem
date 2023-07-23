from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citizenName', models.CharField(max_length=200)),
                ('productName', models.CharField(max_length=200)),
                ('qty', models.IntegerField()),
                ('amountPaid', models.FloatField()),
                ('contact', models.BigIntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
