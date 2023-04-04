                       
 


import msgpack   
import gevent.pool
import gevent.queue
import gevent.VAR75
import gevent.local
import gevent.lock
import logging
import sys

import gevent_zmq as zmq
from .exceptions import TimeoutExpired
from .VAR50 import Context
from .channel_base import ChannelBase


if sys.version_info < (2, 7):
    def get_pyzmq_frame_buffer(frame):
        return frame.buffer[:]
else:
    def get_pyzmq_frame_buffer(frame):
        return frame.buffer


VAR0 = logging.getLogger(__name__)


class SequentialSender(object):

    def __init__(self, socket):
        self.VAR1 = socket

    def _send(self, LOP1):
        VAR2 = None
        for LOP0 in xrange(len(LOP1) - 1):
            try:
                self.VAR1.send(LOP1[LOP0], VAR3=False, VAR4=zmq.SNDMORE)
            except (gevent.GreenletExit, gevent.Timeout) as VAR2:
                if LOP0 == 0:
                    raise
                self.VAR1.send(LOP1[LOP0], VAR3=False, VAR4=zmq.SNDMORE)
        try:
            self.VAR1.send(LOP1[-1], VAR3=False)
        except (gevent.GreenletExit, gevent.Timeout) as VAR2:
            self.VAR1.send(LOP1[-1], VAR3=False)
        if VAR2:
            raise VAR2

    def __call__(self, LOP1, VAR10=None):
        if VAR10:
            with gevent.Timeout(VAR10):
                self._send(LOP1)
        else:
            self._send(LOP1)


class SequentialReceiver(object):

    def __init__(self, socket):
        self.VAR1 = socket

    def _recv(self):
        VAR2 = None
        LOP1 = []
        while True:
            try:
                VAR14 = self.VAR1.recv(VAR3=False)
            except (gevent.GreenletExit, gevent.Timeout) as VAR2:
                if len(LOP1) == 0:
                    raise
                VAR14 = self.VAR1.recv(VAR3=False)
            LOP1.append(VAR14)
            if not VAR14.more:
                break
        if VAR2:
            raise VAR2
        return LOP1

    def __call__(self, VAR10=None):
        if VAR10:
            with gevent.Timeout(VAR10):
                return self._recv()
        else:
            return self._recv()


class Sender(SequentialSender):

    def __init__(self, socket):
        self.VAR1 = socket
        self.VAR20 = gevent.queue.Channel()
        self.VAR21 = gevent.spawn(self._sender)

    def close(self):
        if self.VAR21:
            self.VAR21.kill()

    def _sender(self):
        for LOP1 in self.VAR20:
            super(Sender, self)._send(LOP1)

    def __call__(self, LOP1, VAR10=None):
        try:
            self.VAR20.put(LOP1, VAR10=VAR10)
        except gevent.queue.Full:
            raise TimeoutExpired(VAR10)


class Receiver(SequentialReceiver):

    def __init__(self, socket):
        self.VAR1 = socket
        self.VAR25 = gevent.queue.Channel()
        self.VAR26 = gevent.spawn(self._recver)

    def close(self):
        if self.VAR26:
            self.VAR26.kill()
        self.VAR25 = None

    def _recver(self):
        while True:
            LOP1 = super(Receiver, self)._recv()
            self.VAR25.put(LOP1)

    def __call__(self, VAR10=None):
        try:
            return self.VAR25.get(VAR10=VAR10)
        except gevent.queue.Empty:
            raise TimeoutExpired(VAR10)


class Event(object):

    VAR31 = ['VAR33', 'VAR34', 'VAR35', 'VAR37']

    def __init__(self, name, VAR46, VAR50, VAR32=None):
        self.VAR33 = name
        self.VAR34 = VAR46
        if VAR32 is None:
            self.VAR35 = {'message_id': VAR50.new_msgid(), 'v': 3}
        else:
            self.VAR35 = VAR32
        self.VAR37 = None

    @property
    def header(self):
        return self.VAR35

    @property
    def name(self):
        return self.VAR33

    @name.setter
    def name(self, v):
        self.VAR33 = v

    @property
    def args(self):
        return self.VAR34

    @property
    def identity(self):
        return self.VAR37

    @VAR49.setter
    def identity(self, v):
        self.VAR37 = v

    def pack(self):
        return msgpack.Packer(VAR40=True).pack((self.VAR35, self.VAR33, self.VAR34))

    @staticmethod
    def unpack(VAR85):
        VAR41 = msgpack.Unpacker(VAR42='utf-8')
        VAR41.feed(VAR85)
        VAR43 = VAR41.unpack()

        try:
            (VAR32, name, VAR46) = VAR43
        except Exception as VAR2:
            raise Exception('invalid msg format "{0}": {1}'.format(
                VAR43, VAR2))

         
        if not isinstance(VAR32, dict):
            VAR32 = {}

        return Event(name, VAR46, None, VAR32)

    def __str__(self, VAR45=False):
        if VAR45:
            VAR46 = '[...]'
        else:
            VAR46 = self.VAR34
            try:
                VAR46 = '<<{0}>>'.format(str(self.unpack(self.VAR34)))
            except Exception:
                pass
        if self.VAR37:
            VAR49 = ', '.join(repr(LOP2.bytes) for LOP2 in self.VAR37)
            return '<{0}> {1} {2} {3}'.format(VAR49, self.VAR33,
                    self.VAR35, VAR46)
        return '{0} {1} {2}'.format(self.VAR33, self.VAR35, VAR46)


