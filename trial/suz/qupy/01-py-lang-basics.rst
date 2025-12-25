.. code:: ipython2

    from collections import OrderedDict
    from ftplib import print_line
    from heapq import merge
    from operator import concat
    
    from pydantic_core.core_schema import list_schema
    
    900/7
    
    2 * 3 == 6
    

.. code:: ipython2

    2 ^ 3

.. code:: ipython2

    # Exponent
    2 ** 3

.. code:: ipython2

    #taken as sring!
    x = input(prompt='x =')
    print("You inputted", x)
    print('Type of x=' + str(type(x)))
    y = int(x) * 2
    print('your output: 2x= ', y)

.. code:: ipython2

    # define pi
    pi = 3.14159
    print(pi)

.. code:: ipython2

    # String - str
    print(str(pi))
    print(len(str(pi)))
    
    
    

.. code:: ipython2

    myStr = "0123456789"
    print("myStr[0]: ", myStr[0])
    
    #Slicing (substring)
    print("\n==== slicing %s =======" % myStr)
    print("myStr[4:]: ", myStr[4:])   # 4th-ind to end
    print("myStr[:6]: ", myStr[:6])   # start to (6-1)th-ind
    print("myStr[-4:]: ", myStr[-4:]) # (n-4)th to end
    print("myStr[:-6]: ", myStr[:-6]) # start to ((n-6)-1)th-ind
    
    print("myStr[2:3]: ", myStr[2:3])    # 2nd to 3rd
    print("myStr[-2:-3]: ", myStr[-2:-3])  # (n-2)nd to (n-3-1)th
    
    '''
    Output:
    myStr[0]:  0
    
    ==== slicing 0123456789 =======
    myStr[4:]:  456789
    myStr[:6]:  012345
    myStr[-4:]:  6789
    myStr[:-6]:  0123
    myStr[2:3]:  2
    myStr[-2:-3]:
    '''

.. code:: ipython2

    myStr = "0123456789"
    
    #Slicing (substring)
    print("\n==== slicing and skip-iterating %s =======" % myStr)
    print("myStr[4::3]: ", myStr[4::3], '  #4th-ind to end, i+=3')
    print("myStr[:6:2]: ", myStr[:6:2], '  # start to (6-1)th-ind, i+=2')
    print("myStr[-4::1]: ", myStr[-4::1], '  # (n-4)th to end, i++')
    print("myStr[:-6:2]: ", myStr[:-6:2], '  # start to ((n-6)-1)th-ind, i+=2')
    
    print("myStr[2:3:2]: ", myStr[2:8:2], '  #2nd to 8th, i+=2')
    print("myStr[-2:-3:2]: ", myStr[-2:-3:2], '  #(n-2)nd to (n-3-1)th, i+=2')
    print("myStr[::-1]: ", myStr[::-1], '  #end to start (reverse), given i-=1')
    
    '''
    Output:
    ==== slicing and skip-iterating 0123456789 =======
    myStr[4::3]:  47   #4th-ind to end, i+=3
    myStr[:6:2]:  024   # start to (6-1)th-ind, i+=2
    myStr[-4::1]:  6789   # (n-4)th to end, i++
    myStr[:-6:2]:  02   # start to ((n-6)-1)th-ind, i+=2
    myStr[2:3:2]:  246   #2nd to 8th, i+=2
    myStr[-2:-3:2]:     #(n-2)nd to (n-3-1)th, i+=2
    myStr[::-1]:  9876543210   #end to start (reverse), i-=1
    '''

.. code:: ipython2

    my_name = 'sujeet banerjee_hi  '
    print('I am: ', my_name.capitalize())
    print('Again: ', my_name)
    
    # to list from str
    print(my_name.split())
    
    # Upper (all caps)
    print(my_name.upper())
    
    print('Myself five times: ', my_name * 5)
    
    
    # strip spaces
    print('Myself: ', my_name.strip())
    print('Myself: ', my_name.rstrip())
    
    '''
    Output:
    I am:  Sujeet banerjee_hi
    Again:  sujeet banerjee_hi
    ['sujeet', 'banerjee_hi']
    SUJEET BANERJEE_HI
    Myself five times:  sujeet banerjee_hi  sujeet banerjee_hi  sujeet banerjee_hi  sujeet banerjee_hi  sujeet banerjee_hi
    Myself:  sujeet banerjee_hi
    Myself:  sujeet banerjee_hi
    '''

