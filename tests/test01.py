#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 15:30:51 12-11-2021
# @Author  : Ivan Yastrebov (esim.i2p@gmail.com)
# @Link    : https://github.com/easy-quest
# @Version : $Id$

import os
from os import system as cmd
from dotenv import load_dotenv
load_dotenv()
# my_secret = os.environ.get('TOKEN', 'ad96fe5b51f6d9c0bd241bc4cb01afc7af0e507be9eb7e2b0995a71aa35bd2fc263537ac736d8e41fd35b')

# my_secret2 = os.getenv('TOKEN2', '448b9ddff7c3452cad49aeea52a0bc3e7c4102f8c6b13c01fab8a66e070acdf60b0a1b56cbb25f78a6e19')
# print(my_secret)

# print(token)

# cmd('direnv allow')
# cmd('echo ${token}')                                                                                                                                                                                                                               s

# zzz = 'Easy quest'

my_secret = os.environ['TOKEN']



print(my_secret)