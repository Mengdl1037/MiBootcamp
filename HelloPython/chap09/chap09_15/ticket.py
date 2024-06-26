from random import choice

class Ticket():
    """生成彩票中奖号"""

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
ticket_now = ticket.generate_ticket()
print(f"Winning ticket: {ticket_now}\n")

count = 0
while True:
    my_ticket = ticket.generate_ticket()
    count += 1
    ticket_temp = my_ticket[:]

    win = True
    while ticket_temp:
        if ticket_temp.pop() not in ticket_now:
            win = False
            break
    if win:
        print(f"Congratulations! You won in {count} times.")
        break
    else:
        print(f"Try {count} times: {my_ticket}")
    