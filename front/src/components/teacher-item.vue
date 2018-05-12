<template>
  <div class="student-item">
    <el-row :gutter="20">
      <el-col :span="24">
        <el-card class="box-card">
          <h3>基本信息</h3>
          <el-form size="mini" label-width="100">
            <el-form-item label="姓名:">
              <el-input v-if="edit_item" v-model="item.name"></el-input>
              <span v-else>{{item.name}}</span>
            </el-form-item>

             <el-form-item label="手机号:">
              <el-input v-if="edit_item" v-model="item.mobile"></el-input>
              <span v-else>{{item.name}}</span>
            </el-form-item>

             <el-form-item label="qq:">
              <el-input v-if="edit_item" v-model="item.qq"></el-input>
              <span v-else>{{item.name}}</span>
            </el-form-item>

            <el-form-item label="我的学生:">
              <span  v-for="item in student_list">
                <a type="primary" href="javascript:void (0)" @click="$router.push('/sitem?id='+item.id)" >{{item.name}}</a>
                &nbsp;
              </span>

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
    name: 'teacher-item',
    data() {
      return {
        item: {},
        edit_item:true,
        student_list:[]
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
        let res = await request.get('/v1/api/teacher/' + id + '/')
        console.log(res, 'res')
        this.item = res.data
        this.student_list = res.data.student
      },
      async save_item(){
        this.start_loading()
        let id = this.$route.query.id
        let res = await request.put('/v1/api/teacher/' + id + '/',this.item)
        this.end_loading()
        this.item = res.data
        this.student_list = res.data.student
      }

    },
    async mounted() {
      this.fetch()

    }
  }
</script>
<style soped>
  a{
      color: #1ab394;

    }
</style>
