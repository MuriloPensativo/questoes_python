def palindrome(texto):
    '''Faça uma função que verifique se uma textro passado é palíndrome,
    isto é, se é igual quando lido de trás pra frente.'''
    texto2 = ""
    for a in texto:
        if a.isalpha():
            texto2 += a

    texto2 = texto2.casefold()
    texto2len = len(texto2)
    
    if texto2len % 2 == 1:
        first_half = texto2[:int((texto2len - 1) / 2)]
        second_half = texto2[int((1 - texto2len) / 2):]
    else:
        first_half = texto2[:int(texto2len / 2)]
        second_half = texto2[int(-texto2len / 2):]

    return first_half == second_half[::-1]

def troca_caixa(texto):
    '''Vogais ficam em caixa alta (maiúsculas)
    Consoantes ficam em caixa baixa (minúsculas)'''
    texto2 = ""
    vogais = ['a', 'e', 'i', 'o', 'u']
    consoantes = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    for a in texto:
        if a in vogais:
            texto2 += a.upper()
        elif a in consoantes:
            texto2 += a.lower()
        else:
            texto2 += a
        
    return texto2

def imprime_mes_por_extenso(data):
    '''Faça um programa que solicite a data de nascimento (dd/mm/aaaa) 
    e imprima com o nome do mês por extenso
    '''
    split_data = data.split("/")
    if split_data[1] == "01":
        split_data[1] = " de janeiro de "
    elif split_data[1] == "02":
        split_data[1] = " de fevereiro de "
    elif split_data[1] == "03":
        split_data[1] = " de março de "
    elif split_data[1] == "04":
        split_data[1] = " de abril de "
    elif split_data[1] == "05":
        split_data[1] = " de maio de "
    elif split_data[1] == "06":
        split_data[1] = " de junho de "
    elif split_data[1] == "07":
        split_data[1] = " de julho de "
    elif split_data[1] == "08":
        split_data[1] = " de agosto de "
    elif split_data[1] == "09":
        split_data[1] = " de setembro de "
    elif split_data[1] == "10":
        split_data[1] = " de outubro de "
    elif split_data[1] == "11":
        split_data[1] = " de novembro de "
    elif split_data[1] == "12":
        split_data[1] = " de dezembro de "
    else:
        split_data[1] = " mês inválido "
        
    return "".join(split_data)

def encontra_caracter(texto, caracter):
    '''Receba um texto e retorne a localização da primeira vez que 
    aparece o caracter especificado'''
    for i in range(len(texto)):
        if caracter == texto[i]:
         return i

def numeros_sortudos(limite_inferior=1, limite_superior=100000):
    ''' Daniela é uma pessoa muito supersticiosa. Para ela, um número é 
    sortudo se ele contém o dígito 2 mas não o dígito 7. 
    Faça então uma função que informe a ela quantos números sortudos 
    existem entre um intervalo dado, incluindo os extremos.
    Por exemplo: entre 18644 e 33087, existem 7995 números sortudos.
    Dica: faça uma função de validação e outra que a chama e 
    verifica o intervalo dado
    '''
    count = 0
    for n in range(limite_inferior, limite_superior + 1):
        if "2" in str(n) and "7" not in str(n):
            count += 1
    return count

def ponteironuloville(telefones):
    '''Na pacata vila campestre de Ponteironuloville, todos os telefones 
    têm 6 dígitos. A companhia telefônica estabelece as seguintes regras 
    sobre os números:
    1. Não pode haver dois dígitos consecutivos idênticos, porque isso é chato;
    2. A soma dos dígitos tem que ser par, porque isso é legal;
    3. O último dígito não pode ser igual ao primeiro, porque isso dá azar.
    
    Então, dadas essas regras perfeitamente razoáveis, bem projetadas e 
    maduras, quantos números de telefone na lista abaixo são válidos?  
    Dica: faça uma função de validação e outra que a chama e verifica os 
    valores passados.
    Outra dica: coloque a lista em um arquivo texto
    Mais uma dica: você precisa incluir um teste com esses valores.
        213752 216732 221063 221545 225583 229133 230648 233222
        236043 237330 239636 240138 242123 246224 249183 252936
        254711 257200 257607 261424 263814 266794 268649 273050
        275001 277606 278997 283331 287104 287953 289137 291591
        292559 292946 295180 295566 297529 300400 304707 306931
        310638 313595 318449 319021 322082 323796 326266 326880
        327249 329914 334392 334575 336723 336734 338808 343269
        346040 350113 353631 357154 361633 361891 364889 365746
        365749 366426 369156 369444 369689 372896 374983 375223
        379163 380712 385640 386777 388599 389450 390178 392943
        394742 395921 398644 398832 401149 402219 405364 408088
        412901 417683 440052 444630 463328 466458 486195 488359
        500877 502386 521455 524277 536593 537360 556493 558807
        579937 580112 590483 593112 601523 605761 618314 622752
        637656 641136 662224 666265 422267 447852 469601 489209
        502715 528496 539055 559102 580680 593894 608618 626345
        644176 668010 424767 449116 473108 489388 507617 529345
        540582 562050 582458 594293 609198 626632 644973 672480
        426613 453865 476773 491928 512526 531231 543708 564962
        583012 597525 610141 628889 647617 672695 430474 457631
        477956 496569 512827 531766 547492 569677 585395 598184
        610536 629457 652218 676868 433910 461750 481991 496964
        513796 535067 550779 570945 586244 600455 612636 629643
        657143 677125 435054 462985 482422 497901 518232 535183
        551595 575447 587393 600953 615233 633673 659902 678315
        Resposta: 39 
    '''
    def is_not_repeated(n):
        text = str(n)
        for x in range(len(text) - 1):
            if text[x] == text[x + 1]:
                return False
        return True
    
    def is_even_sum(n):
        text = str(n)
        sum = 0
        for a in text:
            sum += int(a)
        return sum % 2 == 0

    def is_last_not_same_as_first(n):
        z = str(n)
        if z[0] == z[-1]:
            return False
        return True

    total = 0

    for n in telefones:
        if is_not_repeated(n) and is_even_sum(n) and is_last_not_same_as_first(n):
            total += 1
    return total

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0 

