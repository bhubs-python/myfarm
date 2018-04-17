from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db.models.signals import post_save


#member type
class MemberType(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name


# user profile manager
class UserProfileManager(BaseUserManager):
    """Helps django work with our custom user model"""

    def create_user(self, username, email, phone=None, photo=None, job_title=None, company=None, address=None, suit_floor_apt=None, city=None, state=None, zip_postal_code=None, password=None):
        """creates a new user profile objecs"""

        if not email:
            raise ValueError('User must have an email address!')

        if not username:
            raise ValueError('User must have an username!')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, phone=phone, photo=photo, job_title=job_title, company=company, address=address, suit_floor_apt=suit_floor_apt, city=city, state=state, zip_postal_code=zip_postal_code)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, username, email, password):
        """creates and saves a new super user with given details"""

        user = self.create_user(username=username, email=email, password=password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user



# user profile model
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile inside our system"""

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, null=True, blank=True)

    photo = models.ImageField(upload_to='profile/picture/', default='profile/no-img.jpg', null=True, blank=True)

    job_title = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=1000, null=True, blank=True)
    suit_floor_apt = models.CharField(max_length=255, null=True, blank=True)

    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_postal_code = models.CharField(max_length=255, null=True, blank=True)

    join_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    investor = models.BooleanField(default=False)
    farmer = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    class Meta:
        ordering = ('-join_date', )


    def get_full_name(self):
        """Used to get a users full name."""

        return self.username

    def get_short_name(self):
        """Used to get a users short name."""

        return self.username

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""

        return self.username



#virtual credit
class Credit(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    credit = models.FloatField(default=0, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


def create_Credit(sender, **kwargs):
    if kwargs['created']:
        aweberaccount = Credit.objects.create(user=kwargs['instance'])

post_save.connect(create_Credit, sender=UserProfile)




#virtual credit recharge request
class CreditRecharge(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='wallet_user')
    method = models.CharField(max_length=50, null=True, blank=True)
    sender_phone_number = models.CharField(max_length=20, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    credit = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=50, default='pending', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    authorized_by = models.ForeignKey(UserProfile, on_delete=None, null=True, blank=True, related_name='authorized_by')


    def __str__(self):
        return str(self.user.username) + ":" + str(self.transaction_id)



#virtual transfer
class CreditTransfer(models.Model):
    payer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='payer')
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='receiver')
    credit = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.payer.username) + ":" + str(self.receiver.username)
    


#payment details
#its for verifying for staff to see the payment history of user if anything wrong
class PaymentNote(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=None, null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)

    #status only be debit or credit
    status = models.CharField(max_length=20, null=True, blank=True)
    about_payment = models.CharField(max_length=255, null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.user.username)

