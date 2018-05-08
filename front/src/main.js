// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'

Vue.config.productionTip = false
import ElementUI from 'element-ui'
import './theme2/index.css'
/* eslint-disable no-new */
import router from './router'
Vue.use(ElementUI)
new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
})
