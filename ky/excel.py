from django.http import HttpResponse, JsonResponse
import xlwt
import simplejson
from ky.models import Teacher, Student, Lesson


t_header = [
    '姓名', '性别', 'qq', '手机号码',
    '身份证号码', '银行卡号', '银行卡开户行',
    '就职岗位', '本科学校', '本科专业', '辅导院校',
    '312具体院校', '一战 OR 多战', '“本专业”OR 跨专业',
    '是否在职备考', '是否录取', '录取方式', '入学年份',
    '学习年制', '学制类型', '初试总分', '专业课总分',
    '英语分数', '政治分数', '初试排名', '复试分数',
    '复试排名', '总排名', '是否留任', '生日', '智囊团群', '辅导工作群',
                                         '微信群', '协议书发出', '协议书回收', '校区群', '培训记录', '备注'
]

class_level = [
    { "id": 1, "name": "SSVIP", "skype_count": 9999 },
    { "id": 2, "name": "SVIP", "skype_count": 32 },
    { "id": 3, "name": "VIPA", "skype_count": 24 },
    { "id": 4, "name": "VIPB", "skype_count": 16 },
    { "id": 5, "name": "VIPC", "skype_count": 8 },
    { "id": 6, "name": "高分全程", "skype_count": 0 },
    { "id": 7, "name": "培优全程", "skype_count": 0 },
  ]

def get_class_name_by_id(id):
    for item in class_level:
        if item['id'] == id:
            return item['name']
    return '空'

def teacher_export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="teacher-template.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet1')

    row_num = 0
    for i in range(len(t_header)):
        ws.write(row_num, i, t_header[i])

    teacher = Teacher.objects.all()

    for t in teacher:
        row_num = row_num + 1
        ws.write(row_num, 0, t.name)
        ws.write(row_num, 1, t.sex)
        ws.write(row_num, 2, t.qq)
        ws.write(row_num, 3, t.mobile)
        ws.write(row_num, 4, t.idcard)
        ws.write(row_num, 5, t.bank_number)
        ws.write(row_num, 7, t.job)
        ws.write(row_num, 8, t.bachelor_school)
        ws.write(row_num, 9, t.bachelor_major)

        ws.write(row_num, 10, t.fudao_school)
        ws.write(row_num, 11, t.school_312)
        ws.write(row_num, 12, t.is_war_more)
        ws.write(row_num, 13, t.is_cross_major)
        ws.write(row_num, 14, t.is_wokring)
        ws.write(row_num, 15, t.is_passed)
        ws.write(row_num, 16, t.passed_type)
        ws.write(row_num, 17, t.join_year)
        ws.write(row_num, 18, t.study_year)
        ws.write(row_num, 19, t.study_type)
        ws.write(row_num, 20, t.first_total)
        ws.write(row_num, 21, t.pro_class_score)
        ws.write(row_num, 22, t.english_class_score)
        ws.write(row_num, 23, t.politic_class_score)
        ws.write(row_num, 24, t.first_rank)
        ws.write(row_num, 25, t.second_score)
        ws.write(row_num, 26, t.second_rank)
        ws.write(row_num, 27, t.final_rank)
        ws.write(row_num, 28, t.is_stay)
        ws.write(row_num, 29, t.birth)
        ws.write(row_num, 30, t.is_zhinanqun)
        ws.write(row_num, 31, t.is_fudaogongzuoqun)
        ws.write(row_num, 32, t.is_weixunqun)
        ws.write(row_num, 33, t.is_xieyi_send)
        ws.write(row_num, 34, t.is_xieyi_back)
        ws.write(row_num, 35, t.is_xiaoqugroup)
        ws.write(row_num, 36, t.train_records)
        ws.write(row_num, 37, t.remark)
    wb.save(response)
    return response

s_header = ['报班时间', '招生顾问', '报考学校', '姓名', '班型', '公共课', '届', 'qq', '电话', '专业', '本科学校', '备注']

def student_export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="teacher-template.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet1')

    row_num = 0
    for i in range(len(s_header)):
        ws.write(row_num, i, s_header[i])

    student = Student.objects.all()
    for t in student:
        row_num = row_num + 1

        ws.write(row_num, 0, t.apply_time)
        ws.write(row_num, 1, t.adviser)
        ws.write(row_num, 2, t.target_school)
        ws.write(row_num, 3, t.name)

        if t.pro.class_level:
            ws.write(row_num,4,get_class_name_by_id(t.pro.class_level))
        ws.write(row_num, 5, t.due_year)
        ws.write(row_num, 6, t.qq)
        ws.write(row_num, 7, t.mobile)
        ws.write(row_num, 8, t.old_major)
        ws.write(row_num, 9, t.old_school)

        ws.write(row_num, 10, t.old_school)
        ws.write(row_num, 11, t.remark)

    wb.save(response)
    return response



