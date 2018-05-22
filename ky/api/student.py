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
        'create_time':'create_time',
        'update_time':'update_time',
        'pro':SubPreparer('pro', lesson_preparer),
        'com': SubPreparer('com', lesson_preparer),
        'eng': SubPreparer('pro', lesson_preparer),
        'pol': SubPreparer('com', lesson_preparer),
    })

    def list(self):

        return Student.objects.filter(name__icontains=self.request.GET['search'])

    def detail(self, pk):
        return Student.objects.get(id=pk)

    def create(self):
        pass

    def update(self,pk):


        student = Student.objects.get(id=pk)
        student.name = self.data['name'] if 'time' in self.data else student.name
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
            if data['fee']:
                pro.fee = data['fee']
            if 'skype_count_now' in data and data['skype_count_now']:
                pro.skype_count_now = data['skype_count_now']
            if data['if_protocol']:
                pro.if_protocol = data['if_protocol']

            pro.save()

        student.teacher = Teacher.objects.get(id=int(self.data['teacher_id'])) if 'teacher_id' in self.data and self.data['teacher_id'] else student.teacher
        student.save()
        return student

    def delete(self, pk):
        pass