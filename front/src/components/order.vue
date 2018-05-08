<template>
    <div class="teacher">

        <el-breadcrumb separator="/">
            <el-breadcrumb-item :to="{ path: '/school_list' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>order</el-breadcrumb-item>

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

            
            
            <el-table-column prop="student_name" label="student_name"></el-table-column>
            
            
            
            <el-table-column prop="order_style" label="order_style"></el-table-column>
            
            
            
            <el-table-column prop="update_time" label="update_time"></el-table-column>
            
            
            
            <el-table-column prop="id" label="id"></el-table-column>
            
            
            
            <el-table-column prop="create_time" label="create_time"></el-table-column>
            
            
            
            <el-table-column prop="target_school" label="target_school"></el-table-column>
            
            
            
            <el-table-column prop="target_major" label="target_major"></el-table-column>
            
            

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

                
                
                <el-form-item label="student_name" prop="student_name">
                    
                        <el-input v-model="add_form.student_name"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="order_style" prop="order_style">
                    
                        <el-input v-model="add_form.order_style"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="update_time" prop="update_time">
                    
                        <el-input v-model="add_form.update_time"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="id" prop="id">
                    
                        <el-input v-model="add_form.id"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="create_time" prop="create_time">
                    
                        <el-input v-model="add_form.create_time"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="target_school" prop="target_school">
                    
                        <el-input v-model="add_form.target_school"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="target_major" prop="target_major">
                    
                        <el-input v-model="add_form.target_major"></el-input>
                    
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

                
                
                <el-form-item label="student_name" prop="student_name">
                    
                    <el-input v-model="edit_form.student_name"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="order_style" prop="order_style">
                    
                    <el-input v-model="edit_form.order_style"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="update_time" prop="update_time">
                    
                    <el-input v-model="edit_form.update_time"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="id" prop="id">
                    
                    <el-input v-model="edit_form.id"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="create_time" prop="create_time">
                    
                    <el-input v-model="edit_form.create_time"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="target_school" prop="target_school">
                    
                    <el-input v-model="edit_form.target_school"></el-input>
                    
                </el-form-item>
                
                
                
                <el-form-item label="target_major" prop="target_major">
                    
                    <el-input v-model="edit_form.target_major"></el-input>
                    
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

        name: 'order',
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
                    
                        student_name:'',
                        order_style:'',
                        update_time:'',
                        id:'',
                        create_time:'',
                        target_school:'',
                        target_major:'',
                    },
                edit_form: {
                    visible:false,
                
                    student_name:'',
                    order_style:'',
                    update_time:'',
                    id:'',
                    create_time:'',
                    target_school:'',
                    target_major:'',
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
                
                    student_name:data.student_name,
                    order_style:data.order_style,
                    update_time:data.update_time,
                    id:data.id,
                    create_time:data.create_time,
                    target_school:data.target_school,
                    target_major:data.target_major,
                }
            },
            async fetch() {

                var page_size = this.page_size,
                    page_num = this.page_num,
                    search = this.search,
                    that = this
                this.loading = true
                var response = await request.get('http://localhost:8000/v1/api/order/', {
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
                    var response = await request.post('http://localhost:8000/v1/api/order/', add_form)
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
                    var response = await request.delete('http://localhost:8000/v1/api/order/' + data.id + '/')

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
                    var response = await request.put('http://localhost:8000/v1/api/order/' + id + '/', edit_form)
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
