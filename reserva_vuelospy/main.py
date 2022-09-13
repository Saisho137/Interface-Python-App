import PySimpleGUI as sg
import Pasajero

Layout = [
          [ sg.Text("Porcentaje:", size = (8, 0)), sg.Text("", key='-PRC-', size=(10, 1))],
          [ sg.Text("Disponibles:", size=(8,1)), sg.Input(disabled = True, key='-DISPONIBLES-', size=(4,0))],
          [ sg.Text("Ocupados:", size=(8,1)), sg.Input(disabled = True, key='-OCUPADOS-', size=(4,0))],
          [ sg.Graph(canvas_size=(600, 600), graph_bottom_left=(0, 0), graph_top_right=(600, 600), key="-GRAPH-")],
          [
           sg.Text("",size=(10,1)),
           sg.Button("Registrar", button_color= ("black","misty rose"), key='-REGISTRAR-'),
           sg.Button("Buscar", button_color= ("black","gold"), key='-BUSCAR-'),
           sg.Button("Eliminar", button_color= ("black","salmon"), key='-ELIMINAR-'),
           sg.Button("Informacion general", button_color= ("black","sky blue"), key='-INFO-'),
           sg.Button("Estadisticas", button_color= ("black","steel blue"), key='-ESTD-')
          ]
         ]


Avion = sg.Window("Reserva de Vuelos", Layout)
Avion.Finalize()

graph = Avion['-GRAPH-']
graph.DrawImage(filename="AVIONpy.png", location=(70,600))
#---------------------------------------------------------
libres = 50
ocu = 0
#
Avion['-DISPONIBLES-'].update(libres)
Avion['-OCUPADOS-'].update(ocu)
Avion['-PRC-'].update(str((50-libres)*2)+"%")
#---------------------------------------------------------
b1 = graph.DrawRectangle((220,500),(240,520), fill_color = "yellow")
b1t = graph.DrawText("1",(230,510))
b2 = graph.DrawRectangle((255,500),(275,520), fill_color = "yellow")
b2t = graph.DrawText("2",(265,510))

b3 = graph.DrawRectangle((310,500),(330,520), fill_color = "yellow")
b3t = graph.DrawText("3",(320,510))
b4 = graph.DrawRectangle((345,500),(365,520), fill_color = "yellow")
b4t = graph.DrawText("4",(355,510))
#-------------------------------------------------------------------
b5 = graph.DrawRectangle((220,470),(240,490), fill_color = "yellow")
b5t = graph.DrawText("5",(230,480))
b6 = graph.DrawRectangle((255,470),(275,490), fill_color = "yellow")
b6t = graph.DrawText("6",(265,480))

b7 = graph.DrawRectangle((310,470),(330,490), fill_color = "yellow")
b7t = graph.DrawText("7",(320,480))
b8 = graph.DrawRectangle((345,470),(365,490), fill_color = "yellow")
b8t = graph.DrawText("8",(355,480))
#___________________________________________________________________
b9 = graph.DrawRectangle((200,440),(220,460), fill_color = "green")
b9t = graph.DrawText("9",(210,450))
b10 = graph.DrawRectangle((230,440),(250,460), fill_color = "green")
b10t = graph.DrawText("10",(240,450))
b11 = graph.DrawRectangle((260,440),(280,460), fill_color = "green")
b11t = graph.DrawText("11",(270,450))

b12 = graph.DrawRectangle((305,440),(325,460), fill_color = "green")
b12t = graph.DrawText("12",(315,450))
b13 = graph.DrawRectangle((335,440),(355,460), fill_color = "green")
b13t = graph.DrawText("13",(345,450))
b14 = graph.DrawRectangle((365,440),(385,460), fill_color = "green")
b14t = graph.DrawText("14",(375,450))
#-------------------------------------------------------------------
b15 = graph.DrawRectangle((200,410),(220,430), fill_color = "green")
b15t = graph.DrawText("15",(210,420))
b16 = graph.DrawRectangle((230,410),(250,430), fill_color = "green")
b16t = graph.DrawText("16",(240,420))
b17 = graph.DrawRectangle((260,410),(280,430), fill_color = "green")
b17t = graph.DrawText("17",(270,420))

