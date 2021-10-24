import samino

def report_community(reason: str):
    client = samino.Client(None)
    client.login(email=input("Email >> "), password=input("Password >> "))
    community_info = client.get_from_link(input("Community Link >> "))
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
        client = samino.Client(None)
        client.login(email=input("Email >>"), password=input("Password >> "))
        user_info = client.get_from_link(input("User Link >> "))
        object_Id = user_info.objectId
        com_Id = user_info.comId
        local = samino.Local(comId=com_Id)
        while True:
            try:
                local.flag(reason=reason, flagType=5, userId=object_Id)
                print("Report Sended")
            except:
                print("Report Don't Sended")
                pass

    elif select == "2":
        client = samino.Client(None)
        emails = open("emails.txt", "r")
        password = input("Password For All Accounts >> ")
        user_Info = client.get_from_link(input("User Link >> "))
        object_Id = user_info.objectId; com_Id = user_info.comId
        for line in emails:
            email = line.strip()
            try:
                client.login(email=email, password=password)
                client.join_community(com_Id)
                local = samino.Local(comId=com_Id)
                local.flag(reason=reason, flagType=5, userId=object_Id)
                print(f"{email} Sended Report")
            except Exception as e:
                print(e)
