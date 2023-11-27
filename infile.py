def sozni_ikkilik_sanoqga_otkazib_yoz(berilgan_soz):
    ikkilik_sanoq = ' '.join(format(ord(x), 'b') for x in berilgan_soz)
    with open("OAPAPICode.codeprotsess",'w') as machinecode:
        machinecode.write(ikkilik_sanoq)
    print(ikkilik_sanoq)
    return ikkilik_sanoq
sozni_ikkilik_sanoqga_otkazib_yoz(input("KALIT SOZI:"))