b18 = graph.DrawRectangle((305,410),(325,430), fill_color = "green")
b18t = graph.DrawText("18",(315,420))
b19 = graph.DrawRectangle((335,410),(355,430), fill_color = "green")
b19t = graph.DrawText("19",(345,420))
b20 = graph.DrawRectangle((365,410),(385,430), fill_color = "green")
b20t = graph.DrawText("20",(375,420))
#-------------------------------------------------------------------
b21 = graph.DrawRectangle((200,380),(220,400), fill_color = "green")
b21t = graph.DrawText("21",(210,390))
b22 = graph.DrawRectangle((230,380),(250,400), fill_color = "green")
b22t = graph.DrawText("22",(240,390))
b23 = graph.DrawRectangle((260,380),(280,400), fill_color = "green")
b23t = graph.DrawText("23",(270,390))

b24 = graph.DrawRectangle((305,380),(325,400), fill_color = "green")
b24t = graph.DrawText("24",(315,390))
b25 = graph.DrawRectangle((335,380),(355,400), fill_color = "green")
b25t = graph.DrawText("25",(345,390))
b26 = graph.DrawRectangle((365,380),(385,400), fill_color = "green")
b26t = graph.DrawText("26",(375,390))
#-------------------------------------------------------------------
b27 = graph.DrawRectangle((200,350),(220,370), fill_color = "green")
b27t = graph.DrawText("27",(210,360))
b28 = graph.DrawRectangle((230,350),(250,370), fill_color = "green")
b28t = graph.DrawText("28",(240,360))
b29 = graph.DrawRectangle((260,350),(280,370), fill_color = "green")
b29t = graph.DrawText("29",(270,360))

b30 = graph.DrawRectangle((305,350),(325,370), fill_color = "green")
b30t = graph.DrawText("30",(315,360))
b31 = graph.DrawRectangle((335,350),(355,370), fill_color = "green")
b31t = graph.DrawText("31",(345,360))
b32 = graph.DrawRectangle((365,350),(385,370), fill_color = "green")
b32t = graph.DrawText("32",(375,360))
#-------------------------------------------------------------------
b33 = graph.DrawRectangle((200,320),(220,340), fill_color = "green")
b33t = graph.DrawText("33",(210,330))
b34 = graph.DrawRectangle((230,320),(250,340), fill_color = "green")
b34t = graph.DrawText("34",(240,330))
b35 = graph.DrawRectangle((260,320),(280,340), fill_color = "green")
b35t = graph.DrawText("35",(270,330))

b36 = graph.DrawRectangle((305,320),(325,340), fill_color = "green")
b36t = graph.DrawText("36",(315,330))
b37 = graph.DrawRectangle((335,320),(355,340), fill_color = "green")
b37t = graph.DrawText("37",(345,330))
b38 = graph.DrawRectangle((365,320),(385,340), fill_color = "green")
b38t = graph.DrawText("38",(375,330))
#-------------------------------------------------------------------
b39 = graph.DrawRectangle((200,290),(220,310), fill_color = "green")
b39t = graph.DrawText("39",(210,300))
b40 = graph.DrawRectangle((230,290),(250,310), fill_color = "green")
b40t = graph.DrawText("40",(240,300))
b41 = graph.DrawRectangle((260,290),(280,310), fill_color = "green")
b41t = graph.DrawText("41",(270,300))

b42 = graph.DrawRectangle((305,290),(325,310), fill_color = "green")
b42t = graph.DrawText("42",(315,300))
b43 = graph.DrawRectangle((335,290),(355,310), fill_color = "green")
b43t = graph.DrawText("43",(345,300))
b44 = graph.DrawRectangle((365,290),(385,310), fill_color = "green")
b44t = graph.DrawText("44",(375,300))
#-------------------------------------------------------------------
b45 = graph.DrawRectangle((200,260),(220,280), fill_color = "green")
b45t = graph.DrawText("45",(210,270))
b46 = graph.DrawRectangle((230,260),(250,280), fill_color = "green")
b46t = graph.DrawText("46",(240,270))
b47 = graph.DrawRectangle((260,260),(280,280), fill_color = "green")
b47t = graph.DrawText("47",(270,270))

b48 = graph.DrawRectangle((305,260),(325,280), fill_color = "green")
b48t = graph.DrawText("48",(315,270))
b49 = graph.DrawRectangle((335,260),(355,280), fill_color = "green")
b49t = graph.DrawText("49",(345,270))
b50 = graph.DrawRectangle((365,260),(385,280), fill_color = "green")
b50t = graph.DrawText("50",(375,270))
#-------------------------------------------------------------------
sillasj = [b1, b4, b5, b8,  b2, b3, b6, b7]
#-[0,1,2,3,  4,5,6,7]-
# [1,4,5,8,  2,3,6,7]
sillasc = [b9, b14, b15, b20, b21, b26, b27, b32, b33, b38, b39, b44, b45, b50,
           b10, b13, b16, b19, b22, b25, b28, b31, b34, b37, b40, b43, b46, b49,
           b11, b12, b17, b18, b23, b24, b29, b30, b35, b36, b41, b42, b47, b48]
