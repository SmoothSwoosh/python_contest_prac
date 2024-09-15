import sys


encods = ['cp037', 'cp1006', 'cp1250', 'cp1251', 'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257', \
          'cp1258', 'cp437', 'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp864', 'cp866', \
          'cp869', 'cp874', 'cp875', 'hp_roman8', 'iso8859_10', 'iso8859_16', 'iso8859_4', 'iso8859_5', \
          'koi8_r', 'latin_1', 'mac_croatian', 'mac_greek', 'mac_iceland', 'mac_latin2']

procedure = sys.stdin.read()

if procedure.startswith('ПРОЦ') and \
   (procedure.endswith('КНЦ;\n') or procedure.endswith('КНЦ;')):
    print(procedure)
    sys.exit()


decoded = ''
for first_code in encods:
    tmp0 = procedure
    try:
        tmp1 = tmp0.encode(first_code)
    except:
        continue
    try:
        decoded = tmp1.decode('koi8-r')
    except:
        pass
    if decoded.startswith('ПРОЦ') and \
       (decoded.endswith('КНЦ;\n') or decoded.endswith('КНЦ;')):
        print(decoded)
        sys.exit()
    for second_code in encods:
        try:
            tmp2 = tmp1.decode(second_code)
        except:
            continue
        for third_code in encods:
            try:
                tmp3 = tmp2.encode(third_code)
            except:
                continue
            try:
                decoded = tmp3.decode('koi8-r')
            except:
                pass
            if decoded.startswith('ПРОЦ') and \
               (decoded.endswith('КНЦ;\n') or decoded.endswith('КНЦ;')):
                print(decoded)
                sys.exit()
            for fourth_code in encods:
                try:
                    tmp4 = tmp3.decode(fourth_code)
                except:
                    continue
                for fifth_code in encods:
                    try:
                        tmp5 = tmp4.encode(fifth_code)
                    except:
                        continue
                    try:
                        decoded = tmp5.decode('koi8-r')
                    except:
                        continue
                    if decoded.startswith('ПРОЦ') and \
                       (decoded.endswith('КНЦ;\n') or decoded.endswith('КНЦ;')):
                        print(decoded)
                        sys.exit()
