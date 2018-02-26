# Generated by Django 2.0.1 on 2018-02-26 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('name', models.CharField(blank=True, max_length=50)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('type', models.IntegerField(verbose_name=((0, 'Joint'), (2, 'Gate'), (3, 'Counter'), (4, 'Food'), (5, 'Retail'), (6, 'Exit'), (7, 'Club'), (8, 'Security')))),
                ('floor', models.IntegerField(default=0)),
                ('neighbours', models.ManyToManyField(blank=True, related_name='_node_neighbours_+', to='nav.Node')),
            ],
            options={
                'db_table': 'Node',
            },
        ),
    ]
