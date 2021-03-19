from uuid import uuid4
from abc import ABC, abstractmethod

class Ticket(ABC):
    def __init__(self):
        self.valid = True
        self.ticket_id = uuid4()

    @abstractmethod
    def use_me(self):
        pass

    @abstractmethod
    def annul(self,reason):
        pass

    def show_ticket_promary_info(self):
        return {"valid": self.valid, "ticker_id":self.ticket_id}


class TheaterTicket(Ticket):
    def use_me(self):
        self.valid = False
        print("Даем человеку бинокль в подарок")

    def annul(self,reason):
        self.valid = False
        print(f"Билет id {self.ticket_id} был аннулирован по причине {reason}")


class FlightTicket(Ticket):
    def use_me(self):
        self.valid = False
        print("Даем человеку маску в подарок")

    def annul(self,reason):
        self.valid = False
        print(f"Билет id {self.ticket_id} был аннулирован по причине {reason}")


class Controller:
    def __init__(self, controller_id):
        self.controller_id = controller_id

    def use_ticket(self, ticket: Ticket):
        ticket.use_me()
        print(f"Контроллер id {self.controller_id} осуществил погашение билета {ticket.ticket_id}")

    def annul_ticket(self,ticket: Ticket, reason: str):
        ticket.annul(reason)
        print(f"Контроллер id {self.controller_id} осуществил аннулирование билета {ticket.ticket_id}")

    def businees_logic(self, event, ticket):
        if event == "событие_1":
            self.use_ticket(ticket)
        elif event == "событие_2":
            self.annul_ticket(ticket,"событие_2")

"ОСТАНОВИЛСЯ НА 59 минуте"

controller = Controller(1)
t_ticket = TheaterTicket()
f_ticket = FlightTicket()
# controller.use_ticket(t_ticket)
# controller.use_ticket(f_ticket)

# ticket = Ticket()
controller.annul_ticket(f_ticket,"пассажир пьян")