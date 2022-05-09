class RegrasMissingException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)

class EfeitosMissingException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class StatusNotFoundException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class ConteudoInvalidoException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)