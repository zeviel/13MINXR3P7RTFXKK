import amino
import asyncio

async def report_community():
	client = amino.Client()    
	email = input("Email >> ")
	password = input("Password >> ")
	await client.login(email=email, password=password)
	communitylink = input("Community Link >> ")
	communityinfo = await client.get_from_code(communitylink)
	communityid = communityinfo.path[1:communityinfo.path.index('/')]
	while True:
		try:
			await client.flag_community(comId=communityid, reason="Spam, Trolling, Harrasment & Nudity", flagType=110)
			print("Report Sended")
		except:
			print("Report Don't Sended")
			pass

async def report_user():
	print("""[1] Report Using One Account
[2] Report Using Multiply Accounts""")
	select = input("Select >> ")
	
	if select == "1":
		client = amino.Client()
		email = input("Email >> ")
		password = input("Password >> ")
		await client.login(email=email, password=password)
		userlink = input("User Link >> ")
		userinfo = await client.get_from_code(userlink)
		userId = userinfo.objectId
		communityid = userinfo.path[1:userinfo.path.index('/')]
		sub_client = await amino.SubClient(comId=communityid, profile=client.profile)
		while True:
			try:
				await sub_client.flag(reason="Trolling, Pornography, Inappropriate content", flagType=5, userId=userId)
				print("Report Sended")
			except:
				print("Report Don't Sended")
				pass
	
	elif select == "2":
		client = amino.Client()
		emails = open("emails.txt", "r")
		password = input("Password For All Accounts >> ")
		userlink = input("User Link >> ")
		for line in emails:
			email = line.strip()
			try:
				await client.login(email=email, password=password)
				userinfo = await client.get_from_code(userlink)
				userId = userinfo.objectId
				communityid = userinfo.path[1:userinfo.path.index('/')]
				await client.join_community(communityid)
				sub_client = await amino.SubClient(comId=communityid, profile=client.profile)
				await sub_client.flag(reason="Trolling, Pornography, Inappropriate content", flagType=5, userId=userId)
				print(f"{email} Sended Report")
			except amino.lib.util.exceptions.VerificationRequired as e:
				print(f"Verification required for {email}")
				link = e.args[0]['url']
				print(link)
			except Exception as e:
				print(e)