'''
Ubicacion = 
-[0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13]-
 [9,14,15,20,21,26,27,32,33,38,39,44,45,50,/Ventana  
                
-[14,15,16,17,18,19,20,21,22,23,24,25,26,27]-
  10,13,16,19,22,25,28,31,34,37,40,43,46,49,/Centro 
                
-[28,29,30,31,32,33,34,35,36,37,38,39,40,41]- 
  11,12,17,18,23,24,29,30,35,36,41,42,47,48/pasillo ]*/
'''
listaPasajeros = []
listaCedulas = []
#---------------------------------------------------------------------


while True:
    event, values = Avion.Read()
    if event is None:
        Avion.Close()
        break
    elif event == '-REGISTRAR-':
        LayoutRegistrar = [
            [sg.Text("",size=(0,1))],
            [sg.Text("Cedula:",size=(10,2)),sg.Input( key = '-CEDULAR-') ],
            [sg.Text("Nombre:", size=(10,2)), sg.Input(key='-NOMBRER-')],
            [sg.Text("Edad:", size=(10, 2)), sg.Input(key='-EDADR-')],
            [sg.Text("Sexo:",size=(10,2)), sg.Combo(["Masculino", "Femenino"], size=(43,2), key = '-SEXOR-')],
            [sg.Text("Clase:",size=(10,2)), sg.Combo(["Ejecutiva", "Economica"], size=(43,2), key = '-CLASER-')],
            [sg.Text("Ubicacion:",size=(10,2)), sg.Combo(["Ventana", "Pasillo", "Centro"], size=(43,2), key = '-UBIR-')],
            [sg.Input(disabled = True, key='-PRUEBA-')],
            [sg.Text("",size=(20,1)),sg.Button("Registrar", key='-GUARDAR-', button_color= ("black","azure2"))]
        ]

        Registrar = sg.Window("Registrar Pasajero", LayoutRegistrar)
        Registrar.Finalize()

        while True:
            eventRegistrar, valuesRegistrar = Registrar.Read()
            if eventRegistrar is None:
                Registrar.Close()
                break
            elif eventRegistrar == '-GUARDAR-':
                try:
                    cc = int(valuesRegistrar['-CEDULAR-'])
                    name = str(valuesRegistrar['-NOMBRER-'])
                    age = int(valuesRegistrar['-EDADR-'])
                    gen = str(valuesRegistrar['-SEXOR-'])
                    clas = str(valuesRegistrar['-CLASER-'])
                    ubi = str(valuesRegistrar['-UBIR-'])
                    pst = 0
                    if valuesRegistrar['-CLASER-'] == "Ejecutiva" and valuesRegistrar['-UBIR-'] == "Centro":
                        sg.popup_error("La ubicacion \"Centro\" no se encuentra en la clase \"Ejecutiva\"  ", title="Error al Registrar")

                    elif valuesRegistrar['-CEDULAR-'] in listaCedulas:
                       sg.popup_error("La cedula que desea registrar ya tiene una reserva en este Vuelo", title="Error al Registrar")

                    elif cc !="" and  name !="" and age !="" and gen !="" and clas !="" and ubi != "":
                        #
                        obp = Pasajero.Pasajero(cc, name, age, gen, clas, ubi,  pst)
                        listaPasajeros.append(obp)
                        listaCedulas.append(str(obp.cedula))
                        sg.popup("El pasajero se ha registrado con exito", title="Guardado exitoso")
                        #

                        Registrar['-CEDULAR-'].update("")
                        Registrar['-NOMBRER-'].update("")
                        Registrar['-EDADR-'].update("")
                        Registrar['-SEXOR-'].update("")
                        Registrar['-CLASER-'].update("")
                        Registrar['-UBIR-'].update("")
                        Registrar['-PRUEBA-'].update(len(listaCedulas)) #listaCedulas[len(listaCedulas)-1])
                        #
                        libres -= 1
                        ocu += 1

                        Avion['-DISPONIBLES-'].update(libres)
                        Avion['-OCUPADOS-'].update(ocu)
                        Avion['-PRC-'].update(str((50 - libres) * 2) + "%")
                        #
                    else:
                        sg.popup_error("Debe de llenar todos los campos con el tipo de dato adecuado",
                                 title="Error al registrar")

                except (ValueError):
                    sg.popup_error("Debe de llenar todos los campos con el tipo de dato adecuado", title="Error al registrar")

    elif event == '-BUSCAR-':
        LayoutBuscar = [
            [sg.Text("", size=(0, 1))],
            [sg.Text("Cedula:", size=(10, 2)), sg.Input(key='-CEDULAB-')],
            [sg.Text("Nombre:", size=(10, 2)), sg.Input(disabled = True, key='-NOMBREB-')],
            [sg.Text("Clase:", size=(10, 2)), sg.Input(disabled = True, key='-CLASEB-')],
            [sg.Text("Ubicacion:", size=(10, 2)), sg.Input(disabled = True, key='-UBIB-')],
            [sg.Text("Asiento:", size=(10, 2)), sg.Input(disabled = True, key='-ASIENTOB-')],
            [sg.Text("", size=(20, 1)), sg.Button("Buscar", key='-BUSCAR-', button_color= ("black","azure2"))]
        ]

        Buscar =  sg.Window("Buscar Pasajero", LayoutBuscar)
        Buscar.finalize()

        while True:
            eventBuscar, valuesBuscar = Buscar.Read()
            if eventBuscar is None:
                Buscar.Close()
                break
            elif eventBuscar == '-BUSCAR-':
                try:
                    Buscar['-NOMBREB-'].update("")
                    Buscar['-CLASEB-'].update("")
                    Buscar['-UBIB-'].update("")
                    Buscar['-ASIENTOB-'].update("")

                    comp = False
                    bsq = int(valuesBuscar['-CEDULAB-'])

                    for i in range(0, len(listaPasajeros), 1):

                        pp = listaPasajeros[i]

                        if pp.cedula == bsq:

                            x = int(pp.puesto)
                            Buscar['-NOMBREB-'].update(pp.nombre)
                            Buscar['-CLASEB-'].update(pp.clase)
                            Buscar['-UBIB-'].update(pp.ubicacion)
                            Buscar['-ASIENTOB-'].update(x)
                            comp = True
                            break

                    if not comp:
                        sg.popup("No existe una reserva de asiento con la cedula ingresada.", title = "Advertencia")
                except (ValueError):
                    sg.popup("Debe de llenar el campo con el tipo de dato adecuado", title="Error al Buscar")


    elif event == '-ELIMINAR-':
        LayoutEliminar = [
            [sg.Text("", size=(0, 1))],
            [sg.Text("Cedula:", size=(10, 2)), sg.Input(key='-CEDULAE-')],
            [sg.Text("Nombre:", size=(10, 2)), sg.Input(disabled=True, key='-NOMBREE-')],
            [sg.Text("Asiento:", size=(10, 2)), sg.Input(disabled=True, key='-ASIENTOE-')],
            [sg.Text("", size=(20, 1)), sg.Button("Eliminar", key='-ELIMINAR-', button_color= ("black","azure2"))]
        ]

        Eliminar = sg.Window("Eliminar Pasajero", LayoutEliminar)
        Eliminar.finalize()

        while True:
            eventEliminar, valuesEliminar = Eliminar.Read()
            if eventEliminar is None:
                Buscar.Close()
                break
            elif eventEliminar == '-ELIMINAR-':
                try:
                    Eliminar['-NOMBREE-'].update("")
                    Eliminar['-ASIENTOE-'].update("")

                    comp = False

                    eli = int(valuesEliminar['-CEDULAE-'])

                    for i in range(0, len(listaPasajeros), 1):

                        pe  = listaPasajeros[i]

                        if pe.cedula == eli:

                            y = int(pe.puesto)

                            Eliminar['-NOMBREE-'].update(pe.nombre)
                            Eliminar['-ASIENTOE-'].update(y) #asient.setText(Integer.toString(y))
                            listaPasajeros.pop(i)
                            comp = True;
                            break

                    if not comp:
                        sg.popup_error("No hay ninguna reserva con la Cedula que desea eliminar",title="Error al eliminar")
                        Eliminar['-CEDULAE-'].update("")
                    if comp:
                        #
                        sg.popup("Se ha removido el pasajero con Exito", title = "Exito")
                        #
                        libres += 1
                        ocu -= 1

                        Avion['-DISPONIBLES-'].update(libres)
                        Avion['-OCUPADOS-'].update(ocu)
                        Avion['-PRC-'].update(str((50 - libres) * 2) + "%")
                        #

                except (ValueError):
                    sg.popup_error("Debe llenar el campo con el tipo de dato indicado",title = "Error al Eliminar")

    elif event == '-INFO-':
        almacen = []
        for i in range(0, len(listaPasajeros), 1):
            pepe = listaPasajeros[i-1]
            almacen.append([pepe.nombre, pepe.cedula, pepe.puesto, pepe.clase, pepe.ubicacion])
        headings = ['NOMBRES', 'CÉDULAS', 'ASIENTOS', 'CLASES', 'UBICACIÓNES']
        header = [[sg.Text('')] + [sg.Text(h, size=(16, 1)) for h in headings]]
        input_rows = [[sg.Input(default_text=almacen[row][col], size=(20, 1), pad=(0, 0), disabled=True)
                       for col in range(5)] for row in range(len(listaPasajeros))]
        layoutDatos = header + input_rows



        Info = sg.Window("Informacion de los Pasajeros", layoutDatos)
        Info.Finalize()

        while True:
            eventInfo, valuesInfo = Info.Read()
            if eventInfo is None:
                Info.Close()
                break

    elif event == '-ESTD-':
        LayoutEstd = [
            [sg.Text("Ocupacion por sexo",size=(40,1))],
            [sg.Text("Hombres: ",size=(8,0)), sg.Input(disabled = True, key='-HOMBRES-', size=(4,0)),
             sg.Text("Mujeres: ",size=(8,0)),sg.Input(disabled = True, key='-MUJERES-', size=(4,0)) ],
            [sg.Text("Ocupacion por edad",size=(40,1))],
            [sg.Text("Mayores: ",size=(8,0)), sg.Input(disabled = True, key='-MAYORES-', size=(4,0)),
             sg.Text("Menores: ",size=(8,0)), sg.Input(disabled = True, key='-MENORES-', size=(4,0))],
            [sg.Text("Promedio de la edad: ",size=(40,0))],
            [sg.Input(disabled = True, key='-PROMEDIO-', size=(4,0))],
            [sg.Text("Nombre y edad del mas joven: ",size=(40,0))],
            [sg.Input(disabled = True, key='-NOMBREJ-', size=(20,0))],
            [sg.Text("Nombre y edad del mas viejo: ",size=(40,0))],
            [sg.Input(disabled = True, key='-NOMBREV-', size=(20,0))],
            [sg.Text("", size=(16, 1)), sg.Button("Reload", key='-OK-', button_color= ("black","azure2"))]
        ]

        Estd = sg.Window("Estadisticas del Vuelo", LayoutEstd)
        Estd.Finalize()

        while True:
            eventEstd, valuesEstd = Estd.Read()
            if eventEstd is None:
                Estd.Close()
                break
            elif eventEstd == '-OK-':
                #contadores estadisticas
                contm = 0
                conth = 0
                conty = 0
                contx = 0
                sumedad = 0
                min = 150
                max = 0
                #
                for i in range(0, len(listaPasajeros), 1):
                    #sexos
                    if listaPasajeros[i].sexo == "Femenino":
                        #Masculino / Femenino
                        contm += 1
                        Estd['-MUJERES-'].update(contm)
                    elif listaPasajeros[i].sexo == "Masculino":
                        #Masculino / Femenino
                        conth += 1
                        Estd['-HOMBRES-'].update(conth)
                    #edades
                    if listaPasajeros[i].edad >= 18:
                        conty += 1
                        Estd['-MAYORES-'].update(conty)
                    elif listaPasajeros[i].edad < 18:
                        contx += 1
                        Estd['-MENORES-'].update(contx)
                    #promedio edad

                    sumedad += listaPasajeros[i].edad
                    tam = int(len(listaPasajeros))

                    Estd['-PROMEDIO-'].update(sumedad / tam)

                    #mas joven
                    if listaPasajeros[i].edad < min:
                        min = listaPasajeros[i].edad

                        Estd['-NOMBREJ-'].update( listaPasajeros[i].nombre + "," + str(min) )
                    #mas viejo
                    if listaPasajeros[i].edad > max:
                        max = listaPasajeros[i].edad
                        Estd['-NOMBREV-'].update(listaPasajeros[i].nombre + "," + str(max) )
