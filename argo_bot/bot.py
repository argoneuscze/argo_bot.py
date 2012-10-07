from twisted.words.protocols import irc
from twisted.internet import protocol, reactor
from config import Config

# Class responsible for running the bot
class IRCBot(object):
    # Starts the factory
    def start(self):
        reactor.connectTCP(Config._host, Config._port, IRCBotFactory())
        reactor.run()

class IRCBotProtocol(irc.IRCClient):
    _name = Config._name

class IRCBotFactory(protocol.ReconnectingClientFactory):
    protocol = IRCBotProtocol
    channels = [Config._channel]
