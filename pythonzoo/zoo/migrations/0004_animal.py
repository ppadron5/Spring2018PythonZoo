# Generated by Django 2.0.4 on 2018-05-01 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0003_auto_20180430_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter an Exhibit Name)', max_length=200)),
                ('imageFileName', models.CharField(help_text='Enter Image', max_length=200, null=True)),
                ('soundFileName', models.CharField(blank=True, help_text='Enter Sound File', max_length=200, null=True)),
                ('habitatDescription', models.TextField(help_text='Enter Habitat Description', max_length=1000)),
                ('exhibit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zoo.Exhibit')),
            ],
        ),
    ]