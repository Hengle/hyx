from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer


from ky.models import UiTeacher
from ky.api.base import Base

class Teacher(Base):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
        'sex': 'sex',
        'mobile': 'mobile',
        'qq': 'qq',
        'job': 'job',
        'course':'course',
        'guide_type':'guide_type',
        'birth_date':'birth_date',
        'bank_number':'bank_number',
        'bank_name':'bank_name',
        'bank_branch':'bank_branch',
        'bachelor_school':'bachelor_school',
        'bachelor_major':'bachelor_major',
        'grade_year':'grade_year',
        'professional_salary':'professional_salary',
        'open_class_salary':'open_class_salary',
        'one_to_one_salary':'one_to_one_salary',
        'other_salary':'other_salary',
        'now_school':'now_school',
        'now_major':'now_major',
        'if_pass_direct':'if_pass_direct',
        'english_class_score':'english_class_score',
        'politic_class_score':'politic_class_score',
        'first_rank':'first_rank',
        'final_rank':'final_rank',
        'qq_group':'qq_group',
        'remark':'remark',
        'extend':'extend',
        'create_time':'create_time',
        'update_time':'update_time'
    })

    def list(self):
        return UiTeacher.objects.filter(name__contains=self.request.GET.get('search', ''))

    def detail(self, pk):
        return UiTeacher.objects.get(id=pk)

    def create(self):
        pass

    def update(self,pk):
        pass

    def delete(self, pk):
        pass