def teacher_template(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="teacher-template.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet1')
    row_num = 0
    for i in range(len(t_header)):
        print(t_header[i])
        ws.write(row_num, i, t_header[i])
    wb.save(response)
    return response


def teacher_upload(request):
    body = simplejson.loads(request.body)

    list = []

    for key in body:
        print(key, ' : ', body[key])

    (t, teacher_bool) = Teacher.objects.get_or_create(mobile=body['mobile'])

    t.sex = body['性别'] if '性别' in body else ''
    t.qq= body['QQ'] if 'QQ' in body else ''
    t.mobile=body['手机号码'] if '手机号码' in body else ''
    t.idcard=body['身份证号码'] if '身份证号码' in body else ''
    t.bank_number=body['银行卡号'] if '银行卡号' in body else ''
    t.job=body['就职岗位'] if '就职岗位' in body else ''
    t.bachelor_school=body['本科学校'] if '本科学校' in body else ''
    t.bachelor_major=body["本科专业"] if '本科专业' in body else ''
    t.fudao_school=body['辅导院校'] if '辅导院校' in body else ''
    t.school_312=body['312具体院校'] if '312具体院校' in body else ''
    t.is_war_more=body['一战 OR 多战'] if '一战 OR 多战' in body else ''
    t.is_cross_major=body['“本专业”OR 跨专业'] if '“本专业”OR 跨专业' in body else ''
    t.is_wokring=body['是否在职备考'] if '是否在职备考' in body else ''
    t.is_passed=body['是否录取'] if '是否录取' in body else ''
    t.passed_type=body['录取方式'] if '录取方式' in body else ''
    t.join_year=body['入学年份'] if '入学年份' in body else ''
    t.study_year=body['学习年制'] if '学习年制' in body else ''
    t.study_type=body['学制类型'] if '学制类型' in body else ''
    t.first_total=body['初试总分'] if '初试总分' in body else ''
    t.pro_class_score=body['专业课总分'] if '专业课总分' in body else ''
    t.english_class_score=body['英语分数'] if '英语分数' in body else ''
    t.politic_class_score=body['政治分数'] if '政治分数' in body else ''
    t.first_rank=body['初试排名'] if '初试排名' in body else ''
    t.second_score=body['复试分数'] if '复试分数' in body else ''
    t.second_rank=body['复试排名'] if '复试排名' in body else ''
    t.final_rank=body['总排名'] if '总排名' in body else ''
    t.is_stay=body['是否留任'] if '是否留任' in body else ''
    t.birth=body['生日'] if '性别' in body else ''
    t.is_zhinanqun=body['智囊团群'] if '智囊团群' in body else ''
    t.is_fudaogongzuoqun=body['辅导工作群'] if '辅导工作群' in body else ''
    t.is_weixunqun=body['微信群'] if '微信群' in body else ''
    t.is_xieyi_send=body['协议书发出'] if '协议书发出' in body else ''
    t.is_xieyi_back=body['协议书回收'] if '协议书回收' in body else ''
    t.is_xiaoqugroup=body['校区群'] if '校区群' in body else ''
    t.train_records=body['培训记录'] if '培训记录' in body else ''
    t.remark = body['备注'] if '备注' in body else ''

    t.save()

    return JsonResponse(dict(err=False))









def student_template(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="teacher-template.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet1')

    row_num = 0
    for i in range(len(s_header)):
        ws.write(row_num, i, s_header[i])
    wb.save(response)
    return response


pro_list = [
    {"id": 1, "name": "SSVIP", "skype_count": 9999},
    {"id": 2, "name": "SVIP", "skype_count": 32},
    {"id": 3, "name": "VIPA", "skype_count": 24},
    {"id": 4, "name": "VIPB", "skype_count": 16},
    {"id": 5, "name": "VIPC", "skype_count": 8},
    {"id": 6, "name": "高分全程", "skype_count": 0},
    {"id": 7, "name": "培优全程", "skype_count": 0},
]

pro_map = ['9999', '32', '24', '16', '8', '0', '0']


def get_pro_id(name):
    for i in range(len(pro_list)):
        if pro_list[i]['name'] == name:
            return pro_list[i]['id']
    return 0


def student_upload(request):

    item = simplejson.loads(request.body)

    (student, student_bool) = Student.objects.get_or_create(name=item['name'])
    if student_bool:
        item['status'] = '创建学生-'
    else:
        item['status'] = '更新学生-'

    if 'apply_time' in item:
        student.apply_time = item['apply_time']

    if 'adviser' in item:
        student.adviser = item['adviser']

    if 'pro_class_level' in item:
        (lesson, lesson_bool) = Lesson.objects.get_or_create(student=student, type='pro')
        lesson.class_level = get_pro_id(item['pro_class_level'])
        lesson.skype_count = pro_map[lesson.class_level]
        lesson.type = 'pro'
        if lesson_bool:
            item['status'] = item['status'] + '创建班型'
        else:
            item['status'] = item['status'] + '更新班型'

        lesson.save()

    # public_class

    if 'due_year' in item:
        student.due_year = item['due_year']
    if 'qq' in item:
        student.qq = item['qq']
    if 'mobile' in item:
        student.mobile = item['mobile']
    if 'old_major' in item:
        student.old_major = item['old_major']
    if 'old_school' in item:
        student.old_school = item['old_school']
    if 'target_school' in item:
        student.target_school = item['target_school']
    if 'target_major' in item:
        student.target_major = item['target_major']
    if 'remark' in item:
        student.remark = item['remark']
        if 'public_class' in item:
            student.remark = student.remark + '公开课:' + item['public_class']
    student.save()

    return JsonResponse(item)
