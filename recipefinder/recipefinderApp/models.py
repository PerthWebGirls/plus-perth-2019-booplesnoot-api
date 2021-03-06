from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # date_of_birth = models.DateField("Date of birth", auto_now=False, auto_now_add=False)
    nick_name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to="profile/", null=True)
    metric = models.BooleanField(default=True)
    cooking_time = models.ManyToManyField("Cooktime")
    diet = models.ManyToManyField("Diet")
    cuisine = models.ManyToManyField("Cuisine")

    class Meta:
        ordering = ("user",)

    def __str__(self):
        return str(self.user).capitalize()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# -------------------------------- #


# class Preferences(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     metric = models.BooleanField(default=True)
#     cooking_time = models.ManyToManyField("Cooktime")
#     diet = models.ManyToManyField("Diet")
#     cuisine = models.ManyToManyField("Cuisine")

#     class Meta:
#         ordering = ("user",)

#     def __str__(self):
#         return str(self.user).capitalize()


# -------------------------------- #


class Cooktime(models.Model):
    cook_times = models.CharField(max_length=50)

    class Meta:
        ordering = ("cook_times",)

    def __str__(self):
        return str(self.cook_times).capitalize()


# -------------------------------- #


class Diet(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return str(self.name).capitalize()


# -------------------------------- #


class DietRequirement(models.Model):
    user = models.ForeignKey(User, related_name="diet_requirements", on_delete=models.CASCADE)
    diet = models.ForeignKey(Diet, related_name="users", on_delete=models.CASCADE)

    class Meta:
        ordering = ("user",)

    def __str__(self):
        return str(self.user).capitalize()


# -------------------------------- #


class Recipe(models.Model):
    # id = models.AutoField(primary_key=True)  Ben says delete this because this is there by default
    title = models.CharField(max_length=200)
    units = models.CharField(max_length=200)
    image = models.ImageField(upload_to="recipe")
    ingredients = models.ManyToManyField("Ingredient")
    servings = models.CharField(max_length=10)
    time = models.IntegerField()
    instructions = models.TextField()
    dietary_requirement = models.CharField(max_length=200)
    cuisine = models.ManyToManyField("Cuisine")
    # likes = models.ManyToManyField('Likes')
    comments = models.ManyToManyField("Comments")

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return str(self.title).capitalize()


# --------------------- #


class Ingredient(models.Model):
    title = models.CharField(max_length=50)
    ingredient_id = models.IntegerField()

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return str(self.title).capitalize()


# --------------------- #


class Cuisine(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return str(self.name).capitalize()


# --------------------- #


class Comments(models.Model):
    comment = models.CharField(max_length=200)

    class Meta:
        ordering = ("comment",)

    def __str__(self):
        return str(self.comment).capitalize()


# --------------------- #

# class Likes(models.Model):
#     # user = models.ForeignKey(User)
#     recipe = models.ForeignKey(Recipe)
#     timestamp = models.DateTimeField()

#     def __str__(self):
#         return str(self.recipe).capitalize()

