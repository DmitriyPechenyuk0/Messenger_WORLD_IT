let passwordEye = document.getElementById("password-eye")
let passwordInput = document.getElementById('id_password')

let ConfirmationpasswordEye = document.getElementById("confirmation-password-eye")
let ConfirmationpasswordInput = document.getElementById('id_confirm_password')


passwordEye.addEventListener('click', () => {
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
    } else {
        passwordInput.type = 'password';
    }
})
ConfirmationpasswordEye.addEventListener('click', () => {
    if (ConfirmationpasswordInput.type === 'password') {
        ConfirmationpasswordInput.type = 'text';
    } else {
        ConfirmationpasswordInput.type = 'password';
    }
})