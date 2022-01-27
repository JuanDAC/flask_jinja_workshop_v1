from uuid import UUID, uuid4
import datetime
from datetime import datetime as date
from app.models.state import State


class Task():
    __id: int
    __title: str
    __description: str
    __end_date: datetime
    __start_date: datetime
    __state: State

    def __init__(self, **keywords):
        self.__id = keywords.get('id', uuid4().int)
        self.__title = keywords.get('title', "")
        self.__description = keywords.get('description', "")
        self.__end_date = keywords.get('end_date', None)
        self.__start_date = keywords.get('start_date', date.now())
        self.__state = keywords.get('state', State.ToDo)

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value: str):
        self.__description = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value: str):
        self.__title = value

    def end_date(self):
        self.__start_date = date.now()

    @property
    def start_date(self):
        return self.__start_date

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value: State):
        self.__state = value
