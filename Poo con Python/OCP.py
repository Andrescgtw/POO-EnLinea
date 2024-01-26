class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar (self):
        raise NotImplementedError
    
class NotificadorEmail (Notificador):
    def notificar(self):
        print(f"Enviando mensaje por Mail a  {self.usuario.email}")

class NotificadorSMS (Notificador):
    def notificar(self):
        print(f"Enviado SMS a {self.usuario.sms}")
    
class NotificadorWhatsapp (Notificador):
    def notificar(self):
        print(f"Enviado Whatsapp a {self.usuario.whatsapp}")
    