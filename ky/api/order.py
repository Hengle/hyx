from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer


from ky.models import OiOrder
from ky.api.base import Base

class Order(Base):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        # 'student_id_fk':'student_id_fk',
        'student_name':'student_id_fk.name',
        'order_style':'order_style',
        'target_school':'target_school',
        'target_major':'target_major',
        'create_time':'create_time',
        'update_time':'update_time'
    })

    def list(self):
        return OiOrder.objects.all()

    def detail(self, pk):
        return OiOrder.objects.get(id=pk)

    def create(self):
        pass

    def update(self,pk):
        pass

    def delete(self, pk):
        pass