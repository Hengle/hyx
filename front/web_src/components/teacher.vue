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

            
            
            <el-table-column prop="first_rank" label="first_rank"></el-table-column>
            
            
            
            <el-table-column prop="final_rank" label="final_rank"></el-table-column>
            
            
            
            <el-table-column prop="remark" label="remark"></el-table-column>
            
            
            
            <el-table-column prop="bank_number" label="bank_number"></el-table-column>
            
            
            
            <el-table-column prop="other_salary" label="other_salary"></el-table-column>
            
            
            
            <el-table-column prop="bachelor_school" label="bachelor_school"></el-table-column>
            
            
            
            <el-table-column prop="if_pass_direct" label="if_pass_direct"></el-table-column>
            
            
            
            <el-table-column prop="now_major" label="now_major"></el-table-column>
            
            
            
            <el-table-column prop="extend" label="extend"></el-table-column>
            
            
            
            <el-table-column prop="professional_salary" label="professional_salary"></el-table-column>
            
            
            
            <el-table-column prop="bachelor_major" label="bachelor_major"></el-table-column>
            
            
            
            <el-table-column prop="name" label="name"></el-table-column>
            
            
            
            <el-table-column prop="create_time" label="create_time"></el-table-column>
            
            
            
            <el-table-column prop="guide_type" label="guide_type"></el-table-column>
            
            
            
            <el-table-column prop="now_school" label="now_school"></el-table-column>
            
            
            
            <el-table-column prop="birth_date" label="birth_date"></el-table-column>
            
            
            
            <el-table-column prop="one_to_one_salary" label="one_to_one_salary"></el-table-column>
            
            
            
            <el-table-column prop="course" label="course"></el-table-column>
            
            
            
            <el-table-column prop="id" label="id"></el-table-column>
            
            
            
            <el-table-column prop="job" label="job"></el-table-column>
            
            
            
            <el-table-column prop="grade_year" label="grade_year"></el-table-column>
            
            
            
            <el-table-column prop="open_class_salary" label="open_class_salary"></el-table-column>
            
            
            
            <el-table-column prop="qq_group" label="qq_group"></el-table-column>
            
            
            
            <el-table-column prop="sex" label="sex"></el-table-column>
            
            
            
            <el-table-column prop="update_time" label="update_time"></el-table-column>
            
            
            
            <el-table-column prop="english_class_score" label="english_class_score"></el-table-column>
            
            
            
            <el-table-column prop="bank_name" label="bank_name"></el-table-column>
            
            
            
            <el-table-column prop="qq" label="qq"></el-table-column>
            
            
            
            <el-table-column prop="politic_class_score" label="politic_class_score"></el-table-column>
            
            
            
            <el-table-column prop="bank_branch" label="bank_branch"></el-table-column>
            
            
            
            <el-table-column prop="mobile" label="mobile"></el-table-column>
            
            

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

                
                
                <el-form-item label="first_rank" prop="first_rank">
                    
                        <el-input v-model="add_form.first_rank"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="final_rank" prop="final_rank">
                    
                        <el-input v-model="add_form.final_rank"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="remark" prop="remark">
                    
                        <el-input v-model="add_form.remark"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="bank_number" prop="bank_number">
                    
                        <el-input v-model="add_form.bank_number"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="other_salary" prop="other_salary">
                    
                        <el-input v-model="add_form.other_salary"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="bachelor_school" prop="bachelor_school">
                    
                        <el-input v-model="add_form.bachelor_school"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="if_pass_direct" prop="if_pass_direct">
                    
                        <el-input v-model="add_form.if_pass_direct"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="now_major" prop="now_major">
                    
                        <el-input v-model="add_form.now_major"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="extend" prop="extend">
                    
                        <el-input v-model="add_form.extend"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="professional_salary" prop="professional_salary">
                    
                        <el-input v-model="add_form.professional_salary"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="bachelor_major" prop="bachelor_major">
                    
                        <el-input v-model="add_form.bachelor_major"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="name" prop="name">
                    
                        <el-input v-model="add_form.name"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="create_time" prop="create_time">
                    
                        <el-input v-model="add_form.create_time"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="guide_type" prop="guide_type">
                    
                        <el-input v-model="add_form.guide_type"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="now_school" prop="now_school">
                    
                        <el-input v-model="add_form.now_school"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="birth_date" prop="birth_date">
                    
                        <el-input v-model="add_form.birth_date"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="one_to_one_salary" prop="one_to_one_salary">
                    
                        <el-input v-model="add_form.one_to_one_salary"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="course" prop="course">
                    
                        <el-input v-model="add_form.course"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="id" prop="id">
                    
                        <el-input v-model="add_form.id"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="job" prop="job">
                    
                        <el-input v-model="add_form.job"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="grade_year" prop="grade_year">
                    
                        <el-input v-model="add_form.grade_year"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="open_class_salary" prop="open_class_salary">
                    
                        <el-input v-model="add_form.open_class_salary"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="qq_group" prop="qq_group">
                    
                        <el-input v-model="add_form.qq_group"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="sex" prop="sex">
                    
                        <el-input v-model="add_form.sex"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="update_time" prop="update_time">
                    
                        <el-input v-model="add_form.update_time"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="english_class_score" prop="english_class_score">
                    
                        <el-input v-model="add_form.english_class_score"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="bank_name" prop="bank_name">
                    
                        <el-input v-model="add_form.bank_name"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="qq" prop="qq">
                    
                        <el-input v-model="add_form.qq"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="politic_class_score" prop="politic_class_score">
                    
                        <el-input v-model="add_form.politic_class_score"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="bank_branch" prop="bank_branch">
                    
                        <el-input v-model="add_form.bank_branch"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="mobile" prop="mobile">
                    
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

                
                
                <el-form-item label="first_rank" prop="first_rank">
                    
                    <el-input v-model="edit_form.first_rank"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="final_rank" prop="final_rank">
                    
                    <el-input v-model="edit_form.final_rank"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="remark" prop="remark">
                    
                    <el-input v-model="edit_form.remark"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="bank_number" prop="bank_number">
                    
                    <el-input v-model="edit_form.bank_number"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="other_salary" prop="other_salary">
                    
                    <el-input v-model="edit_form.other_salary"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="bachelor_school" prop="bachelor_school">
                    
                    <el-input v-model="edit_form.bachelor_school"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="if_pass_direct" prop="if_pass_direct">
                    
                    <el-input v-model="edit_form.if_pass_direct"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="now_major" prop="now_major">
                    
                    <el-input v-model="edit_form.now_major"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="extend" prop="extend">
                    
                    <el-input v-model="edit_form.extend"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="professional_salary" prop="professional_salary">
                    
                    <el-input v-model="edit_form.professional_salary"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="bachelor_major" prop="bachelor_major">
                    
                    <el-input v-model="edit_form.bachelor_major"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="name" prop="name">
                    
                    <el-input v-model="edit_form.name"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="create_time" prop="create_time">
                    
                    <el-input v-model="edit_form.create_time"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="guide_type" prop="guide_type">
                    
                    <el-input v-model="edit_form.guide_type"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="now_school" prop="now_school">
                    
                    <el-input v-model="edit_form.now_school"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="birth_date" prop="birth_date">
                    
                    <el-input v-model="edit_form.birth_date"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="one_to_one_salary" prop="one_to_one_salary">
                    
                    <el-input v-model="edit_form.one_to_one_salary"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="course" prop="course">
                    
                    <el-input v-model="edit_form.course"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="id" prop="id">
                    
                    <el-input v-model="edit_form.id"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="job" prop="job">
                    
                    <el-input v-model="edit_form.job"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="grade_year" prop="grade_year">
                    
                    <el-input v-model="edit_form.grade_year"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="open_class_salary" prop="open_class_salary">
                    
                    <el-input v-model="edit_form.open_class_salary"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="qq_group" prop="qq_group">
                    
                    <el-input v-model="edit_form.qq_group"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="sex" prop="sex">
                    
                    <el-input v-model="edit_form.sex"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="update_time" prop="update_time">
                    
                    <el-input v-model="edit_form.update_time"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="english_class_score" prop="english_class_score">
                    
                    <el-input v-model="edit_form.english_class_score"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="bank_name" prop="bank_name">
                    
                    <el-input v-model="edit_form.bank_name"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="qq" prop="qq">
                    
                    <el-input v-model="edit_form.qq"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="politic_class_score" prop="politic_class_score">
                    
                    <el-input v-model="edit_form.politic_class_score"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="bank_branch" prop="bank_branch">
                    
                    <el-input v-model="edit_form.bank_branch"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="mobile" prop="mobile">
                    
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
                    
                        first_rank:'',
                        final_rank:'',
                        remark:'',
                        bank_number:'',
                        other_salary:'',
                        bachelor_school:'',
                        if_pass_direct:'',
                        now_major:'',
                        extend:'',
                        professional_salary:'',
                        bachelor_major:'',
                        name:'',
                        create_time:'',
                        guide_type:'',
                        now_school:'',
                        birth_date:'',
                        one_to_one_salary:'',
                        course:'',
                        id:'',
                        job:'',
                        grade_year:'',
                        open_class_salary:'',
                        qq_group:'',
                        sex:'',
                        update_time:'',
                        english_class_score:'',
                        bank_name:'',
                        qq:'',
                        politic_class_score:'',
                        bank_branch:'',
                        mobile:'',
                    },
                edit_form: {
                    visible:false,
                
                    first_rank:'',
                    final_rank:'',
                    remark:'',
                    bank_number:'',
                    other_salary:'',
                    bachelor_school:'',
                    if_pass_direct:'',
                    now_major:'',
                    extend:'',
                    professional_salary:'',
                    bachelor_major:'',
                    name:'',
                    create_time:'',
                    guide_type:'',
                    now_school:'',
                    birth_date:'',
                    one_to_one_salary:'',
                    course:'',
                    id:'',
                    job:'',
                    grade_year:'',
                    open_class_salary:'',
                    qq_group:'',
                    sex:'',
                    update_time:'',
                    english_class_score:'',
                    bank_name:'',
                    qq:'',
                    politic_class_score:'',
                    bank_branch:'',
                    mobile:'',
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
                
                    first_rank:data.first_rank,
                    final_rank:data.final_rank,
                    remark:data.remark,
                    bank_number:data.bank_number,
                    other_salary:data.other_salary,
                    bachelor_school:data.bachelor_school,
                    if_pass_direct:data.if_pass_direct,
                    now_major:data.now_major,
                    extend:data.extend,
                    professional_salary:data.professional_salary,
                    bachelor_major:data.bachelor_major,
                    name:data.name,
                    create_time:data.create_time,
                    guide_type:data.guide_type,
                    now_school:data.now_school,
                    birth_date:data.birth_date,
                    one_to_one_salary:data.one_to_one_salary,
                    course:data.course,
                    id:data.id,
                    job:data.job,
                    grade_year:data.grade_year,
                    open_class_salary:data.open_class_salary,
                    qq_group:data.qq_group,
                    sex:data.sex,
                    update_time:data.update_time,
                    english_class_score:data.english_class_score,
                    bank_name:data.bank_name,
                    qq:data.qq,
                    politic_class_score:data.politic_class_score,
                    bank_branch:data.bank_branch,
                    mobile:data.mobile,
                }
            },
            async fetch() {

                var page_size = this.page_size,
                    page_num = this.page_num,
                    search = this.search,
                    that = this
                this.loading = true
                var response = await request.get('http://localhost:8000/v1/api/teacher/', {
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
                    var response = await request.post('http://localhost:8000/v1/api/teacher/', add_form)
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
                    var response = await request.delete('http://localhost:8000/v1/api/teacher/' + data.id + '/')

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
                    var response = await request.put('http://localhost:8000/v1/api/teacher/' + id + '/', edit_form)
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
