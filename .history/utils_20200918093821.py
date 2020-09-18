
import hashlib


def display_transaction(transaction):
    # for transaction in transactions:
    dict = transaction.to_dict()
    print("sender: " + dict['sender'])
    print('-----')
    print("recipient: " + dict['recipient'])
    print('-----')
    print("value: " + str(dict['value']))
    print('-----')
    print("time: " + str(dict['time']))
    print('-----')

# takes a message as a parameter, encodes it to ASCII, generates a hexadecimal digest and returns the value to the caller.
def sha256(message):
    return hashlib.sha256(message.encode('ascii')).hexdigest()