class Events(ChannelBase):
    def __init__(self, zmq_socket_type, VAR50=None):
        self.VAR51 = False
        self.VAR52 = zmq_socket_type
        self.VAR53 = VAR50 or Context.get_instance()
        self.VAR1 = self.VAR53.socket(zmq_socket_type)

        if zmq_socket_type in (zmq.PUSH, zmq.PUB, zmq.DEALER, zmq.ROUTER):
            self.VAR55 = Sender(self.VAR1)
        elif zmq_socket_type in (zmq.REQ, zmq.REP):
            self.VAR55 = SequentialSender(self.VAR1)
        else:
            self.VAR55 = None

        if zmq_socket_type in (zmq.PULL, zmq.SUB, zmq.DEALER, zmq.ROUTER):
            self.VAR58 = Receiver(self.VAR1)
        elif zmq_socket_type in (zmq.REQ, zmq.REP):
            self.VAR58 = SequentialReceiver(self.VAR1)
        else:
            self.VAR58 = None

    @property
    def recv_is_supported(self):
        return self.VAR58 is not None

    @property
    def emit_is_supported(self):
        return self.VAR55 is not None

    def __del__(self):
        try:
            if not self.VAR1.closed:
                self.close()
        except (AttributeError, TypeError):
            pass

    def close(self):
        try:
            self.VAR55.close()
        except AttributeError:
            pass
        try:
            self.VAR58.close()
        except AttributeError:
            pass
        self.VAR1.close()

    @property
    def debug(self):
        return self.VAR51

    @debug.setter
    def debug(self, v):
        if v != self.VAR51:
            self.VAR51 = v
            if self.VAR51:
                VAR0.debug('debug enabled')
            else:
                VAR0.debug('debug disabled')

    def _resolve_endpoint(self, VAR63, VAR62=True):
        if VAR62:
            VAR63 = self.VAR53.hook_resolve_endpoint(VAR63)
        if isinstance(VAR63, (tuple, list)):
            VAR64 = []
            for LOP3 in VAR63:
                VAR64.extend(self._resolve_endpoint(LOP3, VAR62))
            return VAR64
        return [VAR63]

    def connect(self, VAR63, VAR62=True):
        VAR64 = []
        for LOP4 in self._resolve_endpoint(VAR63, VAR62):
            VAR64.append(self.VAR1.connect(LOP4))
            VAR0.debug('connected to %s (VAR67=%s)', LOP4, VAR64[-1])
        return VAR64

    def bind(self, VAR63, VAR62=True):
        VAR64 = []
        for LOP4 in self._resolve_endpoint(VAR63, VAR62):
            VAR64.append(self.VAR1.bind(LOP4))
            VAR0.debug('bound to %s (VAR67=%s)', LOP4, VAR64[-1])
        return VAR64

    def disconnect(self, VAR63, VAR62=True):
        VAR64 = []
        for LOP4 in self._resolve_endpoint(VAR63, VAR62):
            VAR64.append(self.VAR1.disconnect(LOP4))
            logging.debug('disconnected from %s (VAR67=%s)', LOP4, VAR64[-1])
        return VAR64

    def new_event(self, name, VAR46, VAR74=None):
        VAR75 = Event(name, VAR46, VAR50=self.VAR53)
        if VAR74:
            VAR75.VAR32.update(VAR74)
        return VAR75

    def emit_event(self, VAR75, VAR10=None):
        if self.VAR51:
            VAR0.debug('--> %s', VAR75)
        if VAR75.VAR49:
            LOP1 = list(VAR75.VAR49 or list())
            LOP1.extend(['', VAR75.pack()])
        elif self.VAR52 in (zmq.DEALER, zmq.ROUTER):
            LOP1 = ('', VAR75.pack())
        else:
            LOP1 = (VAR75.pack(),)
        self._send(LOP1, VAR10)

    def recv(self, VAR10=None):
        LOP1 = self._recv(VAR10=VAR10)
        if len(LOP1) > 2:
            VAR49 = LOP1[0:-2]
            VAR85 = LOP1[-1]
        elif len(LOP1) == 2:
            VAR49 = LOP1[0:-1]
            VAR85 = LOP1[-1]
        else:
            VAR49 = None
            VAR85 = LOP1[0]
        VAR75 = Event.unpack(get_pyzmq_frame_buffer(VAR85))
        VAR75.VAR49 = VAR49
        if self.VAR51:
            VAR0.debug('<-- %s', VAR75)
        return VAR75

    def setsockopt(self, *VAR46):
        return self.VAR1.setsockopt(*VAR46)

    @property
    def context(self):
        return self.VAR53
