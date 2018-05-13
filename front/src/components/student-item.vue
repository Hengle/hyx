<template>
  <div class="student-item">
    <el-row :gutter="20">
      <el-col :span="12">
        <el-card class="box-card">
          <h3>基本信息</h3>
          <el-form size="mini" label-width="100">
            <el-form-item label="姓名:">
              <el-input v-if="edit_item" v-model="item.name"></el-input>
              <span v-else>{{item.name}}</span>
            </el-form-item>


            <el-form-item label="电话:">
              <el-input v-if="edit_item" v-model="item.mobile"></el-input>
              <span v-else> {{item.mobile}}</span>
            </el-form-item>


            <el-form-item label="qq:">
              <el-input v-if="edit_item" v-model="item.qq"></el-input>
              <span v-else> {{item.qq}}</span>
            </el-form-item>


            <el-form-item label="背景：">
              <el-input v-if="edit_item" v-model="item.background"></el-input>
              <span v-else> {{item.background}}</span>
            </el-form-item>


            <el-form-item label="届数：">
              <el-input v-if="edit_item" v-model="item.due_year"></el-input>
              <span v-else> {{item.due_year}}</span>
            </el-form-item>


            <el-form-item label="报班时间：">
              <el-input v-if="edit_item" v-model="item.apply_time"></el-input>
              <span v-else> {{item.apply_time}}</span>
            </el-form-item>

            <el-form-item label="原专业：">
              <el-input v-if="edit_item" v-model="item.old_major"></el-input>
              <span v-else> {{item.old_major}}</span>

            </el-form-item>


            <el-form-item label="原学校:">
              <el-input v-if="edit_item" v-model="item.old_school"></el-input>
              <span v-else> {{item.old_school}}</span>
            </el-form-item>


            <el-form-item label="性别：">
              <el-input v-if="edit_item" v-model="item.sex"></el-input>
              <span v-else> {{item.sex}}</span>

            </el-form-item>
            <el-form-item label="来源：">

              <el-select v-model="item.source" v-if="edit_item">
                <el-option v-for="item in basic.source" :label="item.name" :value="item.id"></el-option>
              </el-select>
              <span v-else> {{item.source}}</span>
            </el-form-item>

            <el-form-item label="qq群：">

              <el-select v-model="item.qq_group" v-if="edit_item">
                <el-option v-for="item in basic.qqGroup" :label="item.name" :value="item.id"></el-option>
              </el-select>
              <span v-else> {{item.qq_group}}</span>
            </el-form-item>

            <!--<el-form-item label="状态：">-->
            <!--<el-input v-if="edit_item" v-model="item.status"></el-input>-->
            <!--<span v-else> {{item.status}}</span>-->
            <!--</el-form-item>-->
            <el-form-item label="学习状态：">
              <el-select v-model="item.study_status" v-if="edit_item">
                <el-option v-for="item in basic.studyStatus" :label="item.name" :value="item.id"></el-option>
              </el-select>

              <span v-else> {{item.study_status}}</span>
            </el-form-item>

            <el-form-item label="辅导员：">
              <el-select v-model="item.teacher_id" v-if="edit_item">
                <el-option v-for="item in teacher_list" :label="item.name" :value="item.id"></el-option>
              </el-select>
              <span v-else> {{order.class_level}}</span>
            </el-form-item>


            <el-form-item label="入学邮件发放">
              <el-radio-group v-model="item.email_sent">
                <el-radio-button  v-for="i in basic.email_sent" :label="i.id">{{i.name}}</el-radio-button>
              </el-radio-group>
            </el-form-item>
            <el-form-item label="专业课资料发放">
             <el-radio-group v-model="item.major_sent">
                <el-radio-button v-for="i in basic.major_sent" :label="i.id">{{i.name}}</el-radio-button>
              </el-radio-group>
            </el-form-item>
            <el-form-item label="公共课资料发放">
             <el-radio-group v-model="item.public_sent">
                <el-radio-button  v-for="i in basic.public_sent" :label="i.id">{{i.name}}</el-radio-button>
              </el-radio-group>
            </el-form-item>

            <el-form-item label="备注：">
              <el-input v-if="edit_item" v-model="item.remark" type="textarea" rows="6"></el-input>
              <span v-else> {{item.remark}}</span>

            </el-form-item>

            <span style="float: right">
              <el-button v-if="!edit_item" @click="edit_item=true">编辑</el-button>
               <el-button v-else @click="save_item" type="primary">保存</el-button>
            </span>

            <br/>

          </el-form>
        </el-card>

        <br/>
        <el-card>
          <h3>报考信息</h3>
          <el-form size="mini" label-width="100">
            <el-form-item label="目标学校：">
              <el-input v-if="edit_order" v-model="order.target_school"></el-input>
              <span v-else> {{order.target_school}}</span>
            </el-form-item>
            <el-form-item label="目标专业：">
              <el-input v-if="edit_order" v-model="order.target_major"></el-input>
              <span v-else> {{order.target_major}}</span>
            </el-form-item>


            <span style="float: right">
              <el-button v-if="!edit_order" @click="edit_order=true">编辑</el-button>
               <el-button v-else @click="save_item" type="primary">保存</el-button>
            </span>
            <br/>
          </el-form>

        </el-card>
      </el-col>

      <el-col :span="12">
        <el-card>
          <h3>专业课</h3>
          <el-form size="mini" label-width="100">
            <el-form-item label="报班级别：">
              <el-select v-model="pro.class_level" v-if="edit_item">
                <el-option v-for="item in basic.classLevelProfessional" :label="item.name" :value="item.id"></el-option>
              </el-select>
              <span v-else> {{order.class_level}}</span>
            </el-form-item>

            <el-form-item label="费用">
              <el-input v-model="pro.fee"></el-input>
            </el-form-item>

            <el-form-item label="沟通次数">
              <el-input v-model="pro.skype_count"></el-input>
            </el-form-item>

            <el-form-item label="是否签协议">
              <el-radio-group v-model="pro.if_protocol">
                <el-radio-button :label="1">是</el-radio-button>
                <el-radio-button :label="0">否</el-radio-button>
              </el-radio-group>
            </el-form-item>

            <span style="float: right">
              <el-button v-if="!edit_order" @click="edit_order=true">编辑</el-button>
               <el-button v-else @click="save_pro" type="primary">保存</el-button>
            </span>
            <br/>
          </el-form>

        </el-card>
        <br/>
        <el-card>
          <h3>英语</h3>
          <el-form size="mini" label-width="100">
            <el-form-item label="报班级别：">
              <el-select v-model="eng.class_level" v-if="edit_item">
                <el-option v-for="item in basic.classLevelProfessional" :label="item.name" :value="item.id"></el-option>
              </el-select>
              <span v-else> {{order.class_level}}</span>
            </el-form-item>

            <el-form-item label="费用">
              <el-input v-model="eng.fee"></el-input>
            </el-form-item>


            <el-form-item label="沟通次数">
              <el-input v-model="eng.skype_count"></el-input>
            </el-form-item>

            <el-form-item label="是否签协议">
              <el-radio-group v-model="eng.if_protocol">
                <el-radio-button :label="1">是</el-radio-button>
                <el-radio-button :label="0">否</el-radio-button>
              </el-radio-group>
            </el-form-item>

            <span style="float: right">
              <el-button v-if="!edit_order" @click="edit_order=true">编辑</el-button>
               <el-button v-else @click="save_eng" type="primary">保存</el-button>
            </span>
            <br/>
          </el-form>

        </el-card>

        <br/>

        <el-card>
          <h3>政治</h3>
          <el-form size="mini" label-width="100">
            <el-form-item label="报班级别：">
              <el-select v-model="pol.class_level" v-if="edit_item">
                <el-option v-for="item in basic.classLevelProfessional" :label="item.name" :value="item.id"></el-option>
              </el-select>
              <span v-else> {{order.class_level}}</span>
            </el-form-item>

            <el-form-item label="费用">
              <el-input v-model="pol.fee"></el-input>
            </el-form-item>


            <el-form-item label="沟通次数">
              <el-input v-model="pol.skype_count"></el-input>
            </el-form-item>

            <el-form-item label="是否签协议">
              <el-radio-group v-model="pol.if_protocol">
                <el-radio-button :label="1">是</el-radio-button>
                <el-radio-button :label="0">否</el-radio-button>
              </el-radio-group>
            </el-form-item>

            <span style="float: right">
              <el-button v-if="!edit_order" @click="edit_order=true">编辑</el-button>
               <el-button v-else @click="save_pol" type="primary">保存</el-button>
            </span>
            <br/>
          </el-form>

        </el-card>
        <br/>
        <el-card>
          <h3>公共课</h3>
          <el-form size="mini" label-width="100">
            <el-form-item label="报班级别：">
              <el-select v-model="com.class_level" v-if="edit_item">
                <el-option v-for="item in basic.classLevelProfessional" :label="item.name" :value="item.id"></el-option>
              </el-select>
              <span v-else> {{order.class_level}}</span>
            </el-form-item>

            <el-form-item label="费用">
              <el-input v-model="com.fee"></el-input>
            </el-form-item>


            <el-form-item label="沟通次数">
              <el-input v-model="com.skype_count"></el-input>
            </el-form-item>

            <span style="float: right">
              <el-button v-if="!edit_order" @click="edit_order=true">编辑</el-button>
               <el-button v-else @click="save_com" type="primary">保存</el-button>
            </span>
            <br/>
          </el-form>

        </el-card>


      </el-col>
    </el-row>

    <br/>

  </div>
