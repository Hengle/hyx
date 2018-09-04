from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer


from ky.models import Teacher
from ky.api.base import Base



class TeacherAPI(Base):

    stu_preparer = FieldsPreparer(fields={
        "id":'id',
        "name":"name"
    })

    preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
        'sex': 'sex',
        'mobile': 'mobile',
        'qq': 'qq',
        'student':CollectionSubPreparer("student",stu_preparer),

        'remark':'remark',
        'is_xiaoqugroup': 'is_xiaoqugroup',
        'train_records':'train_records',
        'is_xieyi_back':'is_xieyi_back',
        'is_xieyi_send':'is_xieyi_send',
        "is_weixunqun":'is_weixunqun',
        'birth': 'birth',
        'is_stay': 'is_stay',
        'final_rank': 'final_rank',
        'second_rank':'second_rank',
        'second_score': 'second_score',
        "first_rank": 'first_rank',
        'politic_class_score':'politic_class_score',
        'english_class_score':'english_class_score',
        'pro_class_score':'pro_class_score',
        'first_total':'first_total',
        'study_type':'study_type',
        'study_year':'study_year',
        'join_year':'join_year',
        'passed_type':'passed_type',
        'is_passed':'is_passed',
        'is_wokring':'is_wokring',
        'is_cross_major':'is_cross_major',
        'is_war_more':'is_war_more',
        'school_312':'school_312',
        'fudao_school':'fudao_school',
        'bachelor_major':'bachelor_major',
        'bachelor_school':'bachelor_school',
        'job':'job',
        'bank_name':'bank_name',
        'bank_number':'bank_number',
        'idcard':'idcard',
        'is_zhinanqun':'is_zhinanqun',
        'is_fudaogongzuoqun':'is_fudaogongzuoqun'


    })

    def list(self):

        return Teacher.objects.filter(
            name__icontains=self.request.GET.get('name',''),
            job__icontains=self.request.GET.get('job',''),
            is_stay__icontains=self.request.GET.get('is_stay',''),
            fudao_school__icontains=self.request.GET.get('fudao_school',''),

            is_cross_major__icontains=self.request.GET.get('is_cross_major',''),
            is_war_more__icontains=self.request.GET.get('is_war_more',''),
            is_wokring__icontains=self.request.GET.get('is_working',''),
            study_type__icontains=self.request.GET.get('study_type','')
        ).order_by('id')

    def detail(self, pk):
        return Teacher.objects.get(id=pk)

    def create(self):
        data = self.data
        t = Teacher()


        t.name = data['name'] if 'name' in data else ''
        t.sex = data['sex'] if 'sex' in data else ''
        t.qq = data['qq'] if 'qq' in data else ''
        t.mobile = data['mobile'] if 'mobile' in data else ''
        t.idcard = data['idcard'] if 'idcard' in data else ''
        t.bank_number = data['bank_number'] if 'bank_number' in data else ''
        t.job = data['job'] if 'job' in data else ''
        t.bachelor_school = data['bachelor_school'] if 'bachelor_school' in data else ''
        t.bachelor_major = data['bachelor_major'] if 'bachelor_major' in data else ''
        t.fudao_school = data['fudao_school'] if 'fudao_school' in data else ''
        t.school_312 = data['school_312'] if 'school_312' in data else ''
        t.is_war_more = data['is_war_more'] if 'is_war_more' in data else ''
        t.is_cross_major = data['is_cross_major'] if 'is_cross_major' in data else ''

        t.is_wokring = data['is_wokring'] if 'is_wokring' in data else ''
        t.is_passed = data['is_passed'] if 'is_passed' in data else ''
        t.passed_type = data['passed_type'] if 'passed_type' in data else ''
        t.join_year = data['join_year'] if 'join_year' in data else ''
        t.study_year = data['study_year'] if 'study_year' in data else ''
        t.study_type = data['study_type'] if 'study_type' in data else ''
        t.first_total = data['first_total'] if 'first_total' in data else ''
        t.pro_class_score = data['pro_class_score'] if 'pro_class_score' in data else ''
        t.english_class_score = data['english_class_score'] if 'english_class_score' in data else ''
        t.politic_class_score = data['politic_class_score'] if 'politic_class_score' in data else ''
        t.first_rank = data['first_rank'] if 'first_rank' in data else ''
        t.second_score = data['second_score'] if 'second_score' in data else ''
        t.second_rank = data['second_rank'] if 'second_rank' in data else ''
        t.final_rank = data['final_rank'] if 'final_rank' in data else ''
        t.is_stay = data['is_stay'] if 'is_stay' in data else ''
        t.birth = data['birth'] if 'birth' in data else ''
        t.is_zhinanqun = data['is_zhinanqun'] if 'is_zhinanqun' in data else ''
        t.is_fudaogongzuoqun = data['is_fudaogongzuoqun'] if 'is_fudaogongzuoqun' in data else ''
        t.is_weixunqun = data['is_weixunqun'] if 'is_weixunqun' in data else ''
        t.is_xieyi_send = data['is_xieyi_send'] if 'is_xieyi_send' in data else ''
        t.is_xieyi_back = data['is_xieyi_back'] if 'is_xieyi_back' in data else ''
        t.is_xiaoqugroup = data['is_xiaoqugroup'] if 'is_xiaoqugroup' in data else ''
        t.train_records = data['train_records'] if 'train_records' in data else ''
        t.remark = data['remark'] if 'remark' in data else ''
        t.save()
        return t

    def update(self,pk):
        t = Teacher.objects.get(id=int(pk))
        data = self.data
        t.name = data['name'] if 'name' in data else ''
        t.sex = data['sex'] if 'sex' in data else ''
        t.qq = data['qq'] if 'qq' in data else ''
        t.mobile = data['mobile'] if 'mobile' in data else ''
        t.idcard = data['idcard'] if 'idcard' in data else ''
        t.bank_number = data['bank_number'] if 'bank_number' in data else ''
        t.job = data['job'] if 'job' in data else ''
        t.bachelor_school = data['bachelor_school'] if 'bachelor_school' in data else ''
        t.bachelor_major = data['bachelor_major'] if 'bachelor_major' in data else ''
        t.fudao_school = data['fudao_school'] if 'fudao_school' in data else ''
        t.school_312 = data['school_312'] if 'school_312' in data else ''
        t.is_war_more = data['is_war_more'] if 'is_war_more' in data else ''
        t.is_cross_major = data['is_cross_major'] if 'is_cross_major' in data else ''

        t.is_wokring = data['is_wokring'] if 'is_wokring' in data else ''
        t.is_passed = data['is_passed'] if 'is_passed' in data else ''
        t.passed_type = data['passed_type'] if 'passed_type' in data else ''
        t.join_year = data['join_year'] if 'join_year' in data else ''
        t.study_year = data['study_year'] if 'study_year' in data else ''
        t.study_type = data['study_type'] if 'study_type' in data else ''
        t.first_total = data['first_total'] if 'first_total' in data else ''
        t.pro_class_score = data['pro_class_score'] if 'pro_class_score' in data else ''
        t.english_class_score = data['english_class_score'] if 'english_class_score' in data else ''
        t.politic_class_score = data['politic_class_score'] if 'politic_class_score' in data else ''
        t.first_rank = data['first_rank'] if 'first_rank' in data else ''
        t.second_score = data['second_score'] if 'second_score' in data else ''
        t.second_rank = data['second_rank'] if 'second_rank' in data else ''
        t.final_rank = data['final_rank'] if 'final_rank' in data else ''
        t.is_stay = data['is_stay'] if 'is_stay' in data else ''
        t.birth = data['birth'] if 'birth' in data else ''
        t.is_zhinanqun = data['is_zhinanqun'] if 'is_zhinanqun' in data else ''
        t.is_fudaogongzuoqun = data['is_fudaogongzuoqun'] if 'is_fudaogongzuoqun' in data else ''
        t.is_weixunqun = data['is_weixunqun'] if 'is_weixunqun' in data else ''
        t.is_xieyi_send = data['is_xieyi_send'] if 'is_xieyi_send' in data else ''
        t.is_xieyi_back = data['is_xieyi_back'] if 'is_xieyi_back' in data else ''
        t.is_xiaoqugroup = data['is_xiaoqugroup'] if 'is_xiaoqugroup' in data else ''
        t.train_records = data['train_records'] if 'train_records' in data else ''
        t.remark = data['remark'] if 'remark' in data else ''
        t.save()
        return t


    def delete(self, pk):
        Teacher.objects.get(id=pk).delete()