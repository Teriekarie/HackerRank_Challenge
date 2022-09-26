# python program to show data types
# define a function to store the variables
def hidden_number():
    # The first line contains an integer that you must sum with i.
    integer = input()
    # The second line contains a double that you must sum with d.
    double = input()
    # The third line contains a string that you must concatenate with s.
    string_1 = input ()

    #defining the variables
    i = 4
    d = 4.0
    s = 'HackerRank '
    sum_int = int(integer) + i # new integer
    double_d = float(double) + d # new double
    sentence = s + '' + string_1 # new sentence
    print('{0}\n{1:0.1f}\n{2}'.format(sum_int, double_d, sentence)) # prints all the statements on new lines

hidden_number()