function validateLogin(){
    var a=document.getElementById("username" ).value;
    var b=document.getElementById("password").value;
    
    if(a=="myemail@test.com" && b=="test123"){
    
    alert("success");
    return true;
    }
    else{
    
    alert("credentials wrong");
    return false;
    }
    }