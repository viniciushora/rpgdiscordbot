import discord
from discord.ext import commands
import random
from cogs.rpg.char import *
from cogs.rpg.sessao import *

import pickle
import io
import youtube_dl
import os
from discord.utils import get
import logging
import asyncio
from cogs.rpg.usuario import *

class Server():
    def __init__(self, guild_id, sistemas = [], usuarios = []):
        self.guild_id = guild_id
        self.sistemas = []
        self.usuarios = usuarios

    def atualizar_usuarios(self, usuarios):
        self.usuarios = usuarios

    def adicionar_sistema(self, sistema):
        self.sistemas.append(sistema)

    def get_serverID(self):
        return self.guild_id

    def get_usuarios(self):
        return self.usuarios

    def add_usuario(self, usuario):
        self.usuarios.append(usuario)

    def return_server(self):
        usuarios = []
        for u in self.usuarios:
            usuarios.append(u.return_usuario())
        s = {"guild_id": self.guild_id, "sistemas": self.sistemas, "usuarios": self.array_usuarios()}
        return s

    def array_usuarios(self):
        array_usuarios = []
        for u in self.usuarios:
            array_usuarios.append(u.return_usuario())
        return array_usuarios

    def verifica_usuario(self, user_id):
        for u in self.usuarios:
            if user_id == u.getMemberID():
                return True
        return False
