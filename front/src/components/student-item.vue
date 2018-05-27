<template>
  <div class="student-item">
    <el-row :gutter="20">


        <el-card class="box-card">
          <el-row :gutter="100">
            <el-col :span="12">
                <h3>基本信息</h3>

          <el-form size="mini" label-width="150px">
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



            <el-form-item label="备注：" >
              <el-input v-if="edit_item" v-model="item.remark" type="textarea" rows="6"></el-input>
              <span v-else> {{item.remark}}</span>
            </el-form-item>

          </el-form>
            </el-col>

            <el-col :span="12">

            <el-form size="mini" label-width="150px">
               <h3>专业课报班级信息</h3>

                 <el-form-item label="报班级别：">
              <el-select v-model="item.pro.class_level" v-if="edit_item">
                <el-option v-for="item in basic.classLevelProfessional" :label="item.name" :value="item.id"></el-option>
              </el-select>

            </el-form-item>


            <el-form-item label="一共沟通次数">
              <el-input v-model="item.pro.skype_count"></el-input>
           </el-form-item>


           

            <el-form-item label="是否签协议">
              <el-radio-group v-model="item.pro.if_protocol">
                <el-radio-button :label="1">是</el-radio-button>
                <el-radio-button :label="0">否</el-radio-button>
              </el-radio-group>
            </el-form-item>
            </el-form>




            <br/>

            <el-form  size="mini" label-width="150px">
               <h3>英语课报班级信息</h3>

                 <el-form-item label="报班级别：">
              <el-select v-model="item.eng.class_level" v-if="edit_item">
                <el-option v-for="item in basic.classLevelProfessional" :label="item.name" :value="item.id"></el-option>
              </el-select>

            </el-form-item>


            <el-form-item label="一共沟通次数">

              <el-input v-model="item.eng.skype_count"></el-input>
             </el-form-item>

          

            <el-form-item label="是否签协议">
              <el-radio-group v-model="item.eng.if_protocol">
                <el-radio-button :label="1">是</el-radio-button>
                <el-radio-button :label="0">否</el-radio-button>
              </el-radio-group>
            </el-form-item>
            </el-form>

            <br/>

            <el-form  size="mini" label-width="150px">
               <h3>政治课报班级信息</h3>

                 <el-form-item label="报班级别：">
              <el-select v-model="item.pol.class_level" v-if="edit_item">
                <el-option v-for="item in basic.classLevelProfessional" :label="item.name" :value="item.id"></el-option>
              </el-select>

            </el-form-item>


            <el-form-item label="一共沟通次数">
              <el-input v-model="item.pol.skype_count"></el-input>
            </el-form-item>


            <el-form-item label="是否签协议">
              <el-radio-group v-model="item.pol.if_protocol">
                <el-radio-button :label="1">是</el-radio-button>
                <el-radio-button :label="0">否</el-radio-button>
              </el-radio-group>
            </el-form-item>
            </el-form>

                   <br/>

            <el-form  size="mini" label-width="150px">
               <h3>公共课报班级信息</h3>

                 <el-form-item label="报班级别：">
              <el-select v-model="item.com.class_level" v-if="edit_item">
                <el-option v-for="item in basic.classLevelProfessional" :label="item.name" :value="item.id"></el-option>
              </el-select>

            </el-form-item>


            <el-form-item label="一共沟通次数">
              <el-input v-model="item.com.skype_count"></el-input>
             </el-form-item>


            <el-form-item label="是否签协议">
              <el-radio-group v-model="item.com.if_protocol">
                <el-radio-button :label="1">是</el-radio-button>
                <el-radio-button :label="0">否</el-radio-button>
              </el-radio-group>
            </el-form-item>
            </el-form>

            </el-col>


          </el-row>





           <span style="float: right">
              <el-button v-if="!edit_item" @click="edit_item=true">编辑</el-button>
               <el-button v-else @click="save_item" type="primary" size="mini">保存</el-button>
              <br/>
            </span>
          <br/>
        </el-card>


    </el-row>



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
        item: {
          pro:{},
          eng:{},
          pol:{},
          com:{}
        },

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
        this.end_loading()
      },

      async fetch_teacher(){
        let res = await request.get('/v1/api/teacher/' )
        this.teacher_list = res.data.list
      },

      async save_item(){
        try {
            this.start_loading()
          let id = this.$route.query.id
        let res = await request.put('/v1/api/student/'+id+'/',this.item)
        this.item = res.item

        this.end_loading()
        }catch (e) {
          this.end_loading()
        }

      },


    },
    async mounted() {
      this.start_loading()
      await this.fetch_teacher()
      this.fetch()


    }
  }
</script>
<style>

</style>
