<template>
  <div class="student-item">
<el-form :inline="true">
      <el-form-item label="总数据">{{total}}</el-form-item>
      <el-form-item label="成功数">{{success}}</el-form-item>
      <el-form-item label="失败数">{{error}}</el-form-item>
    <el-form-item label="名字">
         <span v-for="e in err_list">{{e}}&nbsp;&nbsp;</span>
       </el-form-item>
    </el-form>
    <el-form :inline="true" class="demo-form-inline" size="mini">


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

    <el-table
      :data="list"
      style="width: 100%"
      border
      size="mini"

    >



      <el-table-column prop="name" label="姓名"></el-table-column>
      <!--<el-table-column prop="sex" label="性别"></el-table-column>-->
      <el-table-column prop="mobile" label="手机"></el-table-column>
      <el-table-column prop="qq" label="qq"></el-table-column>
<el-table-column prop="status" label="状态"></el-table-column>

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

  let loading
  var basic = require('../stableDict')
  export default {
    name: 'teacher-item',
    data() {
      return {
        list:[],
        success:0,
        total:0,
        error:0,
        err_list:[]
      }
    },
    methods: {
      download_template() {
        location.href = '/v1/excel/teacher_template'
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

          that.list = list
          that.total = list.length
          that.error = 0
        };

        reader.readAsBinaryString(file);
      },

      async upload(){
       var that = this
         let r = function (i) {
         request.post('/v1/excel/teacher_upload',that.list[i]).then(function (res) {
            that.success = that.success +1
          }).catch(function (e) {
           // that.error=that.error+1
           console.log('hllo')
           that.error = that.error +1
           that.err_list.push(that.list[i].name)
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
