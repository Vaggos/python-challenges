#!/usr/bin/python3

# @Author: Vagelis Prokopiou
# @Email: drz4007@gmail.com
# @Date:   2016-04-02 17:56:21

# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

def xyz_there(str):
  str = str.replace('.xyz', '')
  if 'xyz' in str:
    return True
  return False


print(xyz_there('hello my . xyz.welcome here'))

