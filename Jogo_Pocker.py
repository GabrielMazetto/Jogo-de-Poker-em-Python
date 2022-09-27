import random


class Card:
    """Representa uma carta padrao do jogo."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Ouros', 'Espadas', 'Copas', 'Paus']
    rank_names = [None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Dama', 'Valete', 'Rei', 'As']
   
    def __str__(self):
        """Retorna uma representacao em string das cartas."""
        return '%s de %s' %(Card.rank_names[self.rank],
                            Card.suit_names[self.suit])

    def __eq__(self, other):
        """Checa se duas cartas (self e other) possuem o mesmo rank (valor).
        retorna: booleano
        """
        return self.rank == other.rank 
    
    def __lt__(self, other):
        """Compara a carta (self) com outra (other) e verifica se a primeira e menor que a segunda.
        retorna: booleano
        """
        t1 = self.rank   
        t2 = other.rank  
        return t1 < t2

    def __add__(self, other):
        """Permite a soma de duas cartas, retornando o rank total.
        retorna: inteiro
        """
        c1 = self.rank
        c2 = other.rank
        return c1 + c2

    def __sub__(self, other):
        c1 = self.rank
        c2 = other.rank
        return c1 - c2
    

class Deck:
    """Representa um deck padrao de cartas.
    Attributes:
      cards: lista de objetos Card.
    """
    def __init__(self):
        """Inicializa o Deck com 52 cartas.
        """
        self.cards = []
        for suit in range(4):
            for rank in range (1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        """Retorna uma representacao em string do Deck.
        """
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self, i=-1):
        """Remove e retorna uma carta do deck.
        i: indice da carta a ser removida; por padrao, remove a ultima carta.
        """
        return self.cards.pop(i)

    def add_card(self, card):
        """Adiciona uma carta ao deck.
        card: Card
        """
        self.cards.append(card)

    def remove_card(self, card):
        """Remove uma carta do deck.
        
        card: Card
        """
        self.cards.remove(card)

    def shuffle(self):
        """Embaralha as cartas do deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Organiza as cartas em ordem crecente."""
        self.cards.sort(reverse=True)
     
    def move_cards(self, hand, num):
        """Move o numero dado de cartas do deck para a Hand.
        hand: objeto Hand de origem das cartas
        num: numero inteiro de cartas a serem movidas
        """
        for i in range(num):
            hand.add_card(self.pop_card())

    
class Hand(Deck):
    """Representa a mao de cartas de cada jogador."""

    def __init__(self, label=''):
        """A Hand se inicializa vazia.
        """
        self.cards = [] 
        self.label = label 

    def sum_total(self):
        """Soma os valores das cartas e retorna o total.
        """
        #return self.cards.sum()
        total = 0
        for card in self.cards:
            valor = card.rank
            total = total + valor
        return total



def pegar_jogadores(n):
    """Retorna a lista de jogadores da partida.
    """
    quantidade = input("Quantos Jogadores? ")
    quantidade = int(quantidade)
    while quantidade > n or quantidade <= 1:
        quantidade = input("O numero digitado e invalido. Por favor, digite um numero entre 2 e %d: " %n)
        quantidade = int(quantidade)
    jogador = []
    print('')

    for indice in range(0, quantidade):
        nome_jogador = input('Qual o nome do jogador %d? ' %(indice+1))
        jogador.append(nome_jogador)

    return jogador    


def distribuir_cartas(n):
        """Inicializa o jogo movendo n cartas do deck para a mao de cada jogador.
        """
        hand = 0
        while hand<len(jogadores):
                baralho.move_cards(hands[hand], n)
                print('Pontuacao do jogador %s: %d' %(jogadores[hand],pontuacao[hand]))
                hand = hand+1

def dar_aposta_obrigatoria():
    """Retira da pontuacao de cada jogador participante a aopsta obrigatoria.
    """
    for indice in range(0, len(pontuacao)):
        pontuacao[indice] -= aposta_obrigatoria


def deletar():
    """Apos o termino da partida, as cartas de cada mao retornam ao deck.
    Caso o jogador nao tenha a pontuacao necessaria para participar, ele sera retirado do jogo.
    """
    for hand in hands:
        tamanho = len(hand.cards)
        hand.move_cards(baralho, tamanho)
    i = 0
    n = 0
    while n < n_jogadores:
        i_muda = True
        if pontuacao[i] <= 0 or pontuacao[i] < aposta_obrigatoria:
            del pontuacao[i]
            del hands[i]
            del jogadores[i]
            i_muda = False
        if i_muda == True:
            i += 1
        n += 1



def criar_pontuacao(n_jogadores):
        """Inicializa a pontuacao dos jogadores.
        """
        pontuacao = []
        for _ in range(0, n_jogadores):
            pontuacao.append(1000)
        return pontuacao

def criar_mao(n):
    hands = []
    for hand in range(0, n):
        hand = Hand()
        hands.append(hand)
    return hands

def is_carta_alta(hand: Hand()):
    cartas = Hand()
    for carta in hand.cards:
        cartas.add_card(carta)
        if len(cartas.cards) == 5:
            break
    return [True, cartas]

def is_par2(hand: Hand()):
    for card1 in hand.cards:
        count = 0
        cartas = Hand()
        for card2 in hand.cards:
            if card1 == card2:
                count += 1
                cartas.add_card(card1)
        if count == 2:
            for carta in hand.cards:
                if carta not in cartas.cards:
                    cartas.add_card(carta)
                if len(cartas.cards) == 5:
                    break
            return [True, cartas]
    return [False, False]


def is_trinca2(hand: Hand()):
    count = 0
    for card1 in hand.cards:
        count = 0
        cartas = Hand()
        for card2 in hand.cards:
            if card1 == card2:
                count += 1
                cartas.add_card(card1)
        if count == 3:
            for carta in hand.cards:
                if carta not in cartas.cards:
                    cartas.add_card(carta)
                if len(cartas.cards) == 5:
                    break
            return [True, cartas]
    return [False, False]
  

def is_dois_pares2(hand: Hand()):
    count = 0
    a = 0
    cartas = Hand()
    for card1 in hand.cards:
        count = 0
        for card2 in hand.cards:
            if card1 == card2:
                count += 1
        if count == 2:
            cartas.add_card(card1)
            a += 1
        if a == 4:
            break
    #é 4 pq pra cada igual par vai contar duas vezes
    if a == 4:
        for carta in hand.cards:
            if carta not in cartas.cards:
                cartas.add_card(carta)
            if len(cartas.cards) == 5:
                break
        return [True, cartas]
    else:
        return [False, False]

def is_sequencia2(hand: Hand()):
    count = 0
    cartas = Hand()
    for i in range(len(hand.cards) - 1):
        if hand.cards[i] - hand.cards[i+1] != 1:
            count = 0
        else: 
            count += 1
            cartas.add_card(hand.cards[i])
        if count >= 4:
            cartas.add_card(hand.cards[i+1])
            if len(cartas.cards) == 5:
                return [True, cartas]
    else:
        return [False, False]

def is_flush2(hand: Hand()):
    cartas = Hand()
    for card in hand.cards:
        count = 0
        for card2 in hand.cards:
            if card.suit == card2.suit:
                count += 1
                cartas.add_card(card2)
            else:
                cartas.cards = []
        if len(cartas.cards) == 5:
            return [True, cartas]
    return [False, False]

def is_full_halse2(hand: Hand()):
    cartas = Hand()
    par = is_par2(hand)
    trinca = is_trinca2(hand)
    if par[0] and trinca[0]:
        for par in par[1].cards:
            if len(cartas.cards) < 2:
                cartas.add_card(par)
        for trinca in trinca[1].cards:
            if len(cartas.cards) < 5:
                cartas.add_card(trinca)
        return [True, cartas]
    else:
        return [False, False]

def is_streith_flush2(hand: Hand()):
    cartas = Hand()
    sequencia = is_sequencia2(hand)
    if sequencia[0]:
        for i in range(len(sequencia[1].cards) - 1):
            if sequencia[1].cards[i].suit == sequencia[1].cards[i+1].suit:
                cartas.add_card(sequencia[1].cards[i])
        if len(cartas.cards) == 4:
            cartas.add_card(sequencia[1].cards[i+1])
            return [True, cartas]
    return [False, False]

def is_quadra2(hand: Hand()):
    count = 0
    for card1 in hand.cards:
        count = 0
        cartas = Hand()
        for card2 in hand.cards:
            if card1 == card2:
                count += 1
                cartas.add_card(card1)
        if count == 4:
            for carta in hand.cards:
                if carta not in cartas.cards:
                    cartas.add_card(carta)
                if len(cartas.cards) == 5:
                    break
            return [True, cartas]
    return [False, False]

def is_royalt_flush2(hand: Hand()):
    cartas = Hand()
    flush = is_flush2(hand)
    if flush[0] and flush[1].sum_total() == 60:
        flush[1].move_cards(cartas, 5)
        return [True, cartas]
    else:
        return [False, False]
    

def quem_ganhou(lista):
    valores = []
    ganhadores = []
    cartas = [0, 0, 0, 0, 0, 0]
    maos = ['Carta Alta', 'Um Par', 'Trinca', 'Dois Pares', 'Sequência', 'Flush', 'Full Halse', 'Quadra', 'Streith Flush', 'Royalt Flush']
    while len(ganhadores) < n_jogadores:
        ganhadores.append(False)
    valor = 0
    o = 0
    for hand in lista:
        hand.sort()
        carta_alta = is_carta_alta(hand)
        par = is_par2(hand)
        trinca = is_trinca2(hand)
        dois_pares = is_dois_pares2(hand)
        sequencia = is_sequencia2(hand)
        flush = is_flush2(hand)
        full_halse = is_full_halse2(hand)
        streith_flush = is_streith_flush2(hand)
        quadra = is_quadra2(hand)
        royalt_flush = is_royalt_flush2(hand)
        if royalt_flush[0]:
            valor = 9
            cartas[o] = royalt_flush[1].cards
        elif streith_flush[0]:
            valor = 8
            cartas[o] = streith_flush[1].cards
        elif quadra[0]:
            cartas[o] = quadra[1].cards
            valor = 7
        elif full_halse[0]:
            cartas[o] = full_halse[1].cards
            valor = 6
        elif flush[0]:
            cartas[o] = flush[1].cards
            valor = 5
        elif sequencia[0]:
            cartas[o] = sequencia[1].cards
            valor = 4
        elif dois_pares[0]:
            cartas[o] = dois_pares[1].cards
            valor = 3
        elif trinca[0]:
            cartas[o] = trinca[1].cards
            valor = 2
        elif par[0]:
            cartas[o] = par[1].cards
            valor = 1
        else:
            cartas[o] = carta_alta[1].cards
            valor = 0   
        valores.append(valor)
        o += 1
    i = 0
    count = 0
    indices = []
    for valor in valores:
        if valor == max(valores):
            ganhadores[i] = True
            count += 1
            indices.append(i)
        else:
            ganhadores[i] == False
        i += 1
    resultado = []
    arreio = []    #o primeiro elemento do resultado precisa ser uma lista
    rank = [[], [], [], [], [], []]
    for indice in range(len(indices)):
        for carta in cartas[indices[indice]]:
            rank[indice].append(carta.rank)
    if count == 1:
        #se não houve um empate nos tipos das mãos
        arreio.append(indices[0])
        resultado.append(arreio)
        mao_vencedora = valores[indices[0]]
        resultado.append(maos[mao_vencedora])
    else:
        elementos = []
        w = 0
        empate = True
        while w < 5:
            for i in range(len(indices)):
                elementos.append(rank[i][w])
            max_elementos = []
            indice_vencedor1 = []
            indice_vencedor = 0
            for valor in elementos:
                if valor == max(elementos):
                    max_elementos.append(valor)
                    indice_vencedor1.append(indice_vencedor)
                else:
                    indice_vencedor += 1
            if len(max_elementos) == 1:
                arreio.append(indices[indice_vencedor1[0]])
                resultado.append(arreio)
                mao_vencedora = valores[indice_vencedor1[0]]
                resultado.append(maos[mao_vencedora])
                empate = False
                break
            elementos = []
            w += 1
        if empate == True:
            for indice in indice_vencedor1:
                arreio.append(indice)
            resultado.insert(0, arreio)
    return resultado





def partida():
    """Representa uma unica partida do jogo.
    """
    vez = 0
    rodada = 1
    max_rodadas = 3
    total_aposta = aposta_obrigatoria*len(jogadores)
    perdedor = 0
    sairam = [False,False,False,False,False,False]
    apostou = False
    cara_chato = None
    aposta = 0
    apostas = [0,0,0,0,0,0]
    todos_deram_all_win = False
    todos_menos_1_deram_all_win = False
    if rodada == 1:
        #Na primeira rodada
        cartas = Hand()
        baralho.move_cards(cartas, 3)
        print('\nO flop e:\n')
        for carta in cartas.cards:
            print('%s' %carta)
        print('\n')
        cartas_em_uso = Hand()
        for hand in hands:
            cartas_em_uso.cards.extend(hand.cards)
        #cartas_em_uso vai ser usado para devolver as cartas ao deck no final do jogo
        for card in cartas.cards:
            cartas_em_uso.add_card(card)
            for hand in hands:
                hand.add_card(card)
            #cada mao vai ficar com as sete cartas no final
    while rodada <= max_rodadas:
        #Enquanto não forem todas as rodadas
        if cara_chato == vez:
            #O jogador que decidiu aumentar as apostas
            pass
        else:
            print('\nVez do jogador %s:\n' % jogadores[vez])
            desistencia = False
            if perdedor == len(jogadores) - 1:
                #Se todos menos um saírem da partida
                desistencia = True
                break
            if pontuacao[vez] == 0:
                print('Voce deu all win!')
                pass
            elif todos_deram_all_win:
                print('Voce deu all win!')
                pass
            elif sairam[vez] == False:
                #Só os que ainda estão no jogo
                resp = input('Deseja ver suas cartas? ')
                resp = resp.upper()
                if resp == 'S':
                    for i in range(2):
                        print(hands[vez].cards[i])
                    print('\n')
                if pontuacao[vez] < aposta_obrigatoria or pontuacao[vez] < custo or pontuacao[vez] < apostas[vez - 1]:
                    #Se tiverem ou q dar all win ou desistir
                    resposta = input('Digite AW para dar all win (%d) ou S para desistir: ' % (pontuacao[vez]))
                    resposta = resposta.upper()
                    while resposta not in ('AW', 'S'):
                        resposta = input('Resposta invalida. Digite novamente: ')
                        resposta = resposta.upper()
                    if resposta == 'AW':
                        pontuacao[vez] = 0
                        total_aposta += pontuacao[vez]
                        #aposta = apostas[vez-1]
                    else:
                        perdedor += 1
                        sairam[vez] = True
                        print('%s desistiu!!' %jogadores[vez])
                else:
                    if apostou == True:
                        resposta = input('Digite C para cobrir a aposta (%d), D para dobrar (%d), A para apostar outro valor ou S para desistir: ' % (apostas[vez-1] - apostas[vez], aposta*2))
                    else:
                        resposta = input('Digite A para apostar, P para passar, ou S para desistir: ')
                    resposta = resposta.upper()
                    while resposta not in ('A', 'C', 'P', 'D', 'S'):
                        resposta = input('Resposta invalida. Digite novamente: ')
                        resposta = resposta.upper()
                    if resposta == 'A':
                        print("\nESCOLHA O VALOR DA SUA APOSTA:")
                        if custo > aposta:
                            print("1: %d" %custo)
                            print("2: %d" %(custo*2))
                        else:
                            print("1: %d" %aposta)
                            print("2: %d" %(aposta*2))
                        print("3: %d" % total_aposta)
                        print("4: ALL WIN (%d)" %pontuacao[vez])
                        print("5: Escolher outro valor")
                        valor_escolhido = int(input())
                        while valor_escolhido not in (1, 2, 3, 4, 5):
                            print('Opção inválida, digite algum desses números: 1, 2, 3, 4, 5')
                            valor_escolhido = int(input())
                        while True:
                            if valor_escolhido == 1:
                                aposta = custo
                            if valor_escolhido == 2:
                                aposta = custo*2
                            if valor_escolhido == 3:
                                aposta = total_aposta
                            if valor_escolhido == 4:
                                aposta = pontuacao[vez]
                            if valor_escolhido == 5:
                                aposta = int(input('Digite o valor da aposta: '))
                                while aposta > pontuacao[vez]:
                                    print("O valor digitado é maior do que %s possui no momento" %jogadores[vez])
                                    aposta = int(input('Digite o valor da aposta: '))
                            if aposta < custo:
                                print("O valor escolhido é menor do que o mínimo")
                            elif aposta <= pontuacao[vez]:
                                total_aposta += aposta
                                pontuacao[vez] -= aposta
                                break
                            else:
                                print("O valor escolhido é maior do que %s possui no momento" %jogadores[vez])
                            print("Voce tem %d pontos" %pontuacao[vez])
                            valor_escolhido = int(input("Escolha outra opcao"))
                    elif resposta == 'C':
                        if todos_menos_1_deram_all_win == True:
                            todos_deram_all_win = True
                        aposta = apostas[vez-1] - apostas[vez]
                        pontuacao[vez] -= aposta
                        total_aposta += aposta
                        aposta = apostas[vez-1]   #para que a aposta total de cada jogador fique certo
                    elif resposta == 'P':
                        print('%s passou!' %jogadores[vez])
                    elif resposta == 'D':
                        aposta = apostas[vez-1]*2
                        pontuacao[vez] -= aposta
                        total_aposta += aposta
                    elif resposta == 'S':
                        perdedor += 1
                        sairam[vez] = True
                        print('%s desistiu!!' %jogadores[vez])
                    if resposta in ('A','D'):
                        #Voltar nos outros jogadores para eles cobrirem ou aumentarem a aposta
                        cara_chato = vez
                        vez = -1
                        apostou = True
                    count = 0
                    for pontos in pontuacao:
                        if pontos == 0:
                            count += 1
                        if count == len(jogadores) - 1:
                            todos_menos_1_deram_all_win = True
        apostas[vez] = aposta
        vez += 1
        if vez == len(jogadores):
            #Quando a rodada acabar
            vez = 0
            rodada += 1
            if rodada > max_rodadas:
                break
            card = baralho.pop_card()
            for hand in hands:
                hand.add_card(card)
            cartas_em_uso.add_card(card)
            cartas.add_card(card)
            print('\nAs cartas são:\n')
            for carta in cartas.cards:
                print('%s' %carta)
            print('\n')
            apostou = False
            cara_chato = None
            aposta = 0
    #Se forem todas as rodadas
    resultado = quem_ganhou(hands)
    if desistencia == True:
        #Se todos menos um saíram da partida
        pontuacao[vez] += total_aposta
        print('\nA partida acabou!!\nParabens %s, Voce ganhou %d pontos!!' % (jogadores[vez], total_aposta))
    else:
        ganhadores = resultado[0]
        n_vencedores = len(ganhadores)
        for i in range(len(ganhadores)):
            indice = ganhadores[i]
            pontuacao[indice] += int(total_aposta/n_vencedores)
            print('\nA partida acabou!!\nParabens %s, Voce ganhou %d pontos!!' % (jogadores[indice], int(total_aposta/n_vencedores))) 
            print('A mão vencedora foi %s' %resultado[1])
    tamanho = len(cartas_em_uso.cards)
    cartas_em_uso.move_cards(baralho, tamanho)

       
            
print('BEM VINDO AO POKER DO GABRIEL!!\n\n')

baralho = Deck()
baralho.shuffle()

jogar_novamente = input('\nGostariam de jogar uma partida? Digite S para jogar: ')
jogar_novamente = jogar_novamente.upper()

while jogar_novamente == 'S':
    jogadores = pegar_jogadores(6)
    n_jogadores = len(jogadores)
    hands = criar_mao(n_jogadores)
    pontuacao = criar_pontuacao(n_jogadores)
    custo = 50
    aposta_obrigatoria = 25
    n_rodadas = 0
    while len(jogadores) > 1:
        #Lixo serve para zerar as mãos, ao invés disso tentar colocar o criar_mao() só aqui
        lixo = Hand()
        print('\nA aposta inicial e de: %d' %aposta_obrigatoria)
        baralho.shuffle()
        dar_aposta_obrigatoria()
        distribuir_cartas(2)
        partida()
        deletar()
        n_jogadores = len(jogadores)
        n_rodadas += 1
        if 300 > aposta_obrigatoria >= 100:
            aposta_obrigatoria += 50
        elif aposta_obrigatoria >= 300:
            if n_rodadas % 2 == 0:
                aposta_obrigatoria += 150
        elif n_rodadas % 3 == 0:
            custo += 50
            aposta_obrigatoria += 25
    print('\nO JOGO ACABOU! %s GANHOU!!!' % jogadores[0].upper())
    print('Voce terminou com %d pontos\n' %pontuacao[0])
    jogar_novamente = input('Gostariam de jogar uma partida? Digite S para jogar: ')
    jogar_novamente = jogar_novamente.upper()
    
print('\n\nOBRIGADO POR JOGAR!!')