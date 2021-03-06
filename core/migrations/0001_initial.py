# Generated by Django 2.2.1 on 2019-05-22 11:55

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
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=50)),
                ('dealing_type', models.CharField(choices=[('R', 'RENT'), ('S', 'SALE'), ('L', 'LEASE')], max_length=20)),
                ('is_available', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Lease',
            fields=[
                ('house', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.House')),
                ('price', models.IntegerField()),
                ('period', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('house', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.House')),
                ('advance', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('house', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.House')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('area', models.CharField(max_length=100)),
                ('link', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='house',
            name='belongs_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Person'),
        ),
    ]
