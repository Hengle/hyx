<template>
  <div class="teacher">

    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/school_list' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>student</el-breadcrumb-item>

    </el-breadcrumb>
    <br/>


    <el-form :inline="true" class="demo-form-inline" :loading="loading" size="mini">

      <el-form-item>
        <el-input v-model="filter.name" placeholder="学生姓名"></el-input>
      </el-form-item>
      <el-form-item>
        <el-input v-model="filter.target_school" placeholder="报考学校"></el-input>
      </el-form-item>

      <el-form-item>
        <el-input v-model="filter.old_school" placeholder="原学校"></el-input>
      </el-form-item>
      <el-form-item>
        <el-input v-model="filter.due_year" placeholder="届"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button-group>
          <el-button type="primary" @click="fetch" size="mini">查询</el-button>
          <el-button @click="$router.push('sitem?action=create')" size="mini">增加</el-button>
          <el-button @click="  $router.push('/stuUpload')  " size="mini">批量上传</el-button>
          <el-button @click="dataout" size="mini">导出</el-button>
        </el-button-group>
      </el-form-item>

    </el-form>


    <el-table
      :data="list"

      border
      size="mini"
      v-loading="loading"
    >
    <el-table-column prop="remark" label="备注" type="expand">
        <template scope="scope">
          {{scope.row.remark}}
        </template>
      </el-table-column>
      <el-table-column label="序号">
        <template scope="scope">
          {{scope.$index+(page_num-1)*page_size+1}}
        </template>
      </el-table-column>
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="adviser" label="招生顾问" width="100"></el-table-column>
      <!--<el-table-column prop="sex" label="性别"></el-table-column>-->
      <el-table-column prop="mobile" label="电话" width="150"></el-table-column>
      <el-table-column prop="qq" label="qq" width="150"></el-table-column>
      <el-table-column prop="due_year" label="届数"></el-table-column>
      <el-table-column prop="apply_time" label="报班时间"></el-table-column>
      <el-table-column prop="old_school" label="原学校"></el-table-column>
      <el-table-column prop="old_major" label="原专业"></el-table-column>
         <el-table-column prop="target_school" label="目标学校"></el-table-column>
      <!--<el-table-column prop="status" label="状态"></el-table-column>-->


      <!--<el-table-column prop="if_old_major" label="if_old_major"></el-table-column>-->
      <!--<el-table-column prop="create_time" label="create_time"></el-table-column>-->




      <!--<el-table-column prop="background" label="background"></el-table-column>-->
      <el-table-column label="操作" width="225">
        <template scope="scope">
          <el-button-group>
            <el-button type="danger" @click="remove(scope.row)" size="mini">删除</el-button>
            <el-button @click="open_edit(scope.row)" size="mini">编辑</el-button>
            <el-button @click="$router.push('/sitem?id='+scope.row.id)" size="mini">详情</el-button>
          </el-button-group>

        </template>
      </el-table-column>
    </el-table>

    <br>
    <div style="display: inline-block;float: right">
      <el-pagination
        background
        layout="prev, pager, next"
        :total="total"
        @current-change="(p)=>page_num=p"
        :current-page="page_num"
        :page-size="page_size"
      >
      </el-pagination>
    </div>
  </div>
</template>

<script>


  import request from 'axios'

  export default {

    name: 'student',
    data() {
      return {
        list: [],
        total: 0,
        search: '',
        page_size: 10,
        page_num: 1,
        loading: false,
        filter:{
          name:'',
          old_school:'',
          old_major:'',
          due_year:'',
          target_school:''
        }
      }
    },

    watch: {
      page_num() {
        this.fetch()
      }
    },

    methods: {
      dataout() {
        location.href = '/v1/excel/student/export/'
      },
      change_page(p) {
        console.log(p)
      },

      async fetch() {

        var page_size = this.page_size,
          page_num = this.page_num,
          search = this.search,
          that = this
        this.loading = true
        var response = await request.get('/v1/api/student/', {
          params: {
            page_size,
            page_num,
            name:that.filter.name,
            old_school:that.filter.old_school,
            old_major:that.filter.old_major,
            due_year:that.filter.due_year,
            target_school:that.filter.target_school
          }
        })
        this.list = response.data.list
        var page = response.data.page
        this.page_num = page.page_num
        this.page_size = page.page_size
        this.total = page.total
        this.loading = false
      },

      async remove(data) {

        try {
          await this.$confirm('此操作将永久删除该数据, 是否继续?', '提示', {
            confirmButtonTgext: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          })
          var response = await request.delete('/v1/api/student/' + data.id + '/')

          this.$message({
            type: 'success',
            message: '删除成功!'
          });
          this.fetch()
        } catch (e) {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        }

      },
    },
    mounted() {
      this.fetch()
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

</style>
