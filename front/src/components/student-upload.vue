<template>
  <div class="student-item">

    <el-form :inline="true" class="demo-form-inline"  size="mini">

      <el-form-item>
        <el-button-group>
          <el-button @click="  download_template  " size="mini">下载模板</el-button>

        </el-button-group>

      </el-form-item>
      <el-form-item>
        <input type="file" @change="onchange" value="上传"/>
      </el-form-item>
     <el-form-item>
        <el-button @click="  upload  " size="mini">上传</el-button>
      </el-form-item>


    </el-form>
    <el-form>
      <el-form-item label="总数据">{{total}}</el-form-item>
      <el-form-item label="成功数">{{success}}</el-form-item>
      <el-form-item label="失败数">{{error}}</el-form-item>
       <el-form-item label="名字">
         <span v-for="e in err_list">{{e}}&nbsp;&nbsp;</span>
       </el-form-item>
    </el-form>
    <br/>

    <el-table
      :data="list"
      style="width: 100%"
      border
      size="mini"

    >



      <el-table-column prop="apply_time" label="报班时间"></el-table-column>

      <el-table-column prop="adviser" label="招生顾问"></el-table-column>
      <el-table-column prop="target_school" label="报考学校"></el-table-column>
    <el-table-column prop="name" label="姓名"></el-table-column>
 <el-table-column prop="class_level" label="班型"></el-table-column>
      <el-table-column prop="public_class" label="公共课"></el-table-column>
      <el-table-column prop="due_year" label="届"></el-table-column>
      <el-table-column prop="qq" label="qq"></el-table-column>
      <el-table-column prop="mobile" label="电话"></el-table-column>

   <el-table-column prop="old_major" label="专业"></el-table-column>
      <el-table-column prop="old_school" label="本科学校"></el-table-column>
      <!--<el-table-column prop="remark" label="备注"></el-table-column>-->

  <!--<el-table-column prop="status" label="状态">-->
      <!--<template scope="scope">-->
          <!--<p style="color: rgba(0,0,0,0.3)" v-if="scope.row.status =='准备上传' ">{{scope.row.status}}</p>-->
          <!--<p style="color: #1ab394" v-else>{{scope.row.status}}</p>-->
      <!--</template>-->
  <!--</el-table-column>-->

      <!--<el-table-column label="操作" width="250">-->
        <!--<template scope="scope">-->
          <!--<el-button-group>-->
            <!--<el-button type="danger" @click="retry(scope.row)" size="mini">重试</el-button>-->

          <!--</el-button-group>-->
        <!--</template>-->
      <!--</el-table-column>-->
    </el-table>
  </div>
</template>
<script>
  import request from 'axios'
  import Vue from 'vue'
  let loading
  var basic = require('../stableDict')
  export default {
    name: 'teacher-item',
    data() {
      return {
        list:[],

        error:0,
        success:0,
        total:0,
        err_list:[]
      }
    },
    methods: {
      download_template() {
        location.href = '/v1/excel/student_template'
      },
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
      retry(){

      },


      onchange(f) {
        var that = this
        let file = f.target.files[0], name = file.name,reader = new FileReader();
        reader.onload = function (e) {
          let data = e.target.result;
          let wb = XLSX.read(data, {type: "binary"});
          let list = XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]])
          list = list.map(function (obj) {
            console.log(obj)
            obj.apply_time = obj['报班时间']
            obj.adviser = obj['招生顾问']
            obj.target_school = obj['报考学校']
            obj.name = obj['姓名']
            obj.pro_class_level = obj['班型']
            obj.public_class = obj['公共课']
            obj.due_year = obj['届']
            obj.qq = obj['qq']
            obj.mobile = obj['电话']
            obj.old_major = obj['专业']
            obj.old_school = obj['本科学校']
            obj.remark = obj['备注']

            delete obj['报班时间']
            delete obj['招生顾问']
            delete obj['报考学校']
            delete obj['公共课']
            delete obj['姓名']
            delete obj['班型']
            delete obj['届']


            delete obj['电话']
            delete obj['专业']
            delete obj['本科学校']
            delete obj['备注']
            obj.status = '准备上传'
            return obj
          })

          that.list = list
          that.total = that.list.length
          that.success =0
          that.error = 0
        };
        reader.readAsBinaryString(file);
      },

      async upload(){
        var that = this
         let r = function (i) {


         request.post('/v1/excel/student_upload',that.list[i]).then(function (res) {
            that.success = that.success +1
          }).catch(function (e) {
           that.error=that.error+1
           that.error_list.push(that.list[i].name)
         })
        }
        for(var i=0;i<this.list.length;i++){
            r(i)
        }



      }

    },
    async mounted() {


    }
  }
</script>
<style soped>
  a {
    color: #1ab394;

  }
</style>
