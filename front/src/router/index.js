import Vue from 'vue'
import Router from 'vue-router'


import order from '../components/order.vue'

import student from '../components/student.vue'

import teacher from '../components/teacher.vue'
import stuItem from '../components/student-item'
import teaItem from '../components/teacher-item'

Vue.use(Router)

export default new Router({
    routes: [

          {
            path: '/',
            name: '/student',
            component: student
        },

        {
            path: '/order',
            name: '/order',
            component: order
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
            path: '/teaItem',
            name: '/teaItem',
            component: teaItem
        },

        {
            path: '/teacher',
            name: '/teacher',
            component: teacher
        },

    ]
})
