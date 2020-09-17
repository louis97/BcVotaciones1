import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
import pylab as pl
import logging
import datetime
import collections
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from client import *
from transaction import *

Dinesh = Client()
Ramesh = Client()
t = Transaction(
   Dinesh,
   Ramesh.identity,
   5.0
)
signature = t.sign_transaction()
print (signature) 