

#construct hashmap mapping brothers hashed UID to their name
def init_list():
    brothers=open("names_ids.txt")
    #create mapping between id and brother
    id_name_map={}
    for pairing in brothers:
        pair=pairing.split(":")
        UID=pair[1].replace("\n", "")
        NAME=pair[0]
        #add to map
        id_name_map[UID]=NAME
    return id_name_map

def hash_func(id):
    multiplier=1
    hash_value=0
    for num in id:
        print(str(int(num)))
        hash_value+=pow(int(num), multiplier)
        
        multiplier+=1

    return hash_value



#main method
def main():
    print("Event Starting\n")

    #id_name_map is the mapping between a brothers UID and their name
    id_name_map=init_list()
    print(id_name_map)


    while(1):
        #recieve
        brother_id=input()
        #strip issue number off of id
        brother_id=brother_id[:9]
        print(brother_id)
        print(hash_func(brother_id))

main()