.. code:: ipython2

    #List
    ## Append mutates the list
    mlist = [1, 2, 'hihi', [3, 4], {'a':'1', 'b':'2'}]
    print(mlist)
    mlist.append(10)
    mlist.append([20, 30])
    print(mlist)
    mlist.reverse()
    # Won't work!
    # mlist.sort()
    print(mlist)
    
    '''
    Output:
    [1, 2, 'hihi', [3, 4], {'a': '1', 'b': '2'}]
    [1, 2, 'hihi', [3, 4], {'a': '1', 'b': '2'}, 10, [20, 30]]
    [[20, 30], 10, {'a': '1', 'b': '2'}, [3, 4], 'hihi', 2, 1]
    '''
    
    

.. code:: ipython2

    from collections import OrderedDict
    #Dict
    
    #Make a dict
    my_dict = {"a": 1, "b": 2, "c": 3}
    print(my_dict)
    print(my_dict.keys())
    print(my_dict.values())
    print(my_dict.items())
    
    new_dict = OrderedDict(my_dict.items())
    new_dict.update({"t":4})
    new_dict.move_to_end('a', last=True)
    print("Rearranged: ", new_dict)
    print("Popped: ", new_dict.popitem())
    print(new_dict)
    
    '''
    Output:
    {'a': 1, 'b': 2, 'c': 3}
    dict_keys(['a', 'b', 'c'])
    dict_values([1, 2, 3])
    dict_items([('a', 1), ('b', 2), ('c', 3)])
    Rearranged:  OrderedDict({'b': 2, 'c': 3, 't': 4, 'a': 1})
    Popped:  ('a', 1)
    OrderedDict({'b': 2, 'c': 3, 't': 4})
    '''

.. code:: ipython2

    ## Zippin
    zip
    # TBD

.. code:: ipython2

    # Sets
    my_set = set(['a', 'c', 'c', 'd', 'e', 'f', 'g', 'h'])
    print(my_set)
    print(my_set.intersection({'a', 'l', 'c'}))
    print(my_set)
    

.. code:: ipython2

    my_tuple = ('a', 1, 2, 'b', 'a')
    print(my_tuple)
    print(my_tuple[0])
    my_tuple2 = ('a', 1, 2, 'b', 'a')
    print("Added Tuples: ", my_tuple2 + my_tuple)
    print("Repeated Tuples into one:", my_tuple2 * 3)
    print("Repeated Tuples into one (Count):", (my_tuple2 * 3).count('a'))
    
    """
    Output:
    ('a', 1, 2, 'b', 'a')
    a
    ('a', 1, 2, 'b', 'a', 'a', 1, 2, 'b', 'a')
    ('a', 1, 2, 'b', 'a', 'a', 1, 2, 'b', 'a', 'a', 1, 2, 'b', 'a')
    """
    

.. code:: ipython2

    #Boolean
    
    bool_a = True
    print(bool_a == True)
    val = input("Enter any key to exit:")
    print(bool(val))
    
    print("a and not(a): ", (bool_a and not bool_a))
    
    condition = True
    condition2 = False
    if condition:
        print("Condition: True")
    elif not condition2:
        print("Condition2: False")
    else:
        print("No other case!")
    
    x = 0 if condition2 else 1
    print(x)
    
    

.. code:: ipython2

    #Boolean 'in' operator
    
    my_dict = {"a": 1, "b": 2, "c": 3}
    if 'a' in  my_dict:
        print("'a' in my_dict")
    
    if 'b' in  my_dict.keys():
        print("'b' in my_dict")
    
    # Incorrect intent, as 2 is part of values!
    if 2 in  my_dict:
        print("2 in my_dict")
    else:
        print("2 in not my_dict as keys!")
    
    if 2 in  my_dict.values():
        print("2 in my_dict.values")
    else:
        print("2 in not my_dict.values")
    
    

.. code:: ipython2

    for e in myStr:
        print(e)
    
    # This is also correct (as tuple):
    ## for (k,v) in my_dict.items():
    for k,v in my_dict.items():
        print(k, ' --> ', v)
    # The above works for list of tuples as well!
    
    # Print the tuples (items)
    for y in my_dict.items():
        print(y)
    
    print('List from dict.values', [y for x,y in my_dict.items()])
    
    

