from django.db import models

# Create your models here.
class Advertisement(models.Model): 
    title=models.CharField(verbose_name='Заголовок', max_length=128)
    description=models.TextField('Описание')
    price=models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction=models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}, {self.description}, {self.price}, {self.auction}, {self.created_at}, {self.updated_at}'

    class Meta():
        db_table='advertisements'