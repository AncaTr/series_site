import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
class Migration(migrations.Migration):
    initial = True
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name='Gen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SeriesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='Tara',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlu', models.CharField(max_length=200)),
                ('descriere', models.TextField()),
                ('genuri', models.ManyToManyField(to='main.gen')),
                ('tara', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tara')),
            ],
        ),
        migrations.CreateModel(
            name='Comentariu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('creat_la', models.DateTimeField(auto_now_add=True)),
                ('utilizator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.serial')),
            ],
        ),
    ]
