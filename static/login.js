function login_api(){
    var input=document.getElementById('text');
    var password=document.getElementById('password');
    var fromdata=new FormData();
    fromdata.append('username',input.value);
    fromdata.append('password',password.value);
    fetch('/login_api',{method:'POST',body:fromdata})
    .then(response=>{return response.json()})
    .then(data=>{
        if(data['errno']==0){
            alert("登录成功")
            window.location.href='/list';
        }
        else{
            alert("登录失败")
        }

        console.log('上传成功',data)})
    .catch(error=>{console.log('上传失败',error)})
}