const host = 'https://api.randomall.tk'
let passButton = document.getElementById('generate_psw_btn')
passButton.onclick = async function (){
    let number_switch = document.getElementById('numbers_switch').querySelector('input')
    let spec_symbols = document.getElementById('spec_symbols_switch').querySelector('input')
    let length = document.getElementById('length_input')

    const url = host + `/password?length=${length.value}&is_number=${number_switch.checked}&is_spec_symbol=${spec_symbols.checked}`

    let pass;
    try {
        // const response = await fetch(url, {
        //     method: 'GET',
        // })
        // let data = response.json()
        // let pass = data['password']
        let psw_input = document.getElementById('psw_input')
        let safety = 100
        if (length.value <= 15)
            safety -= 50 - length.value * 3
        if (!number_switch.checked)
            safety -= 20
        if (!spec_symbols.checked)
            safety -= 20
        if (safety < 0)
            safety = 0
        if (safety > 100)
            safety = 100

        let psw_safety = document.getElementById('psw_safety_div')
        psw_safety.style.width = safety + '%'

        if (safety > 0 && safety < 40)
            psw_safety.style.background = 'red'
        if (safety >= 40 && safety < 75)
            psw_safety.style.background = 'yellow'
        if (safety >= 75 && safety <= 100)
            psw_safety.style.background = 'green'

        pass = 'alkfgalsdmka;slkg'

        psw_input.value = pass
        psw_input.select()
        document.execCommand('copy')
    } catch (error) {
        console.error('Ошибка:', error)
    }
}

let copyButton = document.getElementById('copy')
copyButton.onclick = async function (){
    let psw_input = document.getElementById('psw_input')
    psw_input.select()
    document.execCommand('copy')
}