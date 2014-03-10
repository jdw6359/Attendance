

def hash_func(id):
    multiplier=1
    hash_value=0
    for num in id:
        hash_value+=pow(int(num), multiplier)
        multiplier+=1
    return hash_value

def main():
        f=open('names_ids.txt','a')
        print("File opened")



        while(1):
                option=input("Press \'y\' to add new brother.\nAny other input will cancel")
                if(option=='y'):
                        brother_name=input("Brother Name: ")
                        brother_id=input("Please Scan RIT ID")
                        brother_id=brother_id[:9]
                        brother_hash=hash_func(brother_id)
                        print("University ID: "+str(brother_id))
                        f.write(str(brother_name)+":"+str(brother_hash)+'\n')
                        print(brother_name+" added to file\n\n")
                else:
                        print("closing program")
                        f.close()
                        break
                        
main()        
        
