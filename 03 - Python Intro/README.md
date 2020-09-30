# Explanation about the exercises. Going about what we learned in class, easy stuff.

## First Challenge
Sets are grouping variables that unlike lists don't accept duplicites, _but_ are iterables. So by creating a set we can run through it and then check how many times is given object **in** a list. That's a favorite of the pythonic crew. The **in** will check if such element is inside the referenced list and return true if positive.

## Second Challenge
Simple arithmetic script. Receive a number and multiply it to obtain the seconds. Important to remember that the **return** command means you can apply the function to an empty variable and that variable will _assume_ the result, meaning it won't be **empty** anymore.
´´´
x = function(something)
´´´
That means that now the variable "x" has the value attributed by the function.

## Third Challenge
Same logic on the first challenge, remove duplicates by creating a set and then re-transform it to a list to sort it. Important to remember that the **sort()** standard method sorts the items by ascending order. To have descending use _.sort(reverse=True)_

## Fourth Challenge
Well, this is also possible without list slicing, but it's a one-liner, we all love this. The important thing here is that strings can be iterate through just like lists. The logic behind it:
´´´
string[Start:End:Step]
´´´
By not putting anything at _start_ or _end_ (that's what the ":" means) what Python interprets that as is **start at the very first number and end at the very last**.

## Fifth Challenge
Another one-liner. Create a set and return it, you should be used to it by now.

## Sixth Challenge
The problem requires no repetition from items, so we create two sets. _But_, here's where it gets interesting! I made a mistake. I thought if the **len()** of the lists could be different, then you might have a problem, but turns out not, so I just left it there out of laziness.

## Seventh Challenge
Two lists and you need to create a new one from the items which are not on one of them. That's easy, you just make sure that **a** is the biggest list and compare it to the filtered one. Whatever it's not there should be on the new list.

## Eighth Challenge
This one actually took me some time to solve it. The big thing is that you have to read the file. Some people use _file.open()_ but then they have to _file.close()_ the file. With _open with()_ there is no need to close it, that executes by itself, and according to the internet should be the **good way** to solve things. So we use _with open()_, read the file, and then save each line of the text as a list, _but_... we also have to split the words into different words in order to save into our solution list:

´´´
lines.split(" ")
´´´
That does the tricky wonderfully. And then, for each split word we have on our line, we eliminate the _""_ and _"\n"_ which are nothing else but line breaks and empty spaces. But it isn't over, now we have to use the **sorted()** command which is different from the **sort()**. I actually didn't know this command, so it was pretty fun. What **sorted()** does is reteurning a list (duh, sorted), except, similar to the _map()_ function, you can input a specific function to choose how to sort it.

You'll notice we also used the _sol[:10]_ to choose only the first 10 items (starting at 0, ending at 9) to show the top-10.

**Problems:** The code doesn't separate words with a _-_ on them, and grammatical errors also get by, such as _'language.Its'_. I'll think of a way to mitigate this (or not).

## Ninth Challenge
Uhhh, multiplication questions! Love those. Not a one-liner, but pretty simple. Choose where does your code stop and then run it in a _for loop_ with a _range_ to generate the iterables. What else, what else, what else... Ah, of course, _x%3_ and _x%5_ to make sure you're getting the multiples. In this case we haven't excluded **0** because it won't affect the sum, so who cares.

## Tenth Challenge
Split the list in three qual parts... First thing I wrote a generic function, so it doesn't matter the len of the function (although it won't be pleasible if you don't input an **even number**. So watch out for that. If you do input an even number, then basically we get the len, split it into three, make sure the division is an **int**, otherwise it won't work in the _for loop with range_ and then get the list size by slicing throught it.
´´´
x = 9, for example.
x /= 3 --> 3.
list = [1,2,3,...,9].
list1 = [:3]
list2 = [3:6]
list3 = [6:9]
´´´
And there you go.

**Things to improve:** Since the OP asked to create 3 lists, then we are limited by that... _had_ he asked for something different, like, say, **split into the highest even number possible**, then we need to probably use the _globals_ to create global lists from within the loop.

## Eleventh Challenge
Get the number of even numbers and uneven. Same thing we did with the multiples of 3 and 5, except now we **exclude the 0** because otherwise it will count it as even, and then add + 1 to our _par_ and _impar_ counters.

## Twelfth Challenge
This was fun. I'm not sure if this is the most pythonic way to solve it, but I hope it is. Simply run the string modules _isalpha()_, _isnumeric()_ and all the other brothers to check if the given string is only composed of one type of variable or if all the strings are lower or upper. If all of that fails, then your password is fine.
