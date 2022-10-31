import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def validate_birthday(value):
    if value < datetime.date.today():
        return value
    raise ValidationError("Geburtstag kann nicht in der Zukunft liegen. Dann lieber leer lassen :-)")


class Profile(models.Model):
    """Profile
    This model represents the profile of the user and contains additional information compared to the standard
    django user profile.
    """
    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profile"

    class Voices(models.TextChoices):
        """
        Model choices for singing voices
        """
        SOPRAN = ('S', "Sopran")
        ALT = ('A', "Alt")
        TENOR = ('T', "Tenor")
        BASS = ('B', "Bass")

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birthday = models.DateField(verbose_name="Geburtstag", blank=True, null=True, validators=[validate_birthday])
    voice = models.CharField(name="Stimme", max_length=1, blank=False, choices=Voices.choices)

    def __str__(self):
        """String representation
        Returns the string representation of this object.
        :return: the string representation of this object
        :rtype: str
        """
        return f"{self.user.first_name} {self.user.last_name} ({self.user.email})"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create user profile
    Creates a user profile.
    :param sender: The user of the profile
    :type sender: User
    :param instance: The user instance to be created
    :type instance: User
    :param created: An indicator if the profile was correctly created
    :type created: bool
    :param kwargs: The keyword arguments
    :type kwargs: Any
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save user profile
    Saves the user profile.
    :param sender: The user of the profile
    :type sender: User
    :param instance: The user instance to be saved
    :type instance: User
    :param kwargs: The keyword arguments
    :type kwargs: Any
    """
    try:
        profile = Profile.objects.get(user=instance)
        profile.save()
    except Profile.DoesNotExist:
        pass
