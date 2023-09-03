from django.db import models


class Timestamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Education(Timestamped):
    institution_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()


class Job(Timestamped):
    company_name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    job_description = models.TextField()


class Project(Timestamped):
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    technologies_used = models.ManyToManyField("Technology")
    start_date = models.DateField()
    end_date = models.DateField()


class Technology(Timestamped):
    name = models.CharField(max_length=100)
    description = models.TextField()
    proficiency = models.IntegerField(
        choices=[(1, "Beginner"), (2, "Intermediate"), (3, "Advanced"), (4, "Expert")]
    )


class Course(Timestamped):
    course_name = models.CharField(max_length=200)
    provider = models.CharField(max_length=100)
    completion_date = models.DateField()
    topics_covered = models.TextField()
