
from uuid import UUID, uuid4
from app.models.task import Task
from typing import List


users = []


class User():
    __id: int
    __name: str
    __password: str
    __tasks: List[Task]

    def __init__(self, **keywords):
        self.__id = keywords.get('id', uuid4().int)
        self.__name = keywords.get('name', "")
        self.__password = keywords.get('password', "")
        self.__tasks = keywords.get('tasks', [])

    @property
    def id(self):
        return self.__id

    
    def check_id(self, id):
        return self.__id == id

    @property
    def password(self):
        pass

    @password.setter
    def password(self, value: str):
        self.__password = value

    def check_password(self, password: str):
        return self.__password == password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if (len(value) < 3):
            raise ValueError('name must be at least 3 characters')
        self.__name = value

    def check_name(self, name: str):
        return self.__name == name

    def add_task(self, value: Task):
        self.__tasks.append(value)

    @property
    def tasks(self):
        return self.__tasks[:]

    def check_credentials(self, name: str, password: str):
        return self.check_name(name) and self.check_password(password)
