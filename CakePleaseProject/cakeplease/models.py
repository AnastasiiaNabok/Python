from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.FloatField()
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField(max_length=200)
    price = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=200)
    minimal_order = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    PAYMENT = (
        ('Cash', 'Cash'),
        ('Card', 'Card'),
    )

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    item = models.ManyToManyField('Item')
    date = models.DateTimeField('delivery date')
    delivery = models.BooleanField(default=False)
    count = models.PositiveSmallIntegerField()
    status = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=4, choices=PAYMENT)


class Review(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    review_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Login(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
