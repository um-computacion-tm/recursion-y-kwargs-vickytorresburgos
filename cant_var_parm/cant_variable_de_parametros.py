def escribir_nombre(*args,**kwargs):
    print("inicio")
    for arg in args:
        print(arg)
        for key, value in kwargs.items():
            print(key,value)

escribir_nombre('Francisco',nombre1='Maria',nombre2='Victoria',apellido1='Torres',apellido2='Burgos')

