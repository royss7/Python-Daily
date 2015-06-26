#!/usr/local/bin/python3

'''
 ********************************************
 * Name        : Code-0001.py
 * Discription : Generate the code for App sell
 * Date        : 2015-06-20
 * Author      : liuyy
 * E-mail      : liuyy2006@163.com
 ********************************************
'''

import random

def unsafe_gen(s):
	i = 0
	one_by_one = False
	while i < 200:
	    if one_by_one:
	        # NOTE : You should assure all the code is unique, so the following 
	        # maybe unsafe.
	        # 1. choose 8 element from s one by one
	        code = ''
	        for j in range(0, 7):
	            #code += s[random.randint(0, len(s)-1)]
	            code += random.choice(s)
	
	        print(code)
	    else:
	        # use random.sample to choose 8 elemets one time
	        print(''.join(random.sample(s, 8)))
	    i += 1

# assure all of codes are unique
def safe_gen(s):
    allcode = set()
    while len(allcode) < 200:
        allcode.add(''.join(random.sample(s, 8)))
    return allcode


if __name__ == "__main__":

    # the code is 8bytes, imclude upper char and digits
    s = [ str(i) for i in range(0, 10)]
    s.extend([chr(i) for i in range(ord('A'), ord('Z') + 1)])
    print(s)
    print(safe_gen(s))



