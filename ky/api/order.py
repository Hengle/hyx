from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer


from ky.models import OiOrder,UiTeacher,UiStudent
from ky.api.base import Base

class Order(Base):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'student_name':'student_id_fk.name',
        'order_style':'order_style',
        'target_school':'target_school',
        'target_major':'target_major',
        'create_time':'create_time',
        'update_time':'update_time'
    })

    def list(self):
        return OiOrder.objects.all()


    # 在order->sutdent 外建 这里id 逻辑上是学生id
    def detail(self, pk):
        student = UiStudent.objects.get(id=pk)
        return OiOrder.objects.get(student=student)

    def create(self):
        pass

    def update(self,pk):
        pass

    def delete(self, pk):
        pass