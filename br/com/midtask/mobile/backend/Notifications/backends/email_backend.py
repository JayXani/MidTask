import ssl

from django.core.mail.backends.smtp import EmailBackend as SMTPBackend
from django.utils.functional import cached_property


class EmailBackend(SMTPBackend):
    @cached_property # Define uma conexao SSL
    def ssl_context(self):
        if self.ssl_certfile or self.ssl_keyfile: # Se existir já uma conexao SSL
            ssl_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT) # Crio um contexto TLS e uso um certificado e chaves personalizados
            ssl_context.load_cert_chain(self.ssl_certfile, self.ssl_keyfile)
            return ssl_context
        else: # APENAS PARA AMBIENTES DE DESENVOLVIMENTO, ISSO NAO DEVE IR PRA PRODUCAO
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False # Desativa o SSL, nao valida o hostname
            ssl_context.verify_mode = ssl.CERT_NONE # Ignora a validacao do certificado
            return ssl_context