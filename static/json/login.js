var token = "";

function login(){
    var param = {
        name: $(".inputText input[type=text]").val(),
        pwd: $(".inputText input[type=password]").val()
    }
    $.ajax({
        url:'http://127.0.0.1:8000/user/login',
        data:JSON.stringify(param),
        type:'post',
        contentType:false,
        processData:false,
        success:function(data){
            token = data.access_token;
            console.log(token);
            $("#login_div").fadeToggle();
            $("#td_d").fadeToggle();
            window.location.href = "./data.html"
        }
    })
}

var getData = function(){
    $("#submit").click(function(){
        console.log("登录@@@@@@")
        $.ajax({
            url:'http://127.0.0.1:8000/list',
            headers:{
                "Authorization":"Bearer "+token,
                'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            },
            type:'get',
            dataType:'json',
            contentType: 'application/json; charset=utf-8',
            success:function(data){
                var data = data.data;
                var Table = document.getElementById("td");
                for (var i=0;i<data.length;i++){
                    var tr=document.createElement("tr");

                    for (const k in data[i]){
                        var td = document.createElement("td");
                        td.innerHTML = data[i][k];
                        tr.appendChild(td);
                    }
                    Table.appendChild(tr);
                }
            },
            error:function(){
                alert("操作有误，请联系管理员....")
            },

        })
    })
}
