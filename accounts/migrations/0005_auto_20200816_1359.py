# Generated by Django 2.2.4 on 2020-08-16 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200816_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='request',
            name='Status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Status'),
        ),
    ]