<template>
  <div class="teacher">

    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/school_list' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>teacher</el-breadcrumb-item>

    </el-breadcrumb>
    <br/>


    <el-form :inline="true" class="demo-form-inline" :loading="loading" size="mini">
      <el-form-item>
        <el-input v-model="filter.name" placeholder="姓名"></el-input>
      </el-form-item>
      <el-form-item>
        <el-input v-model="filter.job" placeholder="工作"></el-input>
      </el-form-item>

      <el-form-item>
        <el-input v-model="filter.fudao_school" placeholder="辅导院校"></el-input>
      </el-form-item>
      <el-form-item>
        <el-select v-model="filter.is_stay" placeholder="是否留任" clearable>
          <el-option value="是"></el-option>
          <el-option value="否"></el-option>
        </el-select>
      </el-form-item>

      <el-form-item>
        <el-select v-model="filter.is_cross_major" placeholder="是否跨专业" clearable>
          <el-option value="本专业">本专业</el-option>
          <el-option value="跨专业">跨专业</el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-select v-model="filter.is_war_more" placeholder="一站OR多战" clearable>
          <el-option value="一战">一战</el-option>
          <el-option value="多战">多战</el-option>
        </el-select>
      </el-form-item>

      <el-form-item>
        <el-select v-model="filter.is_wokring" placeholder="是否在职考研" clearable>
          <el-option value="是">是</el-option>
          <el-option value="否">否</el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-input v-model="filter.study_type" placeholder="学制类型"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button-group>
          <el-button type="primary" @click="fetch" size="mini">查询</el-button>
          <el-button @click="$router.push('/teaItem?action=create')" size="mini">增加</el-button>
          <el-button @click="  $router.push('/teaUpload')  " size="mini">批量上传</el-button>
          <el-button @click="  loadout  " size="mini">导出老师数据</el-button>
        </el-button-group>
      </el-form-item>

    </el-form>


    <el-table
      :data="list"
      style="width: 100%"
      border
      size="mini"
      v-loading="loading"
    >


      <el-table-column label="序号">
        <template scope="scope">
          {{scope.$index+(page_num-1)*page_size+1}}
        </template>
      </el-table-column>

      <el-table-column prop="name" label="姓名"></el-table-column>
      <!--<el-table-column prop="sex" label="性别"></el-table-column>-->
      <el-table-column prop="mobile" label="手机"></el-table-column>
      <el-table-column prop="qq" label="qq"></el-table-column>


      <el-table-column label="操作" width="250">
        <template scope="scope">
          <el-button-group>
            <el-button type="danger" @click="remove(scope.row)" size="mini">删除</el-button>
            <el-button @click="open_edit(scope.row)" size="mini">编辑</el-button>
            <el-button @click="$router.push('/teaItem?id='+scope.row.id)" size="mini">详情</el-button>
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

    name: 'teacher',
    data() {
      return {
        list: [],
        total: 0,
        page_size: 10,
        page_num: 1,
        loading: false,

        filter: {
          study_type:'',
          is_working:'',
          is_war_more:"",
          is_cross_major:"",
          is_stay:'',
          fudao_school:'',
          job:'',
          name:''
        }
      }
    },

    watch: {
      page_num() {
        this.fetch()
      }
    },
    methods: {
      change_page(p) {
        console.log(p)
      },
      loadout() {
        location.href = '/v1/excel/teacher/export/'
      },

      async fetch() {

        var page_size = this.page_size,
          page_num = this.page_num,
          that = this
        this.loading = true

        let filter = {...this.filter}

        filter.page_size = page_size
        filter.page_num = page_num

        var response = await request.get('/v1/api/teacher/', {
          params: filter
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
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          })
          var response = await request.delete('/v1/api/teacher/' + data.id + '/')

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
