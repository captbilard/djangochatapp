# Generated by Django 4.0 on 2022-03-27 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rooms',
            options={'verbose_name_plural': 'Rooms'},
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='rooms.rooms')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='auth.user')),
            ],
            options={
                'ordering': ('date_added',),
            },
        ),
    ]
