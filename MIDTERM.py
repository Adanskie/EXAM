data = []

def Menu():
    print("=========Menu========")
    print("Press [1] SHOW ALL DATA")
    print("Press [2] ADDED SINGLE DATA")
    print("Press [3] ADDED MULTIPLE DATA")
    print("Press [4] DELETE")
    print("Press [5] DELETE ALL DATA")
    print("Press [6] UPDATE DATA")
    print("Press [7] EXIT")

def Show_All_Data():
    if data:
        print()
        num = 0
        for get_value in data:
            print(num , " " , get_value)
            num += 1
        print()
    else:
        print("\n================")
        print("DATA WAS NO VALUE")
        print("================\n")

def Added_Single_Data():
    user_add = input("Enter value for Single Data : ")
    data.append(user_add)
    print("\n==========================")
    print("Success adding Single Data")
    print("==========================\n")

def Added_Multiple_Data():
    number = int(input("Enter a number How much multiple data you want : "))
    for _ in range(number):
        user_added = input("Enter Value for multiple data : ")
        data.append(user_added)
    print("\n===============================")
    print("Success Adding multiple data")
    print("===============================\n")

def Delete():
    num = 0
    if data:
        for get_data in data:
            print(num , " " , get_data)
            num += 1
        choices = int(input("choice index number to delete : "))
        delete = data.pop(choices)
        print("\n===========================")
        print(f"Success delete -> {delete}")
        print("===========================\n")
    else:
        print("\n=================")
        print("Something Wrong")
        print("=================\n")

def Delete_all_Data():
    if data:
        print("\n=========================")
        print("Success Delete all Data")
        print("=========================\n")
        data.clear()
    else:
        print("\n===================")
        print("Something Wrong")
        print("===================\n")

def Update_Data():
    if data:
        num = 0
        print("\n========================")
        for get_data in data:
            print(num," -",get_data)
            num += 1
        print("========================\n")

        index = int(input("choice index number for updating : "))
        value = input("Enter value for update : ")
        data[index] = value
        print("\n================================================")
        print(f"Success Update index [{index}] = {value}")
        print("================================================\n")
    else:
        print("\n===================")
        print("Something Wrong")
        print("===================\n")


while True:
    Menu()
    choice = input("choice number : ")

    match choice:
        case "1":
            Show_All_Data()
        case "2":
            Added_Single_Data()
        case "3":
            Added_Multiple_Data()
        case "4":
            Delete()
        case "5":
            Delete_all_Data()
        case "6":
            Update_Data()
        case "7":
            print("EXIT")
            break
