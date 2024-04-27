import random

def get_numbers_ticket(ticket_input, min, max, quantity):
    if len(ticket_input) != quantity:
        print("Invalid number of inputs")
        return    
    
    ticket_lottery = random.sample(range(min, max), quantity)
    ticket_lottery.sort()
    result = list(zip(ticket_lottery, ticket_input))
    print(f'Lottery Ticket: {" ".join([str(i) for i in ticket_lottery])}')
    print(f'User\'s Choice: {" ".join([str(i) for i in ticket_input])}')    
    
    points = 0
    for lottery, user_choice in result:
        if lottery == user_choice:
            points += 1
    print('\nTotal points:', points)
    
    
print("Provide 5 numbers from 1 to 36 (one by one - separated by spaces):")
ticket_input = list(map(int, input().split()))


get_numbers_ticket(ticket_input, min=1, max=36, quantity=5)

