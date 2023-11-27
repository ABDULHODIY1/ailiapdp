def sozni_ikkilik_sanoqga_otkazib_yoz(bersoz):
    ikkilik_sanoq = ' '.join(format(ord(x), 'b') for x in bersoz)
    return ikkilik_sanoq

def ikkilik_sanoqni_qayta_oqib_chiqar(ikkilik_sanoq):
    soz = ''.join(chr(int(x, 2)) for x in ikkilik_sanoq.split())
    return soz
with open("OAPAPICode.codeprotsess","r")as mcode:
    machinecode=mcode.read()
ikkilik_sanoq = machinecode
qayta_oqib_chiqarilgan_soz = ikkilik_sanoqni_qayta_oqib_chiqar(ikkilik_sanoq)
# print(f"Qayta oqib chiqarilgan so'z: {qayta_oqib_chiqarilgan_soz}")
with open("OAPAPICode.codeprotsess","w") as machine_code:
    machine_code.write(ikkilik_sanoq)

# sozni_ikkilik_sanoqga_otkazib_yoz("")
