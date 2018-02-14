# Generated by Django 2.0.2 on 2018-02-14 22:39

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
                ('type', models.IntegerField(verbose_name=((0, 'Joint'), (2, 'Gate'), (3, 'Counter'), (4, 'Food'), (5, 'Retail'), (7, 'Club')))),
                ('floor', models.IntegerField(default=0)),
                ('neighbours', models.ManyToManyField(blank=True, related_name='_node_neighbours_+', to='nav.Node')),
            ],
            options={
                'db_table': 'Node',
            },
        ),
    ]
