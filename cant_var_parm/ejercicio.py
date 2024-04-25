database = {
            1:{
                "nombre1":"Pablo",
                "nombre2":"Diego",
                "apellido1":"Ruiz",
                "apellido2":"Picasso"
            },
            2:{
                "nombre1":"Elio",
                "apellido1":"Anci"
            },
            3:{
                "nombre1":"Elias",
                "nombre2":"Marcos",
                "nombre3":"Luciano",
                "apellido1":"Marcelo",
                "apellido2":"Gonzalez"
            }
}


def buscar_datos(*args, **kwargs):
    database = kwargs.get('database', {})
    for key, persona in database.items():
        if all(item in persona.values() for item in args):
            return key
    return 

resultado = buscar_datos("Elio","Anci", database=database)
print(resultado)