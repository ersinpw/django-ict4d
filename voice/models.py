from django.db import models


class CallerID(models.Model):
    caller_id = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Region(models.Model):
    region = models.ForeignKey(CallerID, on_delete=models.CASCADE)
    region_text = models.CharField(max_length=200)
    regions = models.IntegerField(default=0)

class Village(models.Model):
    village = models.ForeignKey(CallerID, on_delete=models.CASCADE)
    village_text = models.CharField(max_length=200)
    villages = models.IntegerField(default=0)

class CropSize(models.Model):
    crop_size = models.ForeignKey(CallerID, on_delete=models.CASCADE)
    cropsize_text = models.CharField(max_length=200)
    cropsizes = models.IntegerField(default=0)

class LatestCrop(models.Model):
    latest_crop = models.ForeignKey(CallerID, on_delete=models.CASCADE)
    latestcrop_text = models.CharField(max_length=200)
    latestcrops = models.IntegerField(default=0)

class Language(models.Model):
    language = models.ForeignKey(CallerID, on_delete=models.CASCADE)
    language_text = models.CharField(max_length=200)
    languages = models.IntegerField(default=0)
