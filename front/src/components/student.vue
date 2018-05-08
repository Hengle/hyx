<template>
    <div class="teacher">

        <el-breadcrumb separator="/">
            <el-breadcrumb-item :to="{ path: '/school_list' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>student</el-breadcrumb-item>

        </el-breadcrumb>
        <br/>


        <el-form :inline="true" class="demo-form-inline" :loading="loading" size="mini">

            <el-form-item label="姓名">
                <el-input v-model="search" placeholder="查询"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button-group>
                    <el-button type="primary" @click="fetch" size="mini">查询</el-button>
                    <el-button @click="add_form.visible=true" size="mini">增加</el-button>

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
            <el-table-column prop="sex" label="性别"></el-table-column>
            <el-table-column prop="mobile" label="电话"></el-table-column>
            <el-table-column prop="qq" label="qq"></el-table-column>
            <el-table-column prop="due_year" label="due_year"></el-table-column>
            <el-table-column prop="apply_time" label="apply_time"></el-table-column>
             <el-table-column prop="old_school" label="原来学校"></el-table-column>
            <el-table-column prop="old_major" label="原来专业"></el-table-column>
            <el-table-column prop="status" label="状态"></el-table-column>
          <!--<el-table-column prop="remark" label="remark"></el-table-column>-->
 <el-table-column prop="adviser" label="adviser"></el-table-column>
            <el-table-column prop="if_old_major" label="if_old_major"></el-table-column>
            <!--<el-table-column prop="create_time" label="create_time"></el-table-column>-->




            <el-table-column prop="background" label="background"></el-table-column>
            <el-table-column label="操作" width="190">
                <template scope="scope">
                    <el-button-group>
                        <el-button type="danger" @click="remove(scope.row)" size="mini">删除</el-button>
                        <el-button @click="open_edit(scope.row)" size="mini">编辑</el-button>
                    </el-button-group>

                </template>
            </el-table-column>
        </el-table>


        <el-dialog title="新增" :visible.sync="add_form.visible"
        >
            <el-form class="demo-form-inline" label-width="100px" :model="add_form" status-icon size="mini"
                     ref="add_form">



                <el-form-item label="if_old_major" prop="if_old_major">

                        <el-input v-model="add_form.if_old_major"></el-input>

                </el-form-item>



                <el-form-item label="remark" prop="remark">

                        <el-input v-model="add_form.remark"></el-input>

                </el-form-item>



                <el-form-item label="old_school" prop="old_school">

                        <el-input v-model="add_form.old_school"></el-input>

                </el-form-item>



                <el-form-item label="id" prop="id">

                        <el-input v-model="add_form.id"></el-input>

                </el-form-item>



                <el-form-item label="apply_time" prop="apply_time">

                        <el-input v-model="add_form.apply_time"></el-input>

                </el-form-item>



                <el-form-item label="source" prop="source">

                        <el-input v-model="add_form.source"></el-input>

                </el-form-item>



                <el-form-item label="due_year" prop="due_year">

                        <el-input v-model="add_form.due_year"></el-input>

                </el-form-item>



                <el-form-item label="author" prop="author">

                        <el-input v-model="add_form.author"></el-input>

                </el-form-item>



                <el-form-item label="extend" prop="extend">

                        <el-input v-model="add_form.extend"></el-input>

                </el-form-item>



                <el-form-item label="study_status" prop="study_status">

                        <el-input v-model="add_form.study_status"></el-input>

                </el-form-item>



                <el-form-item label="sex" prop="sex">

                        <el-input v-model="add_form.sex"></el-input>

                </el-form-item>



                <el-form-item label="update_time" prop="update_time">

                        <el-input v-model="add_form.update_time"></el-input>

                </el-form-item>



                <el-form-item label="name" prop="name">

                        <el-input v-model="add_form.name"></el-input>

                </el-form-item>



                <el-form-item label="qq_group" prop="qq_group">

                        <el-input v-model="add_form.qq_group"></el-input>

                </el-form-item>



                <el-form-item label="create_time" prop="create_time">

                        <el-input v-model="add_form.create_time"></el-input>

                </el-form-item>



                <el-form-item label="qq" prop="qq">

                        <el-input v-model="add_form.qq"></el-input>

                </el-form-item>



                <el-form-item label="old_major" prop="old_major">

                        <el-input v-model="add_form.old_major"></el-input>

                </el-form-item>



                <el-form-item label="adviser" prop="adviser">

                        <el-input v-model="add_form.adviser"></el-input>

                </el-form-item>



                <el-form-item label="status" prop="status">

                        <el-input v-model="add_form.status"></el-input>

                </el-form-item>



                <el-form-item label="background" prop="background">

                        <el-input v-model="add_form.background"></el-input>

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



                <el-form-item label="if_old_major" prop="if_old_major">

                    <el-input v-model="edit_form.if_old_major"></el-input>

                </el-form-item>



                <el-form-item label="remark" prop="remark">

                    <el-input v-model="edit_form.remark"></el-input>

                </el-form-item>



                <el-form-item label="old_school" prop="old_school">

                    <el-input v-model="edit_form.old_school"></el-input>

                </el-form-item>



                <el-form-item label="id" prop="id">

                    <el-input v-model="edit_form.id"></el-input>

                </el-form-item>



                <el-form-item label="apply_time" prop="apply_time">

                    <el-input v-model="edit_form.apply_time"></el-input>

                </el-form-item>



                <el-form-item label="source" prop="source">

                    <el-input v-model="edit_form.source"></el-input>

                </el-form-item>



                <el-form-item label="due_year" prop="due_year">

                    <el-input v-model="edit_form.due_year"></el-input>

                </el-form-item>



                <el-form-item label="author" prop="author">

                    <el-input v-model="edit_form.author"></el-input>

                </el-form-item>



                <el-form-item label="extend" prop="extend">

                    <el-input v-model="edit_form.extend"></el-input>

                </el-form-item>



                <el-form-item label="study_status" prop="study_status">

                    <el-input v-model="edit_form.study_status"></el-input>

                </el-form-item>



                <el-form-item label="sex" prop="sex">

                    <el-input v-model="edit_form.sex"></el-input>

                </el-form-item>



                <el-form-item label="update_time" prop="update_time">

                    <el-input v-model="edit_form.update_time"></el-input>

                </el-form-item>



                <el-form-item label="name" prop="name">

                    <el-input v-model="edit_form.name"></el-input>

                </el-form-item>



                <el-form-item label="qq_group" prop="qq_group">

                    <el-input v-model="edit_form.qq_group"></el-input>

                </el-form-item>



                <el-form-item label="create_time" prop="create_time">

                    <el-input v-model="edit_form.create_time"></el-input>

                </el-form-item>



                <el-form-item label="qq" prop="qq">

                    <el-input v-model="edit_form.qq"></el-input>

                </el-form-item>



                <el-form-item label="old_major" prop="old_major">

                    <el-input v-model="edit_form.old_major"></el-input>

                </el-form-item>



                <el-form-item label="adviser" prop="adviser">

                    <el-input v-model="edit_form.adviser"></el-input>

                </el-form-item>



                <el-form-item label="status" prop="status">

                    <el-input v-model="edit_form.status"></el-input>

                </el-form-item>



                <el-form-item label="background" prop="background">

                    <el-input v-model="edit_form.background"></el-input>

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

        name: 'student',
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

                        if_old_major:'',
                        remark:'',
                        old_school:'',
                        id:'',
                        apply_time:'',
                        source:'',
                        due_year:'',
                        author:'',
                        extend:'',
                        study_status:'',
                        sex:'',
                        update_time:'',
                        name:'',
                        qq_group:'',
                        create_time:'',
                        qq:'',
                        old_major:'',
                        adviser:'',
                        status:'',
                        background:'',
                    },
                edit_form: {
                    visible:false,

                    if_old_major:'',
                    remark:'',
                    old_school:'',
                    id:'',
                    apply_time:'',
                    source:'',
                    due_year:'',
                    author:'',
                    extend:'',
                    study_status:'',
                    sex:'',
                    update_time:'',
                    name:'',
                    qq_group:'',
                    create_time:'',
                    qq:'',
                    old_major:'',
                    adviser:'',
                    status:'',
                    background:'',
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
            open_edit(data) {
                this.edit_form = {
                    visible:true,

                    if_old_major:data.if_old_major,
                    remark:data.remark,
                    old_school:data.old_school,
                    id:data.id,
                    apply_time:data.apply_time,
                    source:data.source,
                    due_year:data.due_year,
                    author:data.author,
                    extend:data.extend,
                    study_status:data.study_status,
                    sex:data.sex,
                    update_time:data.update_time,
                    name:data.name,
                    qq_group:data.qq_group,
                    create_time:data.create_time,
                    qq:data.qq,
                    old_major:data.old_major,
                    adviser:data.adviser,
                    status:data.status,
                    background:data.background,
                }
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
            async add() {

                try {
                    await this.su_validate('add_form')
                    var add_form = this.add_form
                    var response = await request.post('/v1/api/student/', add_form)
                    this.add_form.visible = false
                    this.$message({
                        type: 'success',
                        message: '添加数据成功'
                    });
                    this.fetch()
                } catch (e) {
                    this.$message({
                        type: 'error',
                        message: e.error
                    });
                }

            },
            async remove(data) {

                try {
                    await this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
                        confirmButtonText: '确定',
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
            async edit() {
                try {
                    await this.su_validate('edit_form')
                    var edit_form = this.edit_form
                    var id = edit_form.id
                    this.$message({
                        type: 'success',
                        message: '修改信息成功!'
                    });
                    var response = await request.put('/v1/api/student/' + id + '/', edit_form)
                    this.edit_form.visible = false
                    this.fetch()
                } catch (e) {
                    this.$message({
                        type: 'error',
                        message: e.error
                    });
                }
            }
        },
        mounted() {
            this.fetch()
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

</style>
