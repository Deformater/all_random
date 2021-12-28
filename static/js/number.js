const host = 'https://api.randomall.tk'
let numberButton = document.getElementById('generate_number_btn')
numberButton.onclick = async function (){
    let from = document.getElementById('input_from')
    let to = document.getElementById('input_to')

    const url = host + `/number?from_=${from.value}&to_=${to.value}`

    try {
        // const response = await fetch(url, {
        //     method: 'GET',
        // })
        // let data = response.json()
        // let number = data['number']
        let number = 31
        let text = document.getElementById('print_number')
        text.innerHTML = number + ''
    }
    catch (error) {
        console.error('Ошибка:', error)
    }
}