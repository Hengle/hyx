let schoolMap = [[
    "南师专硕",
    "西南专硕",
    "央财专硕",
    "东师专硕",
    "复旦专硕",
    "河大专硕",
    "湖师学硕",
    "湖师专硕",
    "华东专硕",
    "华南专硕",
    "华中学硕",
    "华中专硕",
    "南开专硕",
    "南师学硕",
    "上师专硕",
    "首师专硕",
    "南师专硕",
    "苏大学硕",
    "苏大专硕",
    "西南学硕",
    "中山专硕",
    "中山学硕",
    "统考",
    "陕师专硕",
    "川大专硕",
    "东南专硕",
    "广大专硕",
    "浙师专硕"
  ], [
    "南京师范大学专硕",
    "西南大学专硕",
    "中央财经大学专硕",
    "东北师范大学专硕",
    "复旦大学专硕",
    "河南大学专硕",
    "湖南师范大学学硕",
    "湖南师范大学专硕",
    "华东师范大学专硕",
    "华南师范大学专硕",
    "华中师范大学学硕",
    "华中师范大学专硕",
    "南开大学专硕",
    "南京师范大学学硕",
    "上海师范大学专硕",
    "首都师范大学专硕",
    "南京师范大学专硕",
    "苏州大学学硕",
    "苏州大学专硕",
    "西南大学学硕",
    "中山大学专硕",
    "中山大学学硕",
    "312统考",
    "陕西师范大学专硕",
    "四川大学专硕",
    "东南大学专硕",
    "广州大学专硕",
    "浙江师范大学专硕"
  ]
]
const dict = {
  "schoolMap":schoolMap,
  "targetSchool": {
    1: [
      "湖南师范大学专硕",
      "湖南师范大学学硕",
      "南京师范大学专硕",
      "南京师范大学学硕",
      "华中师范大学专硕",
      "华中师范大学学硕",
      "苏州大学专硕",
      "苏州大学学硕",
      "西南大学专硕",
      "西南大学学硕",
      "中山大学专硕",
      "中山大学学硕",
      "华东师范大学专硕",
      "华南师范大学专硕",
      "复旦大学专硕",
      "首都师范大学专硕",
      "上海师范大学专硕",
      "中央财经大学专硕",
      "河南大学专硕",
      "南开大学专硕",
      "东北师范大学专硕",
    ],
    2: [
      "天津大学学硕",
      "山西大学学硕",
      "山西医科大学学硕",
      "山西师范大学学硕",
      "内蒙古师范大学学硕",
      "中国医科大学学硕",
      "大连医科大学学硕",
      "辽宁师范大学学硕",
      "复旦大学学硕",
      "上海交通大学学硕",
      "华东师范大学学硕",
      "上海师范大学学硕",
      "上海体育学院学硕",
      "浙江大学学硕",
      "浙江理工大学学硕",
      "浙江师范大学学硕",
      "杭州师范大学学硕",
      "宁波大学学硕",
      "安徽医科大学学硕",
      "安徽师范大学学硕",
      "厦门大学学硕",
      "南昌大学学硕",
      "江西师范大学学硕",
      "济南大学学硕",
      "山东中医药大学学硕",
      "山东师范大学学硕",
      "聊城大学学硕",
      "郑州大学学硕",
      "新乡医学院学硕",
      "武汉大学学硕",
      "华中科技大学学硕",
      "中国地质大学学硕",
      "湖北大学学硕",
      "中南大学学硕",
      "暨南大学学硕",
      "华南师范大学学硕",
      "深圳大学学硕",
      "南方医科大学学硕",
      "重庆大学学硕",
      "四川大学学硕",
      "云南师范大学学硕",
      "西北大学学硕",
      "陕西师范大学学硕",
      "空军军医大学学硕",
      "西北师范大学学硕",
      "青海师范大学学硕",
      "宁夏大学学硕",
      "新疆师范大学学硕",
    ]
  },
  "ifOldMajor": [
    { "id": 1, "name": "本专业" },
    { "id": 2, "name": "跨专业" },
  ],
  "background": [
    { "id": 1, "name": "应届生" },
    { "id": 2, "name": "在职" },
    { "id": 3, "name": "二战" },
    { "id": 0, "name": "其他" },
  ],
  "qqGroup": [
    { "id": 1, "name": "总群" },
    { "id": 2, "name": "校区群" },
    { "id": 3, "name": "Both" },
  ],
  "source": [
    { "id": 1, "name": "新学员" },
    { "id": 2, "name": "老学员" },
    { "id": 3, "name": "重修学员" },
    { "id": 4, "name": "延修学员" },
    { "id": 5, "name": "转班学员" },
    { "id": 10, "name": "其他" },
  ],
  "studyStatus": [
    { "id": 1000, "name": "正常" },
    { "id": 1001, "name": "延修" },
    { "id": 2000, "name": "结业" },
    { "id": 3000, "name": "退班" },
    { "id": 3001, "name": "转出" },
  ],
  "orderStylesObj": [
    { "id": 1, "name": "自命题考试" },
    { "id": 2, "name": "312统考" },
  ],
  "classLevelProfessional": [
    { "id": 1, "name": "SSVIP", "skype_count": 9999 },
    { "id": 2, "name": "SVIP", "skype_count": 32 },
    { "id": 3, "name": "VIPA", "skype_count": 24 },
    { "id": 4, "name": "VIPB", "skype_count": 16 },
    { "id": 5, "name": "VIPC", "skype_count": 8 },
    { "id": 6, "name": "高分全程", "skype_count": 0 },
    { "id": 7, "name": "培优全程", "skype_count": 0 },
    { "id": 8, "name": "全程", "skype_count": 0 },
    {"id": 9, "name": "错误班型", "skype_count": 0},

     {"id": 10, "name": "超车班", "skype_count": 0},
    {"id": 11, "name": "超车三科", "skype_count": 0},
    {"id": 12, "name": "爱心助考", "skype_count": 0},
  ],
  "classLevelCommonEnglish": [
    { "id": 0, "name": "无", "skype_count": 0 },
    { "id": 1, "name": "英语协议班", "skype_count": 0 },
    { "id": 2, "name": "英语全程班", "skype_count": 6 },
  ],
  "classLevelCommonPolitic": [
    { "id": 0, "name": "无", "skype_count": 0 },
    { "id": 1, "name": "政治协议班", "skype_count": 0 },
    { "id": 2, "name": "政治全程班", "skype_count": 4 },
  ],
  "courses": {
    1: { "id": 1, "name": "普通心理学", "checked": false, },
    2: { "id": 2, "name": "发展心理学", "checked": false, },
    3: { "id": 3, "name": "社会心理学", "checked": false, },
    4: { "id": 4, "name": "心理统计", "checked": false, },
    5: { "id": 5, "name": "心理测量", "checked": false, },
    6: { "id": 6, "name": "实验心理学", "checked": false, },
    7: { "id": 7, "name": "教育心理学", "checked": false, },
    8: { "id": 8, "name": "管理心理学", "checked": false, },
    9: { "id": 9, "name": "人格心理学", "checked": false, },
    10: { "id": 10, "name": "临床与心理咨询", "checked": false, },
    11: { "id": 11, "name": "变态心理学", "checked": false, },
    12: { "id": 12, "name": "西方心理学史", "checked": false, },
    13: { "id": 13, "name": "心理学研究方法", "checked": false, },
    14: { "id": 14, "name": "英语", "checked": false, },
    15: { "id": 15, "name": "政治", "checked": false, },
  },
  email_sent:[
    { "id": true, "name": "已发" },
    { "id": false, "name": "未发" },
  ],
  major_sent:[
    { "id": 1, "name": "专业课基础资料" },
    { "id": 2, "name": "专业课强化资料" },
    { "id": 3, "name": "专业课冲刺资料" },
  ],
  public_sent:[
    { "id": 1, "name": "公共课基础资料" },
    { "id": 2, "name": "公共课强化资料" },
    { "id": 3, "name": "公共课冲刺资料" },
  ]
};

module.exports = dict;
