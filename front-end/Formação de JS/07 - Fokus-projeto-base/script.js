const html = document.querySelector('html')
const focoBt = document.querySelector('.app__card-button--foco')
const curtoBt = document.querySelector('.app__card-button--curto')
const longoBt = document.querySelector('.app__card-button--longo')
const banner = document.querySelector('.app__image')
const titulo = document.querySelector('.app__title')
const botoes = document.querySelectorAll('.app__card-button')
const musicaFocoInput = document.querySelector('#alternar-musica')
const musica = new Audio('/sons/luna-rise-part-one.mp3')
musica.loop=true

musicaFocoInput.addEventListener('change', () => {
    if (musica.paused) {
        musica.play()
    } else {
        musica.pause()
    }
})
focoBt.addEventListener('click', () => { // '() =>' é uma arrow function 
    alterarContexto('foco')
    focoBt.classList.add('active')
})

curtoBt.addEventListener('click', () => {
    alterarContexto('descanso-curto')
    curtoBt.classList.add('active')
})

longoBt.addEventListener('click', () => {
    alterarContexto('descanso-longo')
    longoBt.classList.add('active')
})

//MUDANDO A FOTO E COR DE FUNDO DOS MODOS DE CONTEXTO
function alterarContexto (contexto) {
    botoes.forEach(function (contexto){ // Neste trecho de código, a função alterarContexto percorre todos os botões e remove a classe "active" de cada um deles, garantindo que apenas um botão fique ativo por vez.
        contexto.classList.remove('active')
    })
    html.setAttribute('data-contexto', contexto)// primeiro parametro é onde vc quer mexer (no 'data-contexto'), o segundo é para o que você quer mudar (para 'foco')
    banner.setAttribute('src', `imagens/${contexto}.png`)

    switch (contexto) {
        case 'foco':
            titulo.innerHTML = 
            'Otimiza sua produtividade,<br> <strong class="app__title-strong">mergulhe no que importa</strong>'
            break;

        case 'descanso-curto':
            titulo.innerHTML = 
            'Que tal dar uma respirada?<br> <strong class="app__title-strong">Faça uma pausa curta</strong>'
            break;
        case 'descanso-longo':
            titulo.innerHTML = 'Hora de voltar à superfície<br> <strong class="app__title-strong">Faça uma pausa longa</strong>'
        default: 
            break;
    }
}

