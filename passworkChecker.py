import re

SIZE_HASH = 13
hash_list = [0] * SIZE_HASH


def bloom_filter(file_name):
    """Generates hash table 
        linear probing incase of collisions
    
    Arguments:
        file_name {[String]} -- [File stores passwords that cannot be accepted]
    """    
    with open(file_name, 'r') as f:
        file_contents = f.readlines()
        for file_content in file_contents:
            hash_value = hash(file_content)
            #print(f'{file_content} : {hash_value}')
            if hash_value >-1:
                #linear probing
                flag = hash_value
                while hash_list[hash_value] >0:
                    hash_value = hash_value+1
                    if hash_value != flag: 
                        if hash_value>12:
                            hash_value = 0
                    else:
                        break
                hash_list[hash_value]=1
        print(hash_list)


#function to calculate hash value of string
def hash(string):
    """Calculates hash value 
    
    Arguments:
        string {[String]} -- [Unacceptable/Potential password]
    
    Returns:
        [integer] -- [Hash value]
    """    
    hash_value = -1
    regex = re.compile('[^A-Z]')
    string = regex.sub('',string)
    if string != '':
        hash_value = 0
        for s in string:
            hash_value = hash_value+ord(s)
        #take modulo to limit the range of hash values
        while hash_value>SIZE_HASH:
            hash_value=hash_value%SIZE_HASH
    return hash_value


if __name__ == "__main__":
    bloom_filter('dictionary.txt')
    password = input("Enter new password: \n")
    password_hash = hash(password)
    while hash_list[password_hash]>0:
        password = input("The password you just entered is unacceptable, enter new password: \n")
        password_hash = hash(password)

    print("Your password has been changed.")


