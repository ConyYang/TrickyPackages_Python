
# Python Tricky Packages Illustration

### 1. Argparse Example
![Code](argparse_example)</br>

This piece of code show show to use terminal commands to
pass in arguments and run the code.
```console
user$: python cylinderArgparse.py -R 2 -H 4
Volume of cylinder 50.2654824574
```

### 2. Config Parser Example
![Code](configParser_example)</br>

We have a bank.ini file which contains 3 sections,
which are [account], [client] and [bank].

We create an object ConfigTest to initiate, print message 
and update a config file.
```
user$: python config_file_create.py
['account', 'client', 'bank']
<Section: account>
['status', 'id', 'pin']
7253
['account', 'client', 'bank']
<Section: account>
['status', 'id', 'pin']
7253
```

### 3. Python Multiprocessing
![code](PythonMultiprocessing)</br>

pythonMultiprocess.py use package multiprocess. We join 5 processes 
each sleep for 1.5 seconds. Use multiprocess, these 5 processes run concurrently, hence
the process only takes about 1.518s to complete.
```console
user$: python pythonMultiprocess.py
Start sleeping for 1.5 second
Start sleeping for 1.5 second
Start sleeping for 1.5 second
Start sleeping for 1.5 second
Start sleeping for 1.5 second
Done Sleeping...
Done Sleeping...
Done Sleeping...
Done Sleeping...
Done Sleeping...

Program finished in 1.5178664039999998 second(s)
```
future.py use package concurrent.futures. We also use list comprehension
and map method in this illustration. We don't need join. concurrent.futures.ProcessPoolExecutor()
will help us to automatically handle every thing.
``` console
user$: python future.py
Start sleeping for 5 second
Start sleeping for 4 second
Start sleeping for 3 second
Start sleeping for 2 second
Start sleeping for 1 second
Done Sleeping...5
Done Sleeping...4
Done Sleeping...3
Done Sleeping...2
Done Sleeping...1
Program finished in 5.047921654 second(s)
```

### 4. Python OOP features
![code](pythonOOPfeatures)</br>

In this section, we create some Employee topic objects to show how we
use python oop features.
We illustrate:
 - Class and Object
 - Class Variable
 - Class Static Method
 - Class Inheritance
 - Special Method
 - Property Decorator
 
### 5. Random Practice
![code](randomPractice)</br>

In this section, we show how we can use random package.
We show method random.random(), random.uniform(), random.randint() and
random.choice().

### 6. Turtle
Draw some basic shapes using turle package.


