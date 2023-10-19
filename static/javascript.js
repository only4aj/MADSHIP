const checkRegister = () => {
    let username = document.getElementById('username').value
    let email = document.getElementById('email').value
    let phoneNumber = document.getElementById('phone').value
    let password = document.getElementById('pass').value
    
    if( username == '' || email == '' || phoneNumber == '' || password == ''){
        alert("Fill all details!")
    }
}

const checkLogin = () =>{
    let username = document.getElementById('uname').value
    let password = document.getElementById('password').value
    if(username == '' || password == ''){
        alert("Fill all details!")
    }
}
