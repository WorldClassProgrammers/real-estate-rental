# Generated by Django 3.1.3 on 2020-11-08 05:47

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import estate.models.condo
import estate.models.room
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(max_length=500)),
                ('number_of_floors', models.IntegerField(default=1)),
                ('juristic_persons_number', models.TextField(max_length=25)),
                ('common_fee_account', models.TextField(max_length=25)),
                ('amenities', multiselectfield.db.fields.MultiSelectField(choices=[('elevator', 'Elevator'), ('parking_lot', 'Parking Lot'), ('cctv', 'CCTV'), ('security', 'Security'), ('wifi', 'WiFi'), ('swimming_pool', 'Swimming Pool'), ('sauna', 'Sauna'), ('garden', 'Garden'), ('playground', 'Playground'), ('gym', 'Gym'), ('shop', 'Shop'), ('restaurant', 'Restaurant')], default=None, max_length=97)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('line_id', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='1', max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('still_on_contract', models.BooleanField(default=False)),
                ('price_for_rent', models.FloatField(default=0)),
                ('price_for_sell', models.FloatField(default=0)),
                ('floor_number', models.CharField(default='1', max_length=10)),
                ('number_of_bedroom', models.IntegerField(default=1)),
                ('number_of_bathroom', models.IntegerField(default=1)),
                ('area', models.FloatField(default=0)),
                ('condo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate.condo')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='estate.owner')),
            ],
        ),
        migrations.CreateModel(
            name='RoomImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=estate.models.room.conference_directory_path)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate.room')),
            ],
        ),
        migrations.CreateModel(
            name='CondoImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=estate.models.condo.conference_directory_path)),
                ('condo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate.condo')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'visitor'), (2, 'owner')])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='estate.owner')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
