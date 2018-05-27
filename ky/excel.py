from django.http import HttpResponse,JsonResponse
import xlwt
import simplejson
from ky.models import Teacher,Student,Lesson

def teacher_export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="teacher-template.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet1')
    header = ['姓名', '手机号','qq','备注']
    row_num=0
    for i in range(len(header)):
        ws.write(row_num, i, header[i])
    return HttpResponse('hello teacher')

def student_export(request):
    return HttpResponse('hello student')
    pass

t_header = [
        '姓名', '手机号','qq','手机号码',
        '身份证号码','银行卡号','银行卡开户行',
        '就职岗位','本科学校','本科专业','辅导院校',
        '312具体院校','一战 OR 多战','“本专业”OR 跨专业',
        '是否在职备考','是否录取','录取方式','入学年份',
        '学习年制','学制类型','初试总分','专业课总分',
        '英语分数','政治分数','初试排名','复试分数',
        '复试排名','总排名','是否留任','生日','智囊团群','辅导工作群'
        '微信群','协议书发出','协议书回收','校区群','培训记录','备注'
        ]
   
def teacher_template(request):


    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="teacher-template.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet1')
    row_num=0
    for i in range(len(t_header)):
        print(t_header[i])
        ws.write(row_num, i, t_header[i])
    wb.save(response)
    return response


def teacher_upload(request):
    body = simplejson.loads(request.body)

    list = []
    for item in body:
        (teacher ,bool )= Teacher.objects.get_or_create(name=item['name'])

        teacher.name = item['name']
        teacher.mobile = item['mobile']
        teacher.remark = item['remark']
        teacher.qq = item['qq']
        if bool:

            item['status'] = '已创建'
        else:
            item['status'] = '已更新'
            list.append(teacher)
    return JsonResponse(dict(list=body))

def student_template(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="teacher-template.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet1')
    header = ['报班时间', '招生顾问', '报考学校', '姓名','班型','公共课','届','qq','电话','专业','本科学校','备注']
    row_num = 0
    for i in range(len(header)):
        ws.write(row_num, i, header[i])
    wb.save(response)
    return response


pro_list = [
    { "id": 1, "name": "SSVIP", "skype_count": 9999 },
    { "id": 2, "name": "SVIP", "skype_count": 32 },
    { "id": 3, "name": "VIPA", "skype_count": 24 },
    { "id": 4, "name": "VIPB", "skype_count": 16 },
    { "id": 5, "name": "VIPC", "skype_count": 8 },
    { "id": 6, "name": "高分全程", "skype_count": 0 },
    { "id": 7, "name": "培优全程", "skype_count": 0 },
  ]

pro_map=['9999','32','24','16','8','0','0']

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
        (lesson,lesson_bool) = Lesson.objects.get_or_create(student=student,type='pro')
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