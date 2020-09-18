import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import binascii
from utils import *

class Client:
    def __init__(self):
        random = Crypto.Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

# We now develop the mine function that implements our own mining strategy. 
# Our strategy in this case would be to generate a hash on the given message that is prefixed with a given number of 1’s. 
# The given number of 1’s is specified as a parameter to mine function specified as the difficulty level.
# If you specify a difficulty level of 2, the generated hash on a given message should start with two 1’s - like 11xxxxxxxx. 
# If the difficulty level is 3, the generated hash should start with three 1’s - like 111xxxxxxxx.
# Note that the generated digest starts with “11”. 
# If you change the difficulty level to 3, the generated digest will start with “111”, and of course, it will probably require more number of iterations. 
# As you can see, a miner with more processing power will be able to mine a given message earlier. 
# That’s how the miners compete with each other for earning their revenues.
def mine(message, difficulty=1):
    assert difficulty >= 1
    prefix = '1' * difficulty
    print('entra a mine')
    for i in range(1000):
        # print(i)
        digest = sha256(str(hash(message)) + str(i))
        if digest.startswith(prefix):
            print ("after " + str(i) + " iterations found nonce: "+ digest)
            return digest
