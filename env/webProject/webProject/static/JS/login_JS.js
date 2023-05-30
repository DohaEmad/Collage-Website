/*
this function cann't login to the home page because django can run inside this page to change the html path 
function LoginValidation(form) {

    let Pass = document.getElementById("pass").value;
    let User = document.getElementById("user").value;

    if ((User !== 'Nourhan') || (Pass !== '12345')) {
        alert('Invalid Password or Invalid Username!!');
        return false;
    } else {
        form.action = "pages/home_page.html";

        return false;

    }

} */