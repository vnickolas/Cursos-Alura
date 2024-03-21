

function tocaSom (idElementoAudio) {

    document.querySelector(idElementoAudio).play()

}

    const listaDeTeclas = document.querySelectorAll('.tecla') //seleciona toda class 'tecla'
    let contador = 0; //determina que a variavel 'contador' tenha seu número incial como '0'
        while (contador < listaDeTeclas.length) { //enquanto o 'contador' for menor que a quantidade do número de teclas (9), o scrip fará... (função abaixo)

            let tecla = listaDeTeclas[contador]; //define que a varialvel 'tecla' puxe a lista de teclas (e entre chaves, seu indíce selecionado), e que sejam uma variavel só

            const instrumento = tecla.classList[1]; //define uma variavel constante para que puxe o índice 1 (2º nome) da "sequencia" de classes denominadas em uma tag ex: (input class= 'recheio massa bolo'), então, o 'instrumento' puxará o índice 1 que é a 'massa'

            const idAudio = `#som_${instrumento}` // define uma variavel constante onde mostrará o valor '#som_' + qual a classe que o instrumento está puxando. ex: se o instrumento está puxando 'massa', logo, o idAudio é '#som_massa'

            tecla.onclick = function(){
                tocaSom(idAudio); //colocamos o idAudio para ele puxar qual o nome exato da class que será tocada. Além disso, como estamos puxando a função 'tomaSom' lá de cima, colocamos entre os paranteses o 'idAudio' como parametro

            } //coloquei o 'contador' entre as chaves pois quero que ele valha cada vez uma coisa, conforme colocamos para o 'contador' mudar a cada loop na seguinte adição:
            contador = contador + 1;
        }