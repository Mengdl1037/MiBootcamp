# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-21
# Function:

def show_messages(messages):
    """Print all the messages in the list
    Arges:
        messages: a list of messages
    """
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """Print all the messages in the first list \
        and then add them to the second list
    Args:
        messages: a list of messages needed to be sent
        sent_messages: a list of messages that have been sent
    """
    while messages:
        message = messages.pop(0)
        sent_messages.append(message)
        print(message)


messages = ['Hello!', 'How are you?', 'Good morning!', 'Good night!']
sent_messages = []
show_messages(messages)
print('\n')
send_messages(messages[:], sent_messages)
print('\n')
print(messages)
print(sent_messages)