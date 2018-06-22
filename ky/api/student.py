from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer


from ky.models import Student,Teacher,Lesson
from ky.api.base import Base

class StudentAPI(Base):
    lesson_preparer = FieldsPreparer(fields={
        "id":'id',
        "type":'type',
        "teacher_name":'teacher_name',
        "assistant_name":'assistant_name',
        "skype_count":"skype_count",
        # "fee":"fee",
        "class_level":"class_level",
        "if_protocol":"if_protocol"
    })

    teacher_preparer = FieldsPreparer(fields={
        "id":"id",
        "name":"name"
    })

    preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
        'if_old_major': 'if_old_major',
        'sex': 'sex',
        'qq': 'qq',
        'mobile':'mobile',
        'adviser': 'adviser',

        'due_year':'due_year',
        'old_school':'old_school',
        'old_major':'old_major',
        'study_status':'study_status',
        'status':'status',
        'apply_time':'apply_time',
        'source':'source',
        'background':'background',
        'qq_group':'qq_group',
        'author':'author',
        'remark':'remark',
        'extend':'extend',
        'teacher_id':'teacher_id',
        'email_sent':'email_sent',
        'major_sent':'major_sent',
        'public_sent':'public_sent',
        'target_school':'target_school',
        'create_time':'create_time',
        'update_time':'update_time',
        'pro':SubPreparer('pro', lesson_preparer),
        'com': SubPreparer('com', lesson_preparer),
        'eng': SubPreparer('pro', lesson_preparer),
        'pol': SubPreparer('com', lesson_preparer),
    })

    def list(self):

        return Student.objects.filter(
            name__icontains=self.request.GET.get('name',''),
            due_year__icontains=self.request.GET.get('due_year',''),
            target_school__icontains=self.request.GET.get('target_school',''),
            old_major__icontains=self.request.GET.get('old_major',''),
            old_school__icontains=self.request.GET.get('old_school','')
        )

    def detail(self, pk):
        return Student.objects.get(id=pk)

    def create(self):

        student = Student()
        student.name = self.data['name'] if 'name' in self.data else ''
        student.due_year = self.data['due_year'] if 'due_year' in self.data else ''
        student.target_school = self.data['target_school'] if 'target_school' in self.data else ''
        student.old_major = self.data['old_major'] if 'old_major' in self.data else ''
        student.old_school = self.data['old_school'] if 'old_school' in self.data else ''
        if 'if_old_major' in self.data:
            student.if_old_major = self.data['if_old_major']
        if 'sex' in self.data:
            student.sex = self.data['sex']
        if 'qq' in self.data:
            student.qq = self.data['qq']
        if 'mobile' in self.data:
            student.mobile = self.data['mobile']
        if 'adviser' in self.data:
            student.adviser = self.data['adviser']

        if 'study_status' in self.data:
            student.study_status = self.data['study_status']
        if 'study_status' in self.data:
            student.study_status = self.data['study_status']
        if 'status' in self.data:
            student.status = self.data['status']
        if 'apply_time' in self.data:
            student.apply_time = self.data['apply_time']
        if 'source' in self.data:
            student.source = self.data['source']
        if 'background' in self.data:
            student.background = self.data['background']
        if 'qq_group' in self.data:
            student.qq_group = self.data['qq_group']
        if 'author' in self.data:
            student.author = self.data['author']
        if 'remark' in self.data:
            student.remark = self.data['remark']
      
        if 'extend' in self.data:
            student.extend = self.data['extend']
        if 'major_sent' in self.data:
            student.major_sent = self.data['major_sent']
        if 'email_sent' in self.data:
            student.email_sent = self.data['email_sent']
        if 'public_sent' in self.data:
            student.public_sent = self.data['public_sent']

        student.save()
        if 'pro' in self.data:
            data = self.data['pro']
            (pro,pro_bool) = Lesson.objects.get_or_create(student=student,type='pro')

            if 'teacher_name' in data:
                pro.teacher_name = data['teacher_name']

            if 'assistant_name' in data:
                pro.assistant_name = data['assistant_name']
            if 'skype_count' in data:
                pro.skype_count = data['skype_count']
            if 'class_level' in data:
                pro.class_level = data['class_level']
            if 'if_protocol' in data:
                pro.if_protocol = data['if_protocol']

            pro.save()

        if 'com' in self.data:
            data = self.data['com']
            (com,pro_bool) = Lesson.objects.get_or_create(student=student,type='com')

            if 'teacher_name' in data:
                com.teacher_name = data['teacher_name']

            if 'assistant_name' in data:
                com.assistant_name = data['assistant_name']
            if 'skype_count' in data:
                com.skype_count = data['skype_count']
            if 'class_level' in data:
                com.class_level = data['class_level']
            if 'if_protocol' in data:
                com.if_protocol = data['if_protocol']
        if 'pol' in self.data:
            data = self.data['pol']
            (pol,pro_bool) = Lesson.objects.get_or_create(student=student,type='pol')

            if 'teacher_name' in data:
                pol.teacher_name = data['teacher_name']

            if 'assistant_name' in data:
                pol.assistant_name = data['assistant_name']
            if 'skype_count' in data:
                pol.skype_count = data['skype_count']
            if 'class_level' in data:
                pol.class_level = data['class_level']
      
            if 'if_protocol' in data:
                pol.if_protocol = data['if_protocol']
            pol.save()

        if 'eng' in self.data:
            data = self.data['pro']
            (eng,pro_bool) = Lesson.objects.get_or_create(student=student,type='eng')

            if 'teacher_name' in data:
                eng.teacher_name = data['teacher_name']

            if 'assistant_name' in data:
                eng.assistant_name = data['assistant_name']
            if 'skype_count' in data:
                eng.skype_count = data['skype_count']
            if 'class_level' in data:
                eng.class_level = data['class_level']
      
            if 'if_protocol' in data:
                eng.if_protocol = data['if_protocol']

            eng.save()
        if 'teacher' in self.data:
            student.teacher = Teacher.objects.get(id=int(self.data['teacher_id']))
        student.save()

        return student

    def update(self,pk):


        student = Student.objects.get(id=pk)
        student.name = self.data['name'] if 'name' in self.data else student.name
        student.if_old_major = self.data['if_old_major'] if 'if_old_major' in self.data else student.if_old_major
        student.sex = self.data['sex'] if 'sex' in self.data else student.sex
        student.qq = self.data['qq'] if 'qq' in self.data else student.qq
        student.mobile = self.data['mobile'] if 'mobile' in self.data else student.mobile
        student.adviser = self.data['adviser'] if 'adviser' in self.data else student.adviser
        student.due_year = self.data['due_year'] if 'due_year' in self.data else student.due_year

        student.old_school = self.data['old_school'] if 'old_school' in self.data else student.old_school
        student.old_major = self.data['old_major'] if 'old_major' in self.data else student.old_major
        student.study_status = self.data['study_status'] if 'study_status' in self.data else student.study_status
        student.status = self.data['status'] if 'status' in self.data else student.status
        student.apply_time = self.data['apply_time'] if 'apply_time' in self.data else student.apply_time
        student.source = self.data['source'] if 'source' in self.data else student.source
        student.background = self.data['background'] if 'background' in self.data else student.background
        student.qq_group = self.data['qq_group'] if 'qq_group' in self.data else student.qq_group

        student.author = self.data['author'] if 'author' in self.data else student.author
        student.remark = self.data['remark'] if 'remark' in self.data else student.remark
        student.extend = self.data['extend'] if 'extend' in self.data else student.extend

        student.name = self.data['name'] if 'time' in self.data else student.name

        student.major_sent = self.data['major_sent'] if 'major_sent' in self.data else student.major_sent
        student.email_sent = self.data['email_sent'] if 'email_sent' in self.data else student.email_sent
        student.public_sent = self.data['public_sent'] if 'public_sent' in self.data else student.public_sent

        # student.target_major = self.data['target_major'] if 'target_major' in self.data else student.target_major
        student.target_school = self.data['target_school'] if 'target_school' in self.data else student.target_school



        if 'pro' in self.data:
            data = self.data['pro']
            (pro,pro_bool) = Lesson.objects.get_or_create(student=student,type='pro')

            if data['teacher_name']:
                pro.teacher_name = data['teacher_name']

            if data['assistant_name']:
                pro.assistant_name = data['assistant_name']
            if data['skype_count']:
                pro.skype_count = data['skype_count']
            if data['class_level']:
                pro.class_level = data['class_level']

            if data['if_protocol']:
                pro.if_protocol = data['if_protocol']

            pro.save()

        if 'com' in self.data:
            data = self.data['com']
            (com,pro_bool) = Lesson.objects.get_or_create(student=student,type='com')

            if data['teacher_name']:
                com.teacher_name = data['teacher_name']

            if data['assistant_name']:
                com.assistant_name = data['assistant_name']
            if data['skype_count']:
                com.skype_count = data['skype_count']
            if data['class_level']:
                com.class_level = data['class_level']


            if data['if_protocol']:
                com.if_protocol = data['if_protocol']

            com.save()

        if 'pol' in self.data:
            data = self.data['pro']
            (pol,pro_bool) = Lesson.objects.get_or_create(student=student,type='pol')

            if data['teacher_name']:
                pol.teacher_name = data['teacher_name']

            if data['assistant_name']:
                pol.assistant_name = data['assistant_name']
            if data['skype_count']:
                pol.skype_count = data['skype_count']

            if data['class_level']:
                pol.class_level = data['class_level']
            if data['if_protocol']:
                pol.if_protocol = data['if_protocol']

            pol.save()

        if 'eng' in self.data:
            data = self.data['pro']
            (eng,pro_bool) = Lesson.objects.get_or_create(student=student,type='eng')

            if data['teacher_name']:
                eng.teacher_name = data['teacher_name']

            if data['assistant_name']:
                eng.assistant_name = data['assistant_name']
            if data['skype_count']:
                eng.skype_count = data['skype_count']
            if data['class_level']:
                eng.class_level = data['class_level']

            if data['if_protocol']:
                eng.if_protocol = data['if_protocol']

            pro.save()

        student.teacher = Teacher.objects.get(id=int(self.data['teacher_id'])) if 'teacher_id' in self.data and self.data['teacher_id'] else student.teacher
        student.save()
        return student

    def delete(self, pk):
        Student.objects.get(id=pk).delete()