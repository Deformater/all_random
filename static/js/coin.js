const host = 'https://api.randomall.tk'
let flipCoinButton = document.getElementById('flip_coin_btn')
flipCoinButton.onclick = async function (){
    const url = host + '/coin'

    try {
        const response = await fetch(url, {
            method: 'GET',
        })
        let data = await response.json()
        let coin = data.coin

        let text_center = document.getElementById('coin_text')

        if (coin)
            text_center.innerHTML = 'ОРЁЛ'
        else
            text_center.innerHTML = 'РЕШКА'
    }
    catch (error) {
        console.error('Ошибка:', error)
    }
}