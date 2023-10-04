print("Calculadora de AU a Kilómetros y Tiempo Luz\n")
print("Revisado en octubre de 2023")

def dist(au):

        #---------------Distancia-Real---------------#
        km = 149_597_870.7 * au

        if km < 1_000_000_000:
            print(f"Distancia real:      {km:.2f} Km")

        elif 1_000_000_000 <= km < 10_000_000_000:
            dkm = km / 1_000_000_000
            print(f"Distancia real:     ~{dkm:.2f} x 10^9 Km")

        elif 10_000_000_000 <= km < 100_000_000_000:
            dkm = km / 10_000_000_000
            print(f"Distancia real:     ~{dkm:.2f} x 10^10 Km")

        elif 100_000_000_000 <= km < 1_000_000_000_000:
            dkm = km / 100_000_000_000
            print(f"Distancia real:     ~{dkm:.2f} x 10^11 Km")

        elif 1_000_000_000_000 <= km < 10_000_000_000_000:
            dkm = km / 1_000_000_000_000
            print(f"Distancia real:     ~{dkm:.2f} x 10^12 Km")

        #---------------Unidad-a-Escala---------------#

        u = km / 10_000_000

        if 1 <= u < 100:
            print(f"Unidad de escala:   ~{u:.1f} cm")

        elif 100 <= u < 100_000:
            met = u / 100
            print(f"Unidad de escala:   ~{met:.2f} m")

        elif u >= 100_000:
            kl = u / 100_000
            print(f"Unidad de escala:   ~{kl:.2f} Km")

        elif u < 1:
            mili = u * 10
            if mili < 0.1:
                print("(Unidad de escala inferior a 0.1 milímetro)")
            else:
                print(f"Unidad de escala:   ~{mili:.2f} mm")

        #---------------Distancia Tierra-Luna---------------#

        tl = km / 384_400
        if 0.5 <= tl < 10_000:
            print(f"Dist. Tierra-Luna:  ~{tl:.2f} X")

        #---------------Espacio-Exterior---------------#

        dluz = km / 25_902_068_371.2
        aluz = dluz / 365
        pc = aluz / 3.263795578182545

        if km >= 25_902_068_371.2:

            if dluz < 2:
                print(f"Distancia (d. luz): ~{dluz:.2f} Día Luz")

            elif 2 <= dluz < 365:
                print(f"Distancia (d. luz): ~{dluz:.2f} Días Luz")

            elif aluz >= 1:

                if aluz < 2:
                    print("\nDistancia interestelar: ")
                    print(f"{aluz:.2f} Año Luz") # 68_551

                elif aluz >= 2 and pc < 1:
                    print("\nDistancia interestelar: ")
                    print(f"{aluz:.2f} Años Luz") # 157_890

                elif aluz >= 2 and 1 <= pc < 2:
                    print("\nDistancias interestelares: ")
                    print(f"{aluz:.2f} Años Luz | {pc:.2f} Pársec") # 213_212 AU

                elif aluz >= 2 and pc >= 2:
                    print("\nDistancias interestelares: ")
                    print(f"{aluz:.2f} Años Luz | {pc:.2f} Pársecs") # 567043

        # -- Tiempo-Luz -- #
        else:

            hluz = round(km // 1_079_252_848.8)
            km = km % 1_079_252_848.8

            mluz = round(km // 17_987_547.48)
            km = km % 17_987_547.48

            sluz = km / 299_792.458

            if hluz < 1:

                if mluz >= 21:

                    if sluz >= 10:
                        print(f"Duración de la luz:  0{hluz}:{mluz}:{sluz:.0f}") # Bien: 4.208005234022618
                    else:
                        print(f"Duración de la luz:  0{hluz}:{mluz}:0{sluz:.0f}") # Bien: 4.093777872188918

                elif mluz < 21:

                    if 10 <= mluz < 21:
                        if sluz >= 10:
                            print(f"Duración de la luz:  0{hluz}:{mluz}:{sluz:.2f}") # Bien: 2.355156239115089
                        elif sluz < 10:
                            print(f"Duración de la luz:  0{hluz}:{mluz}:0{sluz:.2f}") # Bien: 2.2914609980481493

                    elif mluz < 10:
                        if sluz >= 10:
                            print(f"Duración de la luz:  0{hluz}:0{mluz}:{sluz:.2f}") # Correcto: 1.0113990
                        elif sluz < 10:
                            if mluz >= 1:
                                print(f"Duración de la luz:  0{hluz}:0{mluz}:0{sluz:.2f}") # Bien: 0.9808923999428288
                            else:
                                if sluz >= 1:
                                    print(f"Duración de la luz:  {sluz:.2f} s")

                                else:
                                    msluz = km / 299.792458
                                    print(f"Duración de la luz:  {msluz:.4} ms")

            elif hluz >= 1:
                if hluz >= 10:
                    if mluz >= 10:
                        if sluz >= 10:
                            print(f"Duración de la luz:  {hluz}:{mluz}:{sluz:.0f}") # Bien: 135.35741978413068
                        else:
                            print(f"Duración de la luz:  {hluz}:{mluz}:0{sluz:.0f}") # Bien: 171.3490587057667
                    else:
                        if sluz >= 10:
                            print(f"Duración de la luz:  {hluz}:0{mluz}:{sluz:.0f}") # Bien: 108.36369059290361
                        elif sluz < 10:
                            print(f"Duración de la luz:  {hluz}:0{mluz}:0{sluz:.0f}") # Bien: 93.90891934893028
                else:
                    if mluz >= 10:
                        if sluz >= 10:
                            print(f"Duración de la luz:  0{hluz}:{mluz}:{sluz:.0f}") # Bien: 23.949670197799144
                        else:
                            print(f"Duración de la luz:  0{hluz}:{mluz}:0{sluz:.0f}") # Bien: 23.929630309758146
                    else:
                        if sluz >= 10:
                            print(f"Duración de la luz:  0{hluz}:0{mluz}:{sluz:.0f}") # Bien: 22.747276915339146
                        else:
                            print(f"Duración de la luz:  0{hluz}:0{mluz}:0{sluz:.0f}") # Bien: 22.727237027298145



#----------------------------------------------------Termina-la-función------------------------------------------------------------------#

n = input("Ingrese la distancia en unidades astronómicas: ")

if n == "":
    print("\n¡Cancelado! Supongo..")

try:
    n = float(n)
    if n is not None:

        if n == 0:
            print("\n0")

        elif 0 < n <= 0.00000000667:
            print("Ese es un dato demasiado pequeño como para calcular.")

        else:
            print("Las respuestas son aproxiamdas:\n")
            if n < 0:
                n = n * (-1)
                print("*Distancia corregida.")

            nint = int(n)
            nflo = float(n)
            res = nflo - nint
            res2 = nint - nflo
            nstr = str(res)

            c = -2
            for i in nstr:
                c += 1

            c = round(c, 4)

            if n > 0.004:

                if c >= 3:
                    if res2 != 0:
                        if n < 100:
                            print(f"Usted ha ingresado: ~{n:.3} AU")

                        else:
                            print(f"Usted ha ingresado: ~{n:.2f} AU")

                elif c < 3:
                    if res2 != 0:
                        print(f"Usted ha ingresado:  {n} AU")

                    else:
                        print(f"Usted ha ingresado:  {nint} AU")

            else:
                print("Usted ha ingresado: >0.005 AU")

            dist(n)

except ValueError:
    if n != "":
        print("\nError: El usuario ingresó algún dato no numérico.")
