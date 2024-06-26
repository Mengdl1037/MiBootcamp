from random import choice

"""生成彩票中奖号"""
class Ticket():

    def __init__(self):
        self.elements = [str(value) for value in range(0, 10)]
        self.elements += ['a', 'b', 'c', 'd', 'e']

    def generate_ticket(self):
        ticket = []
        i = 0
        while i < 4:
            ticket.append(choice(self.elements))
            i += 1
        return ticket
    

ticket = Ticket()
print(ticket.generate_ticket())