def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31m%s' % ('Falhou')
    else:
        prefixo = '\033[32m%s' % ('Passou')
        acertos += 1
    print('%s Esperado: %s \tObtido: %s\033[1;m' % (prefixo, repr(esperado), repr(obtido)))

def main():

    print(' Palindrome:')
    test(palindrome("ovo"), True) # normal
    test(palindrome("Ovo"), True) # mudança de caixa
    test(palindrome("Ovo "), True) # espaço no final
    test(palindrome(" Ovo "), True) # espaço no início
    test(palindrome('Assam a massa'), True) # frases (espaços em branco)
    test(palindrome('Ame o poema!'), True) # frases com pontuação

    print(' Troca caixa:')
    test(troca_caixa("Araquari"), "ArAqUArI") # normal
    test(troca_caixa("Caxias do Sul"), "cAxIAs dO sUl") # com espaços

    print(' Mês por extenso:')
    test(imprime_mes_por_extenso("19/05/2014"), "19 de maio de 2014")
    test(imprime_mes_por_extenso("25/12/2016"), "25 de dezembro de 2016")

    print(' Encontra caracter:')
    test(encontra_caracter("--*--","*"), 2)
    test(encontra_caracter("19/05/2014","/"), 2)
    test(encontra_caracter("19/05/2014","."), None)

    print(' Números sortudos:')
    test(numeros_sortudos(18644,33087), 7995)

    print(' Ponteironuloville:')
    telefones = ['91775523', '88032828']
    test(ponteironuloville(telefones), 0)
    telefones = '''
        213752 216732 221063 221545 225583 229133 230648 233222
        236043 237330 239636 240138 242123 246224 249183 252936
        254711 257200 257607 261424 263814 266794 268649 273050
        275001 277606 278997 283331 287104 287953 289137 291591
        292559 292946 295180 295566 297529 300400 304707 306931
        310638 313595 318449 319021 322082 323796 326266 326880
        327249 329914 334392 334575 336723 336734 338808 343269
        346040 350113 353631 357154 361633 361891 364889 365746
        365749 366426 369156 369444 369689 372896 374983 375223
        379163 380712 385640 386777 388599 389450 390178 392943
        394742 395921 398644 398832 401149 402219 405364 408088
        412901 417683 440052 444630 463328 466458 486195 488359
        500877 502386 521455 524277 536593 537360 556493 558807
        579937 580112 590483 593112 601523 605761 618314 622752
        637656 641136 662224 666265 422267 447852 469601 489209
        502715 528496 539055 559102 580680 593894 608618 626345
        644176 668010 424767 449116 473108 489388 507617 529345
        540582 562050 582458 594293 609198 626632 644973 672480
        426613 453865 476773 491928 512526 531231 543708 564962
        583012 597525 610141 628889 647617 672695 430474 457631
        477956 496569 512827 531766 547492 569677 585395 598184
        610536 629457 652218 676868 433910 461750 481991 496964
        513796 535067 550779 570945 586244 600455 612636 629643
        657143 677125 435054 462985 482422 497901 518232 535183
        551595 575447 587393 600953 615233 633673 659902 678315
    '''.strip().split()
    test(ponteironuloville(telefones), 39)
    #telefones = open('telefones.txt').read().strip().split()
    #test(ponteironuloville(telefones), 39)

if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")