from dataclasses import dataclass
from typing import Any, Protocol, Set


@dataclass
class Message:
    message_id: str
    payload: Any


@dataclass
class MyApplicationMessage(Message):
    pass


class Subscriber(Protocol):
    def receive(self, message: Message):
        pass


class Speaker(Subscriber):
    def __init__(self, location: Message = ">>>"):
        self.location = location

    def receive(self, message: MyApplicationMessage):
        print(f"Playing at '{self.location:}': {message.payload}")


class Broadcaster:
    def __init__(self):
        self.subscribers: Set[Subscriber] = set()

    def subscribe(self, subscriber: Subscriber):
        self.subscribers.add(subscriber)

    def publish(self, message: Message):
        for subscriber in self.subscribers:
            subscriber.receive(message=message)


broadcaster = Broadcaster()

broadcaster.subscribe(Speaker("left speaker"))
broadcaster.subscribe(Speaker("right speaker"))

broadcaster.publish(MyApplicationMessage(message_id="1", payload="This love ..."))
