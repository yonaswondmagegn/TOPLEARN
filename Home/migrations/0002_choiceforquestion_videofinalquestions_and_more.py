# Generated by Django 4.1.7 on 2023-03-05 10:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceForQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.TextField()),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VideoFinalQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('questiontype', models.CharField(choices=[('S', 'SHORTANSWERE'), ('C', 'CHOISE')], default='C', max_length=1)),
                ('answere', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('choices', models.ManyToManyField(blank=True, related_name='choices', to='Home.choiceforquestion')),
            ],
        ),
        migrations.AddField(
            model_name='videofiles',
            name='videofinalquestions',
            field=models.ManyToManyField(blank=True, related_name='videofinalquestion', to='Home.videofinalquestions'),
        ),
    ]