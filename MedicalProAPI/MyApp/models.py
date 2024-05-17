from django.db import models
from django.core.validators import RegexValidator

class User(models.Model):
    username=models.CharField(primary_key=True, max_length=4, validators=[
        RegexValidator(r'^\d{4}$', 'Track_id must be exactly 4 digits')
    ], default='default_username')
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    blood_state = models.CharField(max_length=10,blank=True, null=True)
    health_state = models.CharField(max_length=20,blank=True, null=True)
    location = models.CharField(max_length=50,blank=True, null=True)
    password = models.CharField(max_length=15, validators=[
        RegexValidator(
                regex='^(?=.*[0-9])(?=.*[a-zA-Z]).{8,}$',
                message='Password must contain at least one digit and one character, and be at least 8 characters long.',
                code='invalid_password'
            )
    ])
     
    def __str__(self):
        return self.name

class Friend(models.Model):
    friend_id=models.CharField(primary_key=True, max_length=4, validators=[
        RegexValidator(r'^\d{4}$', 'Track_id must be exactly 4 digits')
    ], default='default_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    friend_name = models.CharField(max_length=50)
    relation = models.CharField(max_length=55)
    email = models.EmailField(unique=True)
    def clean(self):
        super().clean()

        existing_friends_count = self.user.friends.count()

        if existing_friends_count < 3:
            raise ValidationError("You must add at least 3 friends.")

    def __str__(self):
        return self.friend_name

class Emergency(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emergency')
    location = models.CharField(max_length=255)
    code = models.CharField(max_length=255, choices=[
        ('Red', '221'),
        ('Green', '222'),
        ('Orange', '223'),
    ],primary_key=True)
    action = models.CharField(max_length=255)

    def __str__(self):
        return self.code


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos')
    video_url = models.URLField()
    video_name = models.CharField(max_length=255)

    def __str__(self):
        return self.video_name
    

class Coach(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coaches')
    name = models.CharField(max_length=35)
    specialization = models.CharField(max_length=25,blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Hospital(models.Model):
    hospital_id=models.CharField(primary_key=True, max_length=3, validators=[
        RegexValidator(r'^\d{3}$', 'Track_id must be exactly 3 digits')
    ], default='default_id')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    payment_id = models.CharField(max_length=255)
    password = models.CharField(max_length=10, validators=[
        RegexValidator(
                regex='^[0-9]{10}$',
                message='Password must contain exactly 10 digits.',
                code='invalid_password'
            )
    ])
    cvc = models.CharField(max_length=4)
  
    def validate_cvc(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("CVC must be a numeric value.")
        if len(value) not in [3, 4]:
            raise serializers.ValidationError("CVC must be 3 or 4 digits long.")
        return value


    def __str__(self):
        return self.cvc
    

class Tips(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tips')
    description = models.TextField(max_length=55)
    type = models.CharField(max_length=50)
    url= models.URLField(blank=True, null=True)