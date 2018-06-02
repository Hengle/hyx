<template>
    <div class="teacher">

        <el-breadcrumb separator="/">
            <el-breadcrumb-item :to="{ path: '/school_list' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>teacher</el-breadcrumb-item>

        </el-breadcrumb>
        <br/>


        <el-form :inline="true" class="demo-form-inline" :loading="loading" size="mini">

            <el-form-item label="姓名">
                <el-input v-model="search" placeholder="查询"></el-input>
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


        <el-dialog title="新增" :visible.sync="add_form.visible"
        >
            <el-form class="demo-form-inline" label-width="100px" :model="add_form" status-icon size="mini"
                     ref="add_form">
                <el-form-item label="name" prop="姓名">
                        <el-input v-model="add_form.name"></el-input>
                </el-form-item>
                <!--<el-form-item label="sex" prop="性别">-->
                        <!--<el-input v-model="add_form.sex"></el-input>-->
                <!--</el-form-item>-->
                <el-form-item label="qq" prop="qq">
                        <el-input v-model="add_form.qq"></el-input>
                </el-form-item>
                <el-form-item label="手机" prop="手机号">
                        <el-input v-model="add_form.mobile"></el-input>
                </el-form-item>

            </el-form>


            <span slot="footer" class="dialog-footer">
          <el-button @click="add_form.visible=false" size="mini">取 消</el-button>
          <el-button type="primary" @click="add" size="mini">确 定</el-button>
        </span>
        </el-dialog>


        <el-dialog title="编辑" :visible.sync="edit_form.visible"
        >
            <el-form class="demo-form-inline" label-width="100px" :model="edit_form" status-icon size="mini"
                     ref="edit_form">
              <el-form-item label="name" prop="姓名">
                        <el-input v-model="edit_form.name"></el-input>
                </el-form-item>
                <!--<el-form-item label="sex" prop="性别">-->

                        <!--<el-input v-model="edit_form.sex"></el-input>-->

                <!--</el-form-item>-->
                <el-form-item label="qq" prop="qq">

                        <el-input v-model="edit_form.qq"></el-input>
                </el-form-item>
                <el-form-item label="手机" prop="手机号">

                        <el-input v-model="edit_form.mobile"></el-input>

                </el-form-item>

            </el-form>


            <span slot="footer" class="dialog-footer">
          <el-button @click="edit_form.visible=false" size="mini">取 消</el-button>
          <el-button type="primary" @click="edit" size="mini">确 定</el-button>
        </span>
        </el-dialog>


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
                search: '',
                page_size: 10,
                page_num: 1,
                loading: false,
                add_form: {
                    visible:false,
                    name:'',
                    // sex:'',
                    mobile:'',
                    qq:''
                },
                edit_form: {
                    visible:false,
                    name:'',
                    // sex:'',
                    mobile:'',
                    qq:''
                },
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
            loadout(){
              location.href = '/v1/excel/teacher/export/'
            },

            async fetch() {

                var page_size = this.page_size,
                    page_num = this.page_num,
                    search = this.search,
                    that = this
                this.loading = true
                var response = await request.get('/v1/api/teacher/', {
                    params: {
                        page_size,
                        page_num,
                        search
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
