from dataclasses import dataclass


@dataclass
class Data:
    """ Класс для описания пакета информации."""
    data: str
    ip: int

    def __repr__(self):
        return f'{self.data}'


class Server:
    """ Класс для описания работы серверов сети."""
    ip_total = 1

    def __init__(self):
        self.ip = Server.ip_total
        Server.ip_total += 1
        self.buffer = []
        self.router = None
        print(f"Создан сервер {self.ip}")

    def get_ip(self):
        """ Возвращает ip сервера."""
        return self.ip

    def get_server_data(self, data):
        """ Получает пакет данных."""
        self.buffer.append(data)

    def send_data_from_router(self, data):
        """ Отправляет пакет данных роутеру."""
        router.buffer.append(data)
        self.buffer.clear()

    def __repr__(self):
        return f'Сервер {self.ip}'


class Router:
    """ Класс для описания работы роутеров в сети."""
    def __init__(self):
        self.servers = {}
        self.buffer = []
        print(f"Создан роутер")

    def link(self, server):
        """Связывает сервер с роутером."""
        self.servers[server.get_ip()] = server
        server.router = self
        print(f"{server} присоединился к роутеру")

    def unlink(self, server):
        """Отвязывает сервер от роутера."""
        if server.get_ip() in self.servers:
            server.router = None
            del self.servers[server.get_ip()]
        print(f"{server} отсоединился от роутера")

    def send_data(self):
        """Отправляет данные всем серверам в сети."""
        for data in self.buffer:
            if data.ip in self.servers:
                self.servers[data.ip].get_server_data(data)
                print(f"{self.servers[data.ip]} получил данные {data}")

    def __repr__(self):
        return f'{list(self.servers.keys())}'


# Пример использования
if __name__ == "__main__":
    # Создаем роутер
    router = Router()

    # Создаем серверы
    server1 = Server()
    server2 = Server()
    server3 = Server()

    # Привязываем серверы к роутеру
    router.link(server1)
    router.link(server2)
    router.link(server3)

    # Отправляем данные через роутер
    data1 = Data(data="Hello, Server 3!", ip=server1.get_ip())
    data2 = Data(data="Hello, Server 2!", ip=server2.get_ip())
    data3 = Data(data="Hello, Server 1!", ip=server3.get_ip())

    server1.send_data_from_router(data1)
    server2.send_data_from_router(data2)
    server3.send_data_from_router(data3)

    router.send_data()

