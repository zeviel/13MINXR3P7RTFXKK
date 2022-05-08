import pyfiglet
from animalsay.utils import say
from report_configs import report_functions
from colored import fore, back, style, attr
attr(0)
print(fore.TURQUOISE_2 + style.BOLD)
print("""Script by deluvsushi
Github : https://github.com/deluvsushi""")
print(pyfiglet.figlet_format("13MINXR3P7RTFXKK", font="small"))
say("cat", """[C] Report Community
[U] Report User""")
select = input("Select >> ")

if select == "C":
	reason = input("Reason >> ")
	report_functions.report_community(reason=reason)
	
elif select == "U":
	reason = input("Reason >> ")
	report_functions.report_user(reason=reason)
