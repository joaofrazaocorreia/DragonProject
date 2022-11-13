# **Autoria:**

### **O trabalho foi realizado pelo grupo:**

- João Correia a22202506
- Miguel Almeida a22103547
 
Embora seja um trabalho de grupos, este projeto foi inteiramente programado e compilado por João Correia, visto que Miguel Almeida é um aluno de um ano anterior, tendo apenas conhecimentos de C: e não tendo acesso ao Visual Studio.

Por outras palavras, todo o trabalho e todos os commits são da autoria de João Correia.

### **Repositório do projeto:**

- ##### [https://github.com/joaofrazaocorreia/DragonProject](https://github.com/joaofrazaocorreia/DragonProject)

# **Arquitetura da Solução**

### **O Jogo**

O jogo consiste num loop de batalha entre 4 personagens aliados controlados pelo jogador e 4 personagens inimigos que atacam de forma aleatória. No início de cada ronda, todos os personagens vivos rolam iniciativa, e a ordem de ataque é determinada do maior roll para o menor. Em caso de empate, o personagem com maior Initiative joga primeiro.

Durante os turnos dos personagens aliados, o jogador pode escolher entre "Attack" e "Magic", em que a primeira opção utiliza os stats de Weapon Power (WP) do personagem e os Armour Points (AP) do inimigo que foi escolhido para ser atacado, e a segunda opção gasta Mana Points (MP) para curar, atacar, ou afetar os stats de um personagem à escolha.
 
O jogo acaba quando todos os personagens de uma das equipas forem derrotados. Se todos os inimigos forem derrotados, o jogador vence, mas se todos os aliados forem derrotados, o jogador perde.

### **O Código**

O código foi organizado em secções, divididas por comentários de linhas, para facilitar a procura de certas partes do código quando necessário. 

A primeira secção contém os arrays que guardam os valores necessários para os lancamentos de dados e os que guardam os personagens e feitiços. Contém também um array que guarda os personagens que são derrotados para ajudar a verificar se um personagem se encontra vivo ou não. A segunda contém as funções de lançamento de dados, e a terceira e quarta secções contêm os stats de todos os aliados e de todos os inimigos, respetivamente.

A quinta secção contém os Battle Values, ou seja, funções que são usadas durante o jogo para determinar como decorre a batalha. Esta secção contém funções que: Calculam a iniciativa, rolando um dado de 20 lados e adicionando o stat de iniciativa do respetivo personagem; Permitem ao jogador escolher um personagem-alvo ou um feitiço, recebendo um input do jogador e passando-o para o código; Calculam o dano de um ataque ou de um feitiço, utilizando os stats e os cálculos próprios para cada personagem e cada feitiço;  Aplicam o dano calculado aos stats do alvo; E funções que mostram ao jogador o estado da batalha, como o HP e o MP dos personagens.

A sexta secção contém a fase de iniciativa, que é uma função executada ao início de cada ronda para determinar a ordem dos turnos dos personagens com base nos valores rolados por cada um. Quanto maior o valor rodado, mais acima na ordem o personagem é colocado.

A sétima secção contém a fase de ataque, que ocorre durante os turnos dos personagens aliados, permitindo ao jogador controlar um personagem e atacar/usar magia com os stats deste. Esta fase é exclusivamente usada por personagens aliados.

A oitava secção contém a fase de ataque inimiga, que funciona como a secção anterior, exceto que os alvos são escolhidos aleatóriamente. Esta fase é usada exclusivamente por personagens inimigos.

Por fim, a última secção contém o Game Loop, que faz com que o jogo continue até a condição de vitória ou de derrota serem alcançadas, fazendo uso das funções das secções anteriores durante cada ronda e cada turno.


# **Referências**

Todo o código foi compilado por inspiração própria, seguindo sempre a estrutura pedida no enunciado do exercício, e guiei-me pela minha própria experiência com jogos que usam um sistema de turnos para estruturar o combate e o jogo em sí.

Contudo, troquei algumas ideias com alguns colegas durante e após as aulas, que me levaram a modificar certos aspetos. Um colega explicou que estava a usar a função .lower() nos inputs para facilitar o seu reconhecimento no código, eliminando o facto de muitos inputs serem Case-Sensitive (ou seja, precisarem de ser *exatamente* iguais às opções dadas para que o código os reconhecesse), o que me levou a implementar um sistema parecido para as funções chooseEnemy/Ally/Spell(), visto que a ideia me interessou bastante e me poupou bastante tempo.

Outro colega apontou que tinha demasiado código repetido durante as fases de ataque com magia, e sugeriu que usasse uma função para tratar deste aspeto - o que me levou a implementar o castSpell(), para incluir todos os diferentes feitiços em apenas uma função que chama as outras funções relativas a feitiços conforme necessário.

Mas, para além das ideias mencionadas acima, as restantes são de inspiração própria, tendo escrito novas funções conforme necessário para impedir grandes repetições de código e para facilitar a execução do mesmo.
