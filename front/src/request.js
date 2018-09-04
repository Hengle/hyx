import request from 'axios'
import qs from 'qs'
import {app} from './main'
request.defaults.baseURL = 'http://nework-web.rdc.waibaodashi.com/'
request.defaults.withCredentials = true
request.interceptors.request.use(req=> {
    if(/template/.test(req.url)){
      return req
    }

    if(/qiniu/.test(req.url)){
      return req
    }

    let data = req.data
    for (let key in data){

      if(!data[key]){
        delete data[key]
      }
    }

    // if(!req.data.nocross){
    //   req.headers.withCredentials = true
    // }

    req.data = qs.stringify(data)


    return req;
  }, function (error) {
    vue.$message.error(error)
},error=>{
  app.$message.error(error)
});

request.interceptors.response.use(res=>{
  let {code,desc} = res.data

  if(code !== 200){
    app.$message.error(desc)
  }
  if(code === 501){
    app.$router.push('/login')
	  return res
  }

  return res

},error => {
  app.$message.error(error)
})

export default request