</template>
<script>
  import request from 'axios'
  let loading
  var basic = require('../stableDict')


  export default {
    name: 'student-item',
    data() {
      return {
        item: {},
        order: {},
        pro: {},
        eng:{},
        pol:{},
        com:{},
        edit_item: true,
        edit_order: true,
        edit_pro: true,
        basic: basic,
        teacher_list:[]
      }
    },
    methods: {

      start_loading(){
        loading = this.$loading({
          lock: true,
          text: '正在修改...',
          spinner: 'el-icon-loading',
          background: 'rgba(0, 0, 0, 0.1)'
        });
      },
      end_loading(){
        loading.close()
      },

      async fetch() {

        let id = this.$route.query.id
        let res = await request.get('/v1/api/student/' + id + '/')
        console.log(res, 'res')

        this.item = res.data
      },

      async save_item() {
        this.start_loading()
        let id = this.$route.query.id
        let res = await request.put('/v1/api/student/' + id + '/', this.item)
        console.log(res, 'res')
        this.end_loading()
        this.item = res.data
      },

      async fetch_order() {
        let id = this.$route.query.id
        let res = await request.get('/v1/api/order/' + id + '/')
        console.log(res, 'order')
        this.order = res.data
      },
      async save_order(){
        this.start_loading()
         let id = this.$route.query.id
        let res = await request.put('/v1/api/order/' + id + '/', this.order)
        console.log(res, 'res')
        this.end_loading()
        this.item = res.data
      },

      async fetch_pro() {
        let id = this.order.id
        let res = await request.get('/v1/api/pro/' + id + '/')
        console.log(res, 'order')
        this.pro = res.data
      },
       async save_pro(){
        this.start_loading()
         let id = this.order.id
        let res = await request.put('/v1/api/pro/' + id + '/', this.pro)
        console.log(res, 'res')
         this.end_loading()
        this.item = res.data
      },


      async fetch_eng() {
        let id = this.order.id
        let res = await request.get('/v1/api/eng/' + id + '/')
        console.log(res, 'order')
        this.eng = res.data
      },
       async save_eng(){
        this.start_loading()
        let id = this.order.id
        let res = await request.put('/v1/api/eng/' + id + '/', this.eng)
        console.log(res, 'res')
         this.end_loading()
        this.item = res.data
      },

      async fetch_com() {
        let id = this.order.id
        let res = await request.get('/v1/api/com/' + id + '/')
        console.log(res, 'order')
        this.com = res.data
      },
       async save_com(){
        this.start_loading()
        let id = this.order.id
        let res = await request.put('/v1/api/com/' + id + '/', this.com)
        console.log(res, 'res')
         this.end_loading()
        this.item = res.data
      },

      async fetch_pol() {
        let id = this.order.id
        let res = await request.get('/v1/api/pol/' + id + '/')
        console.log(res, 'order')
        this.pol = res.data
      },
       async save_pol(){
        this.start_loading()
        let id = this.order.id
        let res = await request.put('/v1/api/pol/' + id + '/', this.pol)
        console.log(res, 'res')
         this.end_loading()
        this.pol = res.data
      },
      async fetch_teacher(){
        let res = await request.get('/v1/api/teacher/' )
        console.log(res, 'res')
        this.teacher_list = res.data.list
      }
    },
    async mounted() {

      await this.fetch_teacher()
      this.fetch()
      await this.fetch_order()

      this.fetch_pro()
      this.fetch_eng()
      this.fetch_com()
      this.fetch_pol()

    }
  }
</script>
<style>

</style>
