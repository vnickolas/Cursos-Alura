function tocaSom (seletorAudio) {

  const elemento = document.querySelector(seletorAudio) //coloca a id que foi puxada lá embaixo (ex: #som_tecla_tic) dentro da variavel 'elemento'
     if (elemento && elemento.localName === 'audio') { //se essa id for igual a null E se o localName dessa ID (tagname como header/input/audio...) for igual a 'audio', ele reproduzirá a função abaixo
        elemento.play()
     }
      else {
        alert('Elemento não encontrado ou seletor inválido')
      }


}

  const listaDeTeclas = document.querySelectorAll('.tecla') //seleciona toda class 'tecla'
  
      for (let contador = 0; contador < listaDeTeclas.length; contador ++) { 
          //o LET determina que a variavel 'contador' tenha seu número incial como '0'
          //enquanto o 'contador' for menor que a quantidade do número de teclas (9), o scrip fará... (função abaixo) ASSIM, ELE 'MAPEARÁ/ESCANEARÁ' TODAS AS TECLAS
          // o CONTADOR ++ é para receber ele e icrementar +1



          let tecla = listaDeTeclas[contador]; //define que a varialvel 'tecla' acesse a lista de teclas (e entre chaves, seu indíce selecionado), e que sejam uma variavel só 
          // NO CASO, SERIA TECLA[2] (que traz a 'tecla_clap')
              console.log(`variavel ${tecla}`) // APARECE COMO: variavel [object HTMLButtonElement]
          
          const instrumento = tecla.classList[1]; //define uma variavel constante para que o 'classList' puxe o índice 1 (2º nome) da "sequencia" de classes denominadas em uma tag ex: (input class= 'recheio massa bolo'), então, o 'instrumento' puxará o índice 1 que é a 'massa'
          // NO CASO, FICARIA k
              console.log(`variavel ${instrumento}`) // APARECE COMO: variavel tecla_pom
          
          const idAudio = `#som_${instrumento}` // define uma variavel constante onde mostrará o valor '#som_' + qual a classe que o instrumento está puxando. ex: se o instrumento está puxando 'massa', logo, o idAudio é '#som_massa'
              console.log(`variavel ${idAudio}`) // APARECE COMO: variavel #som_tecla_tic
          
          tecla.onclick = function(){
              tocaSom(idAudio); //colocamos o idAudio para ele puxar qual o nome exato da class que será tocada. Além disso, como estamos puxando a função 'tomaSom' lá de cima, escrevendo o 'idAudio' entre parenteses, ele entra lá em cima como parametro também.

          } 

          tecla.onkeydown = function (event) {
            // onjeydown é quando pelo tab, a tecla do teclado está selecionada, logo...
            // ...fará tal função. Colocamos como parâmetro o 'event' para a função, pois qualquer tecla da lista de teclas que estiverem selecionadas pelo tab (focadas em amarelo), caso a tecla que a pessoa abertar seja 'Space" ou 'Enter', será adicionado uma class 'ativa' e assim, será reproduzido o efeito do css 
            if (event.code === 'Space' || event.code === 'Enter') { //o '.code' entra no "nome" da tecla apertada e como colocarmos para ver se é igual ao 'Space' ou 'Enter', ele fará a função abaixo:

              tecla.classList.add(`ativa`); //adiciona uma classe (classList) e coloca o nome da classe entre parenteses
            }
          }

          tecla.onkeyup = function () {
            // onkeyup é quando pelo tab, a tecla do teclado NÃO está selecionada
            tecla.classList.remove(`ativa`); //remove uma classe (classList) e coloca o nome da classe entre parenteses
          }
          console.log(`Variavel ${contador}`) // APARECE COMO: Variavel 0
      }