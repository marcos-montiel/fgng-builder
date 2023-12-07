from django.db import models

# Create your models here.


class Strenght(models.Model):
    score = models.PositiveSmallIntegerField()
    exceptional = models.PositiveSmallIntegerField(blank=True, null=True)
    melee_attack = models.SmallIntegerField()
    damage = models.SmallIntegerField()
    non_encum = models.PositiveSmallIntegerField()
    max_weight = models.PositiveSmallIntegerField()
    force_doors = models.PositiveSmallIntegerField()
    force_locked = models.PositiveSmallIntegerField(blank=True, null=True)
    bend_bars = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = [['score', 'exceptional']]


    def __str__(self):
        if self.exceptional == 1:
            return "score " + str(self.score) + "/01-50"
        elif self.exceptional == 2:
            return "score " + str(self.score) + "/51-75"
        elif self.exceptional == 3:
            return "score " + str(self.score) + "/76-90"
        elif self.exceptional == 4:
            return "score " + str(self.score) + "/91-99"
        elif self.exceptional == 5:
            return "score " + str(self.score) + "/00"
        else:
            return "score " + str(self.score)
