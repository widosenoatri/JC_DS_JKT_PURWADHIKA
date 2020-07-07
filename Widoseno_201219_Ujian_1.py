### #1 ###
def Hashtag(string_input):
    list_words = string_input.split()
    list_final1 = ['#']

    if(len(string_input)>139 or len(string_input)==0):
        # print(False)
        return False
    else:
        for words in list_words:
            words = words.capitalize()
            list_final1.append(words)
    z = ''.join(list_final1)
    # print(z)
    return z
    

print(Hashtag("Hello there how are you doing"))
print(Hashtag("  Hello   World "))
print(Hashtag(""))





### #2 ###
def create_phone_number(number):
    z = '('
    if (len(number)>=10 and len(number)>0):
        for idx in range(len(number)):
            z += str(int(number[idx]))
            if (idx == 2):
                z+=') '
            elif (idx == 5):
                z+='-'
    else:
        # print(False)
        return False

    # print(z)
    return z

print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))





### #3 ###
def sort_odd_even(num):
    dict1 = {}
    list_odd, list_even, list_final = [], [], num
    temp_odd, temp_even = 0, 0
    for idx1 in range(len(num)):
        if (check_oe(num[idx1])):
            list_even.append(num[idx1])
            dict1[idx1] = 'even'
        else:
            list_odd.append(num[idx1])
            dict1[idx1] = 'odd'

    for idx2 in range(len(list_even)):
        for idx2 in range(len(list_even)):
            if (idx2!=len(list_even)-1 and list_even[idx2] < list_even[idx2+1]):
                temp_even = list_even[idx2]
                list_even[idx2] = list_even[idx2+1]
                list_even[idx2+1] = temp_even

    for idx3 in range(len(list_odd)):
        for idx3 in range(len(list_odd)):
            if (idx3!=len(list_odd)-1 and list_odd[idx3] > list_odd[idx3+1]):
                temp_odd = list_odd[idx3]
                list_odd[idx3] = list_odd[idx3+1]
                list_odd[idx3+1] = temp_odd

    index_even = 0
    for item1 in range(len(list_final)):    
        if (dict1[item1] == 'even'):
            list_final[item1] = list_even[index_even]
            index_even += 1

    index_odd = 0
    for item2 in range(len(list_final)):    
        if (dict1[item2] == 'odd'):
            list_final[item2] = list_odd[index_odd]
            index_odd += 1
    
    # print(list_final)
    return list_final

def check_oe(num):
    if num%2 == 0:
        return True
    else:
        return False
        

print(sort_odd_even([5,3,2,8,1,4]))
print(sort_odd_even([2,8,1,4]))
print(sort_odd_even([]))





### #4 ###
def hollowTriangle(num):
    for row in range(0,num):
        z = ''
        for col in range(0, num*2-1):
            if (col+row == num-1 or col-row == num-1 or row == num-1):
                z += '#'
            else:
                z += '_'
        print(z)

hollowTriangle(1)
hollowTriangle(2)
hollowTriangle(3)
hollowTriangle(4)
hollowTriangle(5)
hollowTriangle(6)