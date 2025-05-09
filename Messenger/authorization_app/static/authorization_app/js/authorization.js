let passwordEye = document.getElementById("password-eye")
let passwordInput = document.getElementById('id_password')

passwordEye.addEventListener('click', () => {
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
    } else {
        passwordInput.type = 'password';
    }
})