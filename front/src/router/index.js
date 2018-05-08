import Vue from 'vue'
import Router from 'vue-router'


import order from '../components/order.vue'

import student from '../components/student.vue'

import teacher from '../components/teacher.vue'



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
            path: '/teacher',
            name: '/teacher',
            component: teacher
        },

    ]
})
