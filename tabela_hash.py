# -*- coding:UTF-8 -*-
from no import No

class TabelaHashEnderecamentoAberto:

    #Constantes
    OCUPADO = 1
    VAZIO = -1
    LIBERADO = -2

    """
    Tabela Hash com tratamento de colisão por endereçamento aberto
    utilizando sondagem quadrática para resolver colisões
    """
    def __init__(self, tamanho=32):
        self.__tamanho = tamanho
        self.__tabela = [None] * tamanho
        self.__qtd = 0
        print(f"Criada EDD Tabela Hash com capacidade: {tamanho}")


    # Retorna o valor do hash para uma determinada chave
    def __hash(self, chave) -> int:
        return hash(chave) % self.__tamanho        
        # implementação do método
        


    # Retorna o valor do hash2 para uma determinada chave e índice k
    def __hash2(self, chave, k) -> int:
        return (self.__hash(chave) + k**2) % self.__tamanho    
        # implementação do método
        

    
    # Retorna a posição do objeto No na Tabela Hash para uma determinada chave
    # Caso a chave não exista na tabela, retorna -1
    # Esse é um método privado, pois só é utilizado dentro da classe
    # Ele é usado internamente para auxiliar os métodos get() e remove()
    def __find(self, chave) -> int:
        hash_value = self.__hash(chave)
        k = 0
        while self.__tabela[hash_value] is not None:
            if self.__tabela[hash_value].chave == chave and self.__tabela[hash_value].dado != self.LIBERADO:
                return hash_value
            k += 1
            hash_value = self.__hash2(chave, k)
            if k == self.__tamanho:
                break
        return -1        
        # implementação do método
    


    # Retorna o objeto No da tabela hash para uma determinada chave
    # Caso a chave não exista na tabela, retorna None
    def get(self, chave) -> No:
        pos = self.__find(chave)
        return self.__tabela[pos] if pos != -1 else None        
        # implementação do método
        


    # Insere um nó na tabela hash recebendo uma chave e um valor
    # Caso a chave já exista na tabela, sobrescreve o valor
    # Caso a tabela esteja cheia, retorna False
    def insert(self, chave, valor) -> None:
        if self.__qtd == self.__tamanho:
            return False

        hash_value = self.__hash(chave)
        k = 0
        while self.__tabela[hash_value] is not None and self.__tabela[hash_value].dado != self.LIBERADO:
            if self.__tabela[hash_value].chave == chave:
                self.__tabela[hash_value].dado = valor
                return True
            k += 1
            hash_value = self.__hash2(chave, k)
            if k == self.__tamanho:
                break

        self.__tabela[hash_value] = No(chave, valor)
        self.__tabela[hash_value].status = self.OCUPADO
        self.__qtd += 1
        return True        
        # implementação do método
    
    

    # Remove um dado da tabela inserindo None na posição da 
    # lista de chaves e da lista do valores
    # Retorna True se a remoção foi bem sucedida, False caso contrário
    def remove(self, chave) -> bool:
        pos = self.__find(chave)
        if pos != -1:
            self.__tabela[pos].status = self.LIBERADO
            self.__qtd -= 1
            return True
        return False        
        
        # implementação do método
        pass

    
    # Retorna uma lista de tuplas com os seguintes valores: (chave, valor, status) 
    # Caso a posição não tenha sido ocupada, retorna a seguinte tupla: (None, None, status) 
    # Caso a tabela esteja vazia, retorna uma lista vazia
    def display(self) -> list[tuple]:
        pos = self.__find(chave)
        if pos != -1:
            self.__tabela[pos].status = self.LIBERADO
            self.__qtd -= 1
            return True
        return False

    def display(self) -> list[tuple]:
        result = []
        i = 0
        for j in self.__tabela:
            if j is None:
                result.append((None, None, self.VAZIO))
                i+=1
            else:
                result.append((j.chave, j.dado, j.status))
            if i == self.__tamanho:
                result = []
        return result        
        # implementação do método
    


