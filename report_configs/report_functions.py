import aminofix

def report_community(reason: str):
    client = aminofix.Client()
    client.login(email=input("Email >> "), password=input("Password >> "))
    community_info = client.get_from_code(input("Community Link >> "))
    com_Id = community_info.comId
    while True:
        try:
            client.flag_community(comId=com_Id, reason=reason, flagType=110)
            print("Report Sended")
        except Exception as e:
        	print(e)

def report_user(reason: str):
    print(
        """[1] Report Using One Account
[2] Report Using Multiply Accounts"""
    )
    select = input("Select >> ")

    if select == "1":
        client = aminofix.Client()
        client.login(email=input("Email >>"), password=input("Password >> "))
        user_Info = client.get_from_code(input("User Link >> "))
        object_Id = user_Info.objectId; com_Id = user_Info.comId
        sub_client =  aminofix.SubClient(comId=com_Id, profile=client.profile)
        while True:
            try:
                sub_client.flag(reason=reason, flagType=5, userId=object_Id)
                print("Report Sended")
            except Exception as e:
                print(e)
                

    elif select == "2":
        client = aminofix.Client()
        emails = open("emails.txt", "r")
        password = input("Password For All Accounts >> ")
        user_Info = client.get_from_code(input("User Link >> "))
        object_Id = user_Info.objectId; com_Id = user_Info.comId
        for line in emails:
            email = line.strip()
            try:
                client.login(email=email, password=password)
                client.join_community(com_Id)
                sub_client =  aminofix.SubClient(comId=com_Id, profile=client.profile)
                sub_client.flag(reason=reason, flagType=5, userId=object_Id)
                print(f"{email} Sended Report")
            except Exception as e:
                print(e)
