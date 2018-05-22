# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models






class Teacher(models.Model):
    name = models.CharField(max_length=11, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    qq = models.CharField(max_length=11, blank=True, null=True)
    job = models.CharField(max_length=11, blank=True, null=True)
    course = models.CharField(max_length=30, blank=True, null=True)
    guide_type = models.IntegerField(blank=True, null=True)
    birth_date = models.CharField(max_length=10, blank=True, null=True)
    bank_number = models.CharField(max_length=20, blank=True, null=True)
    bank_name = models.CharField(max_length=20, blank=True, null=True)
    bank_branch = models.CharField(max_length=20, blank=True, null=True)
    bachelor_school = models.CharField(max_length=20, blank=True, null=True)
    bachelor_major = models.CharField(max_length=20, blank=True, null=True)
    grade_year = models.IntegerField(blank=True, null=True)
    professional_salary = models.IntegerField(blank=True, null=True)
    open_class_salary = models.IntegerField(blank=True, null=True)
    one_to_one_salary = models.IntegerField(blank=True, null=True)
    other_salary = models.IntegerField(blank=True, null=True)
    now_school = models.CharField(max_length=20, blank=True, null=True)
    now_major = models.CharField(max_length=20, blank=True, null=True)
    if_pass_direct = models.IntegerField(blank=True, null=True)
    english_class_score = models.IntegerField(blank=True, null=True)
    politic_class_score = models.IntegerField(blank=True, null=True)
    first_rank = models.IntegerField(blank=True, null=True)
    final_rank = models.IntegerField(blank=True, null=True)
    qq_group = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    extend = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True, auto_now=True)
    update_time = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = True
        db_table = 'teacher'
        ordering = ['-create_time', '-update_time']

    def __str__(self):
        return self.name

    @property
    def student(self):
        return self.student_set.all()



lesson_base =  dict(
    id=False,
    type=False,
    teacher_name=False,
    assistant_name=False,
    skype_count=False,
    skype_count_now=False,
    if_protocol=False,
    class_level=False
)

class Student(models.Model):
    name = models.CharField(max_length=11, blank=True, null=True)
    if_old_major = models.IntegerField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    qq = models.CharField(unique=True, max_length=11, blank=True, null=True)
    adviser = models.CharField(max_length=20, blank=True, null=True)
    due_year = models.CharField(max_length=128,blank=True, null=True)
    old_school = models.CharField(max_length=20, blank=True, null=True)
    old_major = models.CharField(max_length=20, blank=True, null=True)
    study_status = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    apply_time = models.CharField(max_length=20, blank=True, null=True)
    source = models.CharField(max_length=20, blank=True, null=True)
    background = models.CharField(max_length=11, blank=True, null=True)
    qq_group = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    extend = models.TextField(blank=True, null=True)

    teacher = models.ForeignKey(Teacher,null=True,blank=True,on_delete=models.SET_NULL)
    email_sent = models.BooleanField(default=False)
    major_sent = models.IntegerField(null=True,blank=True)
    public_sent = models.IntegerField(null=True,blank=True)
    order_style = models.IntegerField(blank=True, null=True)

    target_school = models.CharField(max_length=20, blank=True, null=True)
    # target_major = models.CharField(max_length=20, blank=True, null=True)

    create_time = models.DateTimeField(blank=True, null=True, auto_now=True)
    update_time = models.DateTimeField(blank=True, null=True, auto_now=True)


    class Meta:
        managed = True
        db_table = 'student'
        ordering = ['-create_time', '-update_time']


    @property
    def pro(self):
        if self.lesson_set.filter(type='pro').exists():
            return self.lesson_set.get(type='pro')
        else:
            return lesson_base

    @property
    def com(self):
        if self.lesson_set.filter(type='com').exists():
            return self.lesson_set.get(type='com')
        else:
            return lesson_base

    @property
    def eng(self):
        if self.lesson_set.filter(type='eng').exists():
            return self.lesson_set.get(type='eng')
        else:
            return lesson_base

    @property
    def pol(self):
        if self.lesson_set.filter(type='pol').exists():
            return self.lesson_set.get(type='pol')
        else:
            return lesson_base

    def __str__(self):
        return self.name



class Lesson(models.Model):
    student = models.ForeignKey(Student,on_delete= models.SET_NULL, blank=True, null=True)
    class_level = models.IntegerField(blank=True, null=True)
    teacher_name = models.CharField(max_length=20, blank=True, null=True)
    assistant_name = models.CharField(max_length=20, blank=True, null=True)
    skype_count = models.IntegerField(blank=True, null=True)
    skype_count_now = models.IntegerField(blank=True, null=True)
    # fee = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=128,null=True,blank=True)
    if_protocol = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'lesson'
        ordering = ['-create_time', '-update_time']

