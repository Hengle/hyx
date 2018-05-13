import Vue from 'vue'
import Router from 'vue-router'


import order from '../components/order.vue'

import student from '../components/student.vue'

import teacher from '../components/teacher.vue'
import stuItem from '../components/student-item'
import teaItem from '../components/teacher-item'
import teacher_upload  from '../components/teacher-upload'
import student_upload  from '../components/student-upload'
Vue.use(Router)

export default new Router({
    routes: [

          {
            path: '/',
            name: '/student',
            component: student
        },

        {
            path: '/student',
            name: '/student',
            component: student
        },

      {
            path: '/sitem',
            name: '/sitem',
            component: stuItem
        },

        {
            path: '/stuUpload',
            name: '/stuUpload',
            component: student_upload
        },


         {
            path: '/teaItem',
            name: '/teaItem',
            component: teaItem
        },

        {
            path: '/teacher',
            name: '/teacher',
            component: teacher
        },

         {
            path: '/teaUpload',
            name: '/teaUpload',
            component: teacher_upload
        },

    ]
})
