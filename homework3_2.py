import random


def get_numbers_ticket(min, max, quantity):
    ticket_lottery = random.sample(range(1, 36), k=5)
    print("Provide 5 numbers from 1 to 36 (one by one- separated by spacebars):")
    ticket_input: list = list(map(int, input().split()))
    result = list(zip(ticket_lottery, ticket_input))
    print(f'Lottery Ticket: {" ".join([str(i) for i in ticket_lottery])}')
    print(f'User\'s Choice : {" ".join([str(i) for i in ticket_input])}')
    print(' \n ----------- Results ----------- ')
    points = 0
    for lottery, user_choice in result:
        if lottery == user_choice:
            points += 1
    print('\nTotal points', points)


ticket_lottery = get_numbers_ticket(min=1, max=36, quantity=5)