.. code:: ipython2

    for x in range(10):
        # I am undecided yet, what to write!
        pass
    
    my_dict = {"a": 1, "b": 2, "c": 3}
    print(my_dict)
    print("Popped by key 'b'", my_dict.pop('b'))
    print("Popped rightmost: ", my_dict.popitem())
    print('Mutated dict: ', my_dict)
    
    # Iterate from 8 to 9 (indices), no-skips
    for x in range(8, 10):
        # I am undecided yet, what to write!
        print(x)
    print("-----------\n")
    
    # Iterate from 5 to 9 (indices), i+=2
    for x in range(5, 10, 2):
        # I am undecided yet, what to write!
        print(x)
    
    

.. code:: ipython2

    #String formatting
    for num in range(4):
        s = f"I am at the number {num}"
        print(s)

.. code:: ipython2

    # enumeration - creates a wrapper over a list to enumerate it
    for num in enumerate(range(6, 10)):
        s = f"I am at the number {num}"
        print(s)
    
    print("-----------\n")
    
    for idx, num in enumerate(list(range(6,10))):
        s = f" *I am at [{idx}] --> the number {num}"
        print(s)
    
    my_dict = {"a": 1, "b": 2, "c": 3}
    for idx, entry in enumerate(my_dict):
        print(idx, "-->", entry)
    

.. code:: ipython2

    #RANDOM
    from random import randint
    from random import randrange
    from random import shuffle
    
    print(randint(1,10))
    print(randrange(1,10))
    print("-----------\n")
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffle(my_list)
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Random shuffle - mutates ths list
    shuffle(my_list)
    for rnd in my_list:
        print(rnd)
    

.. code:: ipython2

    # Zip multi lists
    
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    l3 = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    
    zipped = zip(l1, l2, l3)
    print(zipped)
    print([zipped])
    print(enumerate(zipped))
    
    # Using list(zipped(..)) somehow corrupts the zip
    #print(list(zipped))
    
    print("-----------\n")
    
    ## The zip elements disappear if iterated once!!!
    # for x in list(zipped):
    #     print(x)
    #
    # for x in list(zipped):
    #     print(x)
    print("-----------\n")
    
    for i, x in enumerate(list(zipped)):
        print(f"[{i}] ==> {x}")
    

.. code:: ipython2

    #Str to char-lisr
    chars = [ch for ch in myStr]
    print(chars)
    
    # same effect
    chars = list(ch for ch in myStr)
    print(chars)

.. code:: ipython2

    #Function, function as code
    import numpy
    help(numpy.fft)

.. code:: ipython2

    #Function. without 'return' the function returns NoneType
    # Variable args
    
    def func(*args, **kwargs):
        print('args:', args, ' len:', len(args))
        print('kwargs:', kwargs, ' len:', len(kwargs))
        print('Fourth arg:', args[3])
    
        # Incorrect: Can potentially give 'keyerror'!!!
        if kwargs['mymy'] is not None:
            print('Kwarg mymy=:', kwargs['mymy'])
    
        # Incorrect: Can potentially give 'keyerror'!!!
        #
        # if kwargs['pepe'] is not None:
        #     print('Kwarg pepe=:', kwargs['pepe'])
    
        # Incorrect: Can potentially give 'keyerror'!!!
        #
        # if kwargs['pepe']:
        #     print('Kwarg pepe=:', kwargs['pepe'])
    
        #correct!
        if 'pepe' in kwargs:
            print('Kwarg pepe=:', kwargs['pepe'])
    
        if 'some' in kwargs:
            print('Kwarg some=:', kwargs['some'])
    
        return
    
    func(1, 2, 3, {1, 2, 3}, [3, 4, 5], my_dict, (), \
         mymy=2, some="yoyo!"
         )

