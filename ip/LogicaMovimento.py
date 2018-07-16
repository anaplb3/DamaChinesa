# -*- coding: utf-8 -*-

def pegarProximaPosicao(linhaAtual, posicaoNaLinhaAtual, direcao, salto):
    if salto == True:
        quantidadeDeLinhasPraPular=2
    else:
        quantidadeDeLinhasPraPular=1

   
    proximaLinha = linhaAtual
    if direcao == "ul" or direcao == "ur":
        proximaLinha -= quantidadeDeLinhasPraPular
    elif direcao == "dl" or direcao == "dr":
        proximaLinha += quantidadeDeLinhasPraPular
   

    deslocamento = 0
    
    if (((linhaAtual>=1 and linhaAtual<=4) and (proximaLinha>=1 and proximaLinha<=4)) or  
    ((linhaAtual>=14 and linhaAtual<=17) and (proximaLinha>=14 and proximaLinha<=17)) or  
    ((linhaAtual>=5 and linhaAtual<=13) and (proximaLinha>=5 and proximaLinha<=13))):      
        deslocamento = 0  
    elif (((linhaAtual>=1 and linhaAtual<=4) and (proximaLinha>=5 and proximaLinha<=9)) or 
    ((linhaAtual>=14 and linhaAtual<=17) and (proximaLinha>=9 and proximaLinha<=13))):     
        deslocamento = 4
    elif (((linhaAtual>=5 and linhaAtual<=9) and (proximaLinha>=1 and proximaLinha<=4)) or 
    ((linhaAtual>=9 and linhaAtual<=13) and (proximaLinha>=14 and proximaLinha<=17))):     
        deslocamento = -4

    posicaoNaProximaLinha = posicaoNaLinhaAtual
    if direcao=="ul":
        if (((linhaAtual>=1 and linhaAtual<=4) and (proximaLinha>=1 and proximaLinha<=4)) or   
        ((linhaAtual>=9 and linhaAtual<=13) and (proximaLinha>=9 and proximaLinha<=13)) or    
        ((linhaAtual>=5 and linhaAtual<=6) and (proximaLinha>=3 and proximaLinha<=4))):        
            posicaoNaProximaLinha += deslocamento - quantidadeDeLinhasPraPular
            if linhaAtual == 6 and proximaLinha == 4:                                          
                posicaoNaProximaLinha += 1
        else:
            posicaoNaProximaLinha += deslocamento
            if linhaAtual == 14 and proximaLinha == 12:                                        
                posicaoNaProximaLinha -= 1


    elif direcao=="ur" :
        if (((linhaAtual>=5 and linhaAtual<=9) and (proximaLinha>=5 and proximaLinha<=9)) or   
        ((linhaAtual>=14 and linhaAtual<=17) and (proximaLinha>=14 and proximaLinha<=17)) or  
        ((linhaAtual>=14 and linhaAtual<=15) and (proximaLinha>=12 and proximaLinha<=13))):   
            posicaoNaProximaLinha += deslocamento + quantidadeDeLinhasPraPular
            if linhaAtual == 14 and proximaLinha == 12:                                       
                posicaoNaProximaLinha -= 1
        else:
            posicaoNaProximaLinha += deslocamento
            if linhaAtual == 6 and proximaLinha == 4:                                          
                posicaoNaProximaLinha += 1


    elif direcao=="dr" :
        if (((linhaAtual>=1 and linhaAtual<=4) and (proximaLinha>=1 and proximaLinha<=6)) or   
        ((linhaAtual>=9 and linhaAtual<=13) and (proximaLinha>=9 and proximaLinha<=15)) or     
        ((linhaAtual>=12 and linhaAtual<=13) and (proximaLinha>=14 and proximaLinha<=15))):    
            posicaoNaProximaLinha += deslocamento + quantidadeDeLinhasPraPular
            if ((linhaAtual == 4 and proximaLinha == 6) or                                     
            (linhaAtual == 12 and proximaLinha == 14)):                                         
                posicaoNaProximaLinha -= 1
            elif(linhaAtual==13 and (proximaLinha>=14 and proximaLinha<=15)):                 
                posicaoNaProximaLinha -= quantidadeDeLinhasPraPular
        else:
            posicaoNaProximaLinha += deslocamento  


    elif direcao=="dl" :
        if (((linhaAtual>=5 and linhaAtual<=9) and (proximaLinha>=5 and proximaLinha<=9)) or   
        ((linhaAtual>=14 and linhaAtual<=17) and (proximaLinha>=14 and proximaLinha<=17)) or   
        ((linhaAtual>=12 and linhaAtual<=13) and (proximaLinha>=14 and proximaLinha<=15))):    
            posicaoNaProximaLinha += deslocamento - quantidadeDeLinhasPraPular
            if linhaAtual == 12 and proximaLinha == 14:                                        
                posicaoNaProximaLinha += 1
        else:
            posicaoNaProximaLinha += deslocamento
            if linhaAtual == 4 and proximaLinha == 6:                                          
                posicaoNaProximaLinha -= 1
            


    elif direcao == "l":
        posicaoNaProximaLinha -= quantidadeDeLinhasPraPular

    else: 
        posicaoNaProximaLinha += quantidadeDeLinhasPraPular

    return [proximaLinha, posicaoNaProximaLinha]
    






