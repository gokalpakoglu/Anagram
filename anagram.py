import random


def create_anagram(firststring):
    firststring_char = []
    for i in firststring:
        firststring_char.append(i)
    createrandomstring = ''.join(random.sample(firststring_char, len(firststring_char)))
    return createrandomstring


def bubble_sort(index):
    for i in range(len(index)):
        for j in range(len(index) - i - 1):
            if index[j] > index[j + 1]:
                index[j], index[j + 1] = index[j + 1], index[j]
    return index


def compare2str(firststring, secondstring):
    if len(firststring) == len(secondstring):
        s1_convert = str2chr2int(firststring)
        s2_convert = str2chr2int(secondstring)
        firststring_sort = bubble_sort(s1_convert)
        secondstring_sort = bubble_sort(s2_convert)
        ok = True
        for index in range(len(firststring_sort)):
            if firststring_sort[index] == secondstring_sort[index]:
                ok = True
            else:
                ok = False
                break
    else:
        print("The lengths of the strings are not the same.")
        ok = False
    return ok


def str2chr2int(string):
    convertchar = []
    for i in string:
        convertchar.append(i)
    convertint = [ord(x) for x in convertchar]
    return convertint


def int2chr2str(asci):
    convertchar = [chr(ch) for ch in asci]
    convertstr = ''
    for i in convertchar:
        convertstr += i
    return convertstr


def main():
    print("Enter two strings to find out if strings are anagrams or not!")
    print("If you enter a string the program will fill the other string!")
    firststring = input("Please enter first string:")
    secondstring = input("Please enter second string:")

    if secondstring == '':
        print("You did not write the second string and the program filled the second string!")
        secondstring = create_anagram(firststring)

    print("First String:", firststring)
    print("Second String:", secondstring)
    print("Sorted version of the entered string:", int2chr2str(bubble_sort(str2chr2int(firststring))))
    print("sorted version of the entered string:", int2chr2str(bubble_sort(str2chr2int(secondstring))))

    if compare2str(firststring, secondstring):
        print("The strings you entered are anagrams!")
    else:
        print("The strings you entered did not match!")


main()
