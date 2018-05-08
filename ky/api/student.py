from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer


from ky.models import UiStudent
from ky.api.base import Base

class Student(Base):
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
        'create_time':'create_time',
        'update_time':'update_time',
    })

    def list(self):
        return UiStudent.objects.filter(name__contains=self.request.GET.get('search', ''))

    def detail(self, pk):
        return UiStudent.objects.get(id=pk)

    def create(self):
        pass

    def update(self,pk):
        pass

    def delete(self, pk):
        pass