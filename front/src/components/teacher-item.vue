<template>
  <div class="student-item">
    <el-card class="box-card">
      <el-form label-width="100px" size="mini">
        <el-row :gutter="50">
          <el-col :span="12">


            <el-button-group >
              <el-button v-if="!edit_item" @click="edit_item=true" size="mini">编辑</el-button>
              <el-button v-if="edit_item&&!create" @click="edit_item=false" size="mini">取消</el-button>
               <el-button v-if=" edit_item&&!create " @click="save_item" type="primary" size="mini">保存</el-button>
              <el-button v-if="edit_item&&create" @click="post" type="primary" size="mini">提交</el-button>
            </el-button-group>

            <h3>基本信息</h3>

            <el-form-item label="我的学生:">
              <span v-for="item in student_list">
                <a type="primary" href="javascript:void (0)"
                   @click="$router.push('/sitem?id='+item.id)">{{item.name}}</a>
                &nbsp;
              </span>

            </el-form-item>

              <el-form-item label="姓名:">
                <el-input v-if="edit_item" v-model="item.name"></el-input>
                <span v-else>{{item.name}}</span>
              </el-form-item>

              <el-form-item label="手机号:">
                <el-input v-if="edit_item" v-model="item.mobile"></el-input>
                <span v-else>{{item.mobile}}</span>
              </el-form-item>

              <el-form-item label="qq:">
                <el-input v-if="edit_item" v-model="item.qq"></el-input>
                <span v-else>{{item.qq}}</span>
              </el-form-item>

              <el-form-item label="身份证:">
                <el-input v-if="edit_item" v-model="item.idcard"></el-input>
                <span v-else>{{item.idcard}}</span>
              </el-form-item>

            <el-form-item label="银行:">
                <el-input v-if="edit_item" v-model="item.bank_name"></el-input>
                <span v-else>{{item.bank_name}}</span>
              </el-form-item>


            <el-form-item label="银行卡号:">
                <el-input v-if="edit_item" v-model="item.bank_number"></el-input>
                <span v-else>{{item.bank_number}}</span>
              </el-form-item>

              <el-form-item label="工作:">
                <el-input v-if="edit_item" v-model="item.job"></el-input>
                <span v-else>{{item.job}}</span>
              </el-form-item>

        <el-form-item label="本科学校:">
                <el-input v-if="edit_item" v-model="item.bachelor_school"></el-input>
                <span v-else>{{item.bachelor_school}}</span>
              </el-form-item>

              <el-form-item label="本科专业:">
                <el-input v-if="edit_item" v-model="item.bachelor_major"></el-input>
                <span v-else>{{item.bachelor_major}}</span>
              </el-form-item>

             <el-form-item label="312具体院校:">
                <el-input v-if="edit_item" v-model="item.school_312"></el-input>
                <span v-else>{{item.school_312}}</span>
              </el-form-item>

             <el-form-item label="辅导院校:">
                <el-input v-if="edit_item" v-model="item.fudao_school"></el-input>
                <span v-else>{{item.fudao_school}}</span>
              </el-form-item>

              <el-form-item label="备注：">
                <el-input v-if="edit_item" v-model="item.remark" type="textarea" rows="6"></el-input>
                <span v-else> {{item.remark}}</span>
              </el-form-item>



              <br/>


            <br/>

          </el-col>

          <el-col :span="12">
          <h3>老师考试信息</h3>



               <el-form-item label="是否在职考研:">
                <el-input v-if="edit_item" v-model="item.is_wokring"></el-input>
                <span v-else>{{item.is_wokring}}</span>
              </el-form-item>

             <el-form-item label="是否跨专业:">
                <el-input v-if="edit_item" v-model="item.is_cross_major"></el-input>
                <span v-else>{{item.is_cross_major}}</span>
              </el-form-item>

                  <el-form-item label="一站or多战:">
                <el-input v-if="edit_item" v-model="item.is_war_more"></el-input>
                <span v-else>{{item.is_war_more}}</span>
              </el-form-item>

               <el-form-item label="英语分:">
                <el-input v-if="edit_item" v-model="item.english_class_score"></el-input>
                <span v-else>{{item.english_class_score}}</span>
              </el-form-item>


          <el-form-item label="英语分:">
                <el-input v-if="edit_item" v-model="item.english_class_score"></el-input>
                <span v-else>{{item.english_class_score}}</span>
              </el-form-item>
                     <el-form-item label="政治分:">
                <el-input v-if="edit_item" v-model="item.politic_class_score"></el-input>
                <span v-else>{{item.politic_class_score}}</span>
              </el-form-item>
                   <el-form-item label="专业课分:">
                <el-input v-if="edit_item" v-model="item.pro_class_score"></el-input>
                <span v-else>{{item.pro_class_score}}</span>
              </el-form-item>
            <el-form-item label="初试总成绩:">
                <el-input v-if="edit_item" v-model="item.first_total"></el-input>
                <span v-else>{{item.first_total}}</span>
              </el-form-item>
               <el-form-item label="初试排名:">
                <el-input v-if="edit_item" v-model="item.first_rank"></el-input>
                <span v-else>{{item.first_rank}}</span>
              </el-form-item>
               <el-form-item label="复试排名:">
                <el-input v-if="edit_item" v-model="item.first_rank"></el-input>
                <span v-else>{{item.first_rank}}</span>
              </el-form-item>
                   <el-form-item label="复试排名:">
                <el-input v-if="edit_item" v-model="item.final_rank"></el-input>
                <span v-else>{{item.final_rank}}</span>
              </el-form-item>

               <el-form-item label="是否通过考试:">
                <el-input v-if="edit_item" v-model="item.is_passed"></el-input>
                <span v-else>{{item.is_passed}}</span>
              </el-form-item>

              <el-form-item label="录取方式:">
                <el-input v-if="edit_item" v-model="item.passed_type"></el-input>
                <span v-else>{{item.passed_type}}</span>
              </el-form-item>

                     <el-form-item label="学年:">
                <el-input v-if="edit_item" v-model="item.study_year"></el-input>
                <span v-else>{{item.study_year}}</span>
              </el-form-item>

                  <el-form-item label="学制类型:">
                <el-input v-if="edit_item" v-model="item.study_type"></el-input>
                <span v-else>{{item.study_type}}</span>
              </el-form-item>


                  <el-form-item label="是否留任:">
                <el-input v-if="edit_item" v-model="item.is_stay"></el-input>
                <span v-else>{{item.is_stay}}</span>
              </el-form-item>

            <h3>老师带班信息</h3>


                  <el-form-item label="微信群:">
                <el-input v-if="edit_item" v-model="item.is_weixunqun"></el-input>
                <span v-else>{{item.is_weixunqun}}</span>
              </el-form-item>


                  <el-form-item label="校区群:">
                <el-input v-if="edit_item" v-model="item.is_xiaoqugroup"></el-input>
                <span v-else>{{item.is_xiaoqugroup}}</span>

              </el-form-item>

                 <el-form-item label="智囊团群:">
                <el-input v-if="edit_item" v-model="item.is_zhinanqun"></el-input>
                <span v-else>{{item.is_zhinanqun}}</span>
              </el-form-item>


                  <el-form-item label="辅导工作群:">
                <el-input v-if="edit_item" v-model="item.is_fudaogongzuoqun"></el-input>
                <span v-else>{{item.is_fudaogongzuoqun}}</span>

              </el-form-item>

               <el-form-item label="协议书发放:">
                <el-input v-if="edit_item" v-model="item.is_xieyi_send"></el-input>
                <span v-else>{{item.is_xieyi_send}}</span>
              </el-form-item>


                  <el-form-item label="协议书收回:">
                <el-input v-if="edit_item" v-model="item.is_xieyi_back"></el-input>
                <span v-else>{{item.is_xieyi_back}}</span>

              </el-form-item>
          </el-col>

        </el-row>
      </el-form>
    </el-card>
    <br/>

  </div>
