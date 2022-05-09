import discord
import asyncio

class Usuario:
    def __init__(self, user_id , nome, personagens = []):
        self.user_id = user_id
        self.nome = nome
        self.personagens = personagens

    def getNomeID(self):
        return self.nome

    def setNomeID(self,nome):
        self.nome = nome

    def getMemberID(self):
        return self.user_id

    def addPersonagem(self,personagem):
        self.personagens.append(personagem)

    def delPersonagem(self,personagem):
        cont = 0
        for i in range(len(self.personagens)):
            if self.personagens[i] == personagem.getID():
                del(self.personagens[i])
                cont +=1
        if cont==0: return False

    def return_usuario(self):
        usuario = {"user_id": self.user_id, "nome": self.nome, "personagens": self.personagens}
        return usuario