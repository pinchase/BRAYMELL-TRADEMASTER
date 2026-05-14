# Generated migration for Client and Brand models restructuring

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        # Create Client model
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(help_text='URL slug (auto-generated if not provided)', max_length=200, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'ordering': ['name'],
            },
        ),
        # Create Brand model
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='brand_logos/')),
                ('order', models.PositiveIntegerField(default=0, help_text='Display priority order')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='core.client')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
                'ordering': ['order', 'name'],
                'unique_together': {('client', 'name')},
            },
        ),
        # Add brand field to Project (initially nullable to populate data)
        migrations.AddField(
            model_name='project',
            name='brand',
            field=models.ForeignKey(help_text='Brand this project is associated with', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='core.brand'),
        ),
    ]
