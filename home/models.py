from django.db import models

# Create your models here.
class contact(models.Model):
        
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
        

