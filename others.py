# import os
# import subprocess
#
# #Telegram Bot Token Encoder
# def Encoder():
#     with open("PAPICode.codecore",'w')as f:
#         PAPICCODE=input("Enter API TOKEN")
#         f.write(PAPICCODE)
#         print("Good saved this token : ")
# # Encoder()
# # Telegram Bot Dekoder
# def Decoder():
#     with open("PAPICode.codecore","r")as fr:
#         x=fr.read()
#
#     return x
#
# def OEncoder():
#     with open("PAPICode.codecore",'w')as f:
#         PAPICCODE=input("Enter API TOKEN")
#         f.write(PAPICCODE)
#         print("Good saved this token : ")
# # Encoder()
# def Decoder():
#     with open("PAPICode.codecore","r")as fr:
#         x=fr.read()
#
#     return x
# Decoder()
#
# def changerToken(type = None):
#     if type == None:
#         print("Stop")
#     elif type == "D.filetype":
#         chose = input("Chose Api Token Cahnger File Name:")
#         A=input("Enter New Token")
#         if chose == "PAPICode.codecore":
#             with open("PAPICode.codecore",'w')as fs:
#                 fs.write(A)
#         elif chose == "PAPICode.codecoreI":
#             with open("PAPICode.codecore",'w')as fs:
#                 fs.write(A)
# a=input("enter")
# if a == "1":
#     changerToken()
# elif a== "2":
#     ch
#
# # api_key=""
# # OpenAI=""

def sozni_ikkilik_sanoqga_otkazib_yoz(berilgan_soz):
    ikkilik_sanoq = ' '.join(format(ord(x), 'b') for x in berilgan_soz)
    return ikkilik_sanoq

def sssddsd(ikkilik_sanoq):
    soz = ''.join(chr(int(x, 2)) for x in ikkilik_sanoq.split())
    return soz

# Berilgan so'z
# berilgan_soz = input("""ENTER TOKEN FOR TELEGRAM BOT""")
with open("PAPICode.codecore","r")as mcode:
    machinecode=mcode.read()
# So'zni ikkilik sanoqga otkazamiz
ikkilik_sanoq = machinecode
# print(f"Berilgan so'z: {berilgan_soz}")
# print(f"Ikkilik sanoq: {ikkilik_sanoq}")

# Ikkilik sanoqni qayta oqib chiqaramiz
qayta_oqib_chiqarilgan_soz2 = sssddsd(ikkilik_sanoq)

print(qayta_oqib_chiqarilgan_soz2)
with open("PAPICode.codecore","w") as machine_code:
    machine_code.write(ikkilik_sanoq)


#
# class OAI:
#     def Decoder(berilgan_soz):
#         ikkilik_sanoq = ' '.join(format(ord(x), 'b') for x in berilgan_soz)
#         return ikkilik_sanoq
#
#     def encoder(ikkilik_sanoq):
#         soz = ''.join(chr(int(x, 2)) for x in ikkilik_sanoq.split())
#         return soz
#
#     # Berilgan so'z
#     berilgan_soz = input("""ENTER TOKEN FOR TELEGRAM BOT""")

    # # So'zni ikkilik sanoqga otkazamiz
    # ikkilik_sanoq = sozni_ikkilik_sanoqga_otkazib_yoz(berilgan_soz)
    # print(f"Berilgan so'z: {berilgan_soz}")
    # print(f"Ikkilik sanoq: {ikkilik_sanoq}")
    #
    # # Ikkilik sanoqni qayta oqib chiqaramiz
    # qayta_oqib_chiqarilgan_soz = ikkilik_sanoqni_qayta_oqib_chiqar(ikkilik_sanoq)
    # print(f"Qayta oqib chiqarilgan so'z: {qayta_oqib_chiqarilgan_soz}")
