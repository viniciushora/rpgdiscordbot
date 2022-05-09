import pymongo
import pickle

from cogs.rpg.server import *

end = "mongodb+srv://dahoradev:sieg482593@myrpgbot-database-zml9u.gcp.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(end)
db = client.MyRpgBot


class Database:
    @staticmethod
    def server_in_database(guild_id):
        collection = db['servers']
        if collection.count({'guild_id': guild_id }, limit = 1) != 0:
            return True
        return False

    @staticmethod
    def get_server_from_bd(guild_id):
        collection = db['servers']
        busca = collection.find({"server.guild_id": guild_id})
        if busca:
            for doc in busca:
                print(doc)
                g_id = doc['server']['guild_id']
                sistemas = doc['server']['sistemas']
                usuarios = []
                for user in doc['server']['usuarios']:
                    u = Usuario(user['user_id'], user['nome'], user['personagens'])
                    usuarios.append(u)
                server = Server(g_id, sistemas, usuarios)
                return server
        return False

    @staticmethod
    def update_server_usuarios(server):
        s = server.return_server()
        collection = db.servers
        result = collection.update_many(
            {"server.guild_id": server.get_serverID()},
            {
                "$set": {
                    "server.usuarios": s['usuarios']
                }
            }
        )
        print("Data updated with id", result)

    @staticmethod
    def insert_server(server):
        collection = db.servers
        s = server.return_server()
        insert = {"server": s}
        collection.insert_one(insert)
        print("Data inserted with id", server.get_serverID())