</template>
<script>
  import request from 'axios'

  let loading
  var basic = require('../stableDict')
  export default {
    name: 'teacher-item',
    data() {
      return {
        item: {},
        edit_item: true,
        student_list: [],
        create:false
      }
    },
    methods: {
      start_loading() {
        loading = this.$loading({
          lock: true,
          text: '正在修改...',
          spinner: 'el-icon-loading',
          background: 'rgba(0, 0, 0, 0.1)'
        });
      },
      end_loading() {
        loading.close()
      },

      async fetch() {
        let id = this.$route.query.id
        let res = await request.get('/v1/api/teacher/' + id + '/')
        console.log(res, 'res')
        this.item = res.data
        this.student_list = res.data.student
      },
      async save_item() {

        console.log(this.item)
        return
        this.start_loading()
        let id = this.$route.query.id
        let res = await request.put('/v1/api/teacher/' + id + '/', this.item)
        this.end_loading()
        this.item = res.data
        this.student_list = res.data.student
      },
      async post() {
        this.start_loading()
        let res = await request.post('/v1/api/teacher/', this.item)
        this.end_loading()
        this.item = res.data
      }

    },
    async mounted() {
      console.log(this.$route.query.action,'this.$route.query.action')
      if(this.$route.query.action == 'create'){
        this.create = true
        this.edit_item = true
      }else {
        this.fetch()
        this.edit_item = false
        this.create = false
      }


    }
  }
</script>
<style soped>
  a {
    color: #1ab394;

  }
</style>
