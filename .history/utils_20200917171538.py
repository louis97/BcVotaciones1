
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

