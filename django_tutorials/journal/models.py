from django.db import models
from datetime import timedelta, datetime


# Create your models here.


##############################
### - test stuff:
##############################
#
# class User(models.Model):
#     email = models.EmailField()
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=20)
#     first_name = models.CharField(max_length=25)
#     last_name = models.CharField(max_length=50)
#     active_flag = models.BooleanField(default=True)
#     registered_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return 'User: {}'.format(self.username)
#
#
# class Activity(models.Model):
#     activity_name = (models.CharField(max_length=200))
#     instruction = (models.TextField(max_length=1000, null=True, blank=True))
#     active_flag = (models.BooleanField(default=True))
#     is_habit = (models.BooleanField(default=False))
#
#     value_instruction = (models.CharField(max_length=50, null=True, blank=True))
#     duration_instruction = (models.CharField(max_length=50, null=True, blank=True))
#     note_instruction = (models.CharField(max_length=50, null=True, blank=True))
#
#     def __str__(self):
#         return self.activity_name
#
#
# class ActivityLog(models.Model):
#     user_id = (models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True))
#     activity_id = (models.ForeignKey(Activity, on_delete=models.CASCADE, blank=False))
#     entry_date = (models.DateTimeField(auto_now_add=True))
#     completed = (models.BooleanField(default=False))
#     note = (models.TextField(max_length=1000, null=True, blank=True))
#
#
#     def __str__(self):
#         return "User: {}, Activity:{}, Date:{}".format(User.username, Activity.activity_name, self.activity_date)
#
# class NoSugar(models.Model):
#     """ Simple schema for 1 habit.
#         MAKE SOMETHING QUICK AND DIRTY!
#     """
#     #~TODO Try to make something scalable later.
#     entry_date = (models.DateTimeField(default=datetime.utcnow(), blank=True))
#     completed = (models.BooleanField(default=False, blank=True))
#     note = (models.TextField(max_length=1000, null=True, blank=True))


######################################################################################
# -- Normalized Schema Idea ~TODO - Think of way of implementation.
######################################################################################
#
#
# class ActivityLogItem(models.Model):
#     """ Includes the activity data items to populate...
#     """
#     activity_log = (models.ForeignKey(ActivityLog, on_delete=models.CASCADE))
#     item = (models.ForeignKey(Item, on_delete=models.CASCADE))
#     numeric_value = (models.DecimalField(null=True, blank=True))
#     text_value = (models.CharField(max_length=250, null=True, blank=True))
#     boolean_value = (models.BooleanField(null=True, blank=True))
#     #duration_value = (models.DecimalField(null=True, blank=True))
#
#
# class ItemType(models.Model):
#     """ Lists the data item types to use for an activity:
#         numeric, text, boolean, duration... (other?)
#         Shows which field in the ActivityItem table to populate the data.
#     """
#     item_type_name = (models.CharField(max_length=20))
#
#     def __str__(self):
#         return self.item_type_name
#
#
# class Item(models.Model):
#     """ Lists the items to collect.
#         item_info - short info (maybe to include in the text box.
#         item_detail - detailed info.
#     EXAMPLE:
#         Main String | Decimal | Log weight in lb | Details about how to log weight
#     """
#     item_name = (models.CharField(max_length=50))
#     item_type = (models.ForeignKey(ItemType, on_delete=models.CASCADE))
#     item_info = (models.CharField(max_length=100, null=True, blank=True))
#     item_detail = (models.CharField(max_length=1000, null=True, blank=True))
#     is_lookup = (models.BooleanField(default=False))
#
#
# class ActivityItem(models.Model):
#     """ Lists items for each activity.
#         Represents the many to many rel between activity and item.
#     EXAMPLE:
#         Weight | Weight measured | True | 1
#     """
#     activity = (models.ForeignKey(Activity, on_delete=models.CASCADE))
#     item = (models.ForeignKey(Item, on_delete=models.CASCADE))
#     active_flag = (models.BooleanField(default=True))
#     item_order = (models.PositiveIntegerField(null=True))
#
#
# class ItemLookup(models.Model):
#     """ Contains lookup values of those items where is_lookup=True
#     """
#     item = (models.ForeignKey(Item, on_delete=models.CASCADE))
#     lookup_value = (models.CharField(max_length=100, default=''))
#
#
# class HabitPeriodicity(models.Model):
#     """ Lists the frequency types - weekly (7), monthly (30), daily (1)
#     """
#     periodicity_name = (models.CharField(max_lenth=20))
#     periodicity_days = (models.SmallIntegerField)