.. code:: ipython2

    #Map Reduce - tuples as aggregates
    from functools import reduce, partial
    
    my_list = [2, 1, 5, 10, 3, 6, 7, 9, 8, 4]
    
    # Map function
    def divide_by_five(x):
        return x / 5
    
    #Reduce function
    def add_to(res, x):
        #print(f"Received: aggregate={res} | x={x}")
        return res+x
    
    def add_reduce(val_str:tuple, x):
        #print(f"Received: v_s={val_str} | x={x}")
        (v, s) = val_str
        #print("v=", v)
        #print("s=", s)
        # Return the aggregate-tuple
        return v+x, f"{x} + {s if len(s) != 0 else 'nil'}"
    
    mmap = map(divide_by_five, my_list)
    print(mmap)
    # The correct one!
    print(list(mmap))
    print([mmap])
    
    print("List: ", my_list)
    # reduce-fn, list, initial-value
    red = reduce(add_to, my_list, 100)
    print(red)
    
    print("List: ", my_list)
    # Aggregate can be tuple or anything!
    red = reduce(add_reduce, my_list, (0, ""))
    print(red)
    
    '''
    Output:
    
    <map object at 0x000001107FCA0820>
    [0.4, 0.2, 1.0, 2.0, 0.6, 1.2, 1.4, 1.8, 1.6, 0.8]
    [<map object at 0x000001107FCA0820>]
    List:  [2, 1, 5, 10, 3, 6, 7, 9, 8, 4]
    155
    List:  [2, 1, 5, 10, 3, 6, 7, 9, 8, 4]
    (55, '4 + 8 + 9 + 7 + 6 + 3 + 10 + 5 + 1 + 2 + nil')
    '''
    print()

.. code:: ipython2

    #Lambda
    # ':' instead of '->'
    print (reduce(lambda res, x : res + x, my_list))

.. code:: ipython2

    #Class; Python special methods of form: __xxx__()
    
    class Game:
        # Akin to static variables in Java
        bb = 'cc'
    
        def __init__(self, name, numPlayers):
            # Akin to class-member variables in Java
            self.name = name
            self.numPlayers = numPlayers
            self.players = []
    
        def addPlayer(self, player):
            self.players.append(player)
    
        # That's Java, not Python!
        def toString(self):
            print(self.name)
    
        # len(game_instance) return the number of players
        def __len__(self):
            return len(self.players)
    
        # Py equivalent of toString
        def __str__(self):
            return f"Game ==> \n  Name: {self.name}, \n  Players: \
                \n       {self.players}"
    
    class Player:
        def __init__(self, name, gender, age):
            self.name = name
            self.gender = gender
            self.age = age
            self.score = 0
    
        def getScore(self):
            return self.score
    
        def __str__(self):
            return f"Player {self.name} --> score: {self.score}"
    
    
    #Inerited
    class SuperPlayer(Player):
    
        #Override
        def getScore(self):
            return -1
    
    # Instantiate
    gg = Game('yoyo', 3)
    gg.addPlayer(Player('John', 'male', 18))
    gg.addPlayer(Player('Merlin', 'female', 18))
    gg.addPlayer(SuperPlayer('Suppa Rao', 'male', 18))
    
    # No Protection!!!
    # print(gg.name)
    # gg.name = "garbage"
    # print(gg.name)
    print(gg)
    print(len(gg))
    print(gg.players[0])
    
    # Akin to static variables in Java
    print(Game.bb)

.. code:: ipython2

    # try-except-else-finally-raise!
    x = -1
    max_attempts = 4
    while True:
        inp = input("Enter a number: ")
        try:
            x = int(inp)
        except:
            if max_attempts <= 0:
                raise Exception("Too many incorrect attempts, \
                    baling out!")
    
            max_attempts -= 1
            print("Invalid input %s. Enter a number." % inp)
    
            continue
        else:
            # INCORRECT PLACE:
            # if max_attempts <= 0:
            #     raise Exception("Too many incorrect attempts.\
            #  Baling out!")
            break
        finally:
            # Close all streams, DB conncetion etc
            pass
    print('Your input:', x)

.. code:: ipython2

    l1 = [1,2,3]
    l2 = [10, 20]
    print(l1.append(l2))
    print(l1)
    
    #print(merge(l1, l2))
    print(list(zip(l1, l2)))
    
    #concat(l1, l2)
    
    l2 = ['b', 'a', 'e']
    l2.insert(2, 'b')
    print(l2)
    

.. code:: ipython2

    'python'[3]
    
    for i in range(10):
        continue
        break
    
    2**3
    
    [range(10)]
    list(range(5, 16))
    #list()
    
    
