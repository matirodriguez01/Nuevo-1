from tkinter import *

from tkinter import ttk, font, messagebox


class App:
    __ventana = None
    __altura = 0
    __peso = 0
    __resultado = 0
    __texto = ''

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('576x353')
        self.__ventana.resizable(0, 0)
        self.__ventana.title('')
        fuente1 = font.Font(weight='bold', size=12)
        fuente2 = font.Font(weight='bold', size=10)
        opts = {'fill': 'both', 'expand': 'True'}

        # Frame 1
        frame1 = ttk.Frame(self.__ventana)
        frame1.pack(side=TOP, **opts, padx=0, pady=0, ipady=0, ipadx=0)
        frame1['borderwidth'] = 0
        ttk.Label(frame1, text='Calculadora de IMC', font=fuente1).pack(side=TOP, **opts, padx=180, pady=0)

        # Frame 2
        frame2 = ttk.Frame(self.__ventana)
        frame2.pack(side=TOP, **opts, padx=0, pady=10)
        frame2['borderwidth'] = 0
        ttk.Separator(frame2, orient='horizontal').pack(side=TOP, **opts, padx=0, pady=0)
        ttk.Label(frame2, text='Altura:', font=fuente2, foreground='gray').pack(side=LEFT, **opts, padx=5, pady=10)
        self.__altura = DoubleVar()
        self.alturaEntry = ttk.Entry(frame2, foreground='gray', background='light gray')
        self.alturaEntry.pack(side=LEFT, **opts, padx=10, pady=0, ipadx=170, ipady=0)
        ttk.Label(frame2, text='cm', background='light gray').pack(side=LEFT, **opts, pady=0)
        ttk.Separator(self.__ventana, orient='horizontal').pack(side=TOP, **opts, padx=0, pady=0)

        # Frame 3
        frame3 = ttk.Frame(self.__ventana)
        frame3.pack(side=TOP, **opts, padx=0, pady=0, ipady=0, ipadx=0)
        frame3['borderwidth'] = 0
        ttk.Label(frame3, text='Peso:', font=fuente2, foreground='gray').pack(side=LEFT, **opts, padx=5, pady=0)
        self.__peso = DoubleVar()
        self.pesoEntry = ttk.Entry(frame3, foreground='gray', background='light gray')
        self.pesoEntry.pack(side=LEFT,  **opts, padx=10, pady=0, ipadx=170, ipady=0)
        ttk.Label(frame3, text='kg', background='light gray').pack(side=RIGHT, **opts, padx=0, pady=0)
        ttk.Separator(frame3, orient='horizontal').pack(side=TOP, **opts, padx=0, pady=0)

        # Frame 4
        frame4 = ttk.Frame(self.__ventana)
        self.__resultado = DoubleVar(value=0)
        self.__texto = StringVar(value='Peso normal')
        frame4.pack(side=TOP, **opts, padx=0, pady=0)
        frame4['borderwidth'] = 0
        ttk.Separator(frame4, orient='horizontal').pack(side=TOP, **opts, padx=1, pady=1)
        ttk.Style().configure("TButton", background='#228B22', foreground='#228B22')
        ttk.Button(frame4, text='Calcular', command=self.calcular).pack(side=LEFT, **opts, pady=10, padx=50, ipady=5)
        ttk.Button(frame4, text='Limpiar', command=self.limpiar).pack(side=RIGHT, **opts, pady=10, padx=50, ipady=5)

        # Frame 5 #dff0d8
        frame5 = ttk.Frame(self.__ventana)
        frame5.pack(side=TOP, **opts, padx=0, pady=0, ipady=0)
        frame5['borderwidth'] = 0
        ttk.Label(frame5, text='').pack(side=LEFT, **opts, ipadx=60)
        ttk.Label(frame5, text='Tu índice de masa corporal (IMC) es de',
                  background='#dff0d8', font=fuente2, foreground='#467d46').pack(side=LEFT, **opts, ipady=10)
        ttk.Label(frame5, textvariable=self.__resultado,
                  background='#dff0d8', foreground='#467d46', font=fuente2).pack(side=LEFT, **opts, padx=0, ipady=10)
        ttk.Label(frame5, text='Kg/m2', font=fuente2, foreground='#467d46',
                  background='#dff0d8').pack(side=LEFT, **opts, ipadx=0, ipady=10)
        ttk.Label(frame5, text='').pack(side=RIGHT, ipadx=60)

        # Frame 6
        frame6 = ttk.Frame(self.__ventana)
        frame6.pack(side=TOP, **opts, padx=0, pady=0)
        frame6['borderwidth'] = 0
        ttk.Label(frame6, text='').pack(side=LEFT, **opts, ipadx=0)
        ttk.Label(frame6, text='', background='#dff0d8', font=fuente2).pack(side=LEFT, **opts, ipady=10, ipadx=0)
        ttk.Label(frame6, text='', font=fuente2).pack(side=RIGHT, **opts, padx=0, ipady=10, ipadx=0)
        ttk.Label(frame6, textvariable=self.__texto, background='#dff0d8',
                  foreground='#467d46', font=fuente2).pack(side=RIGHT, **opts, ipadx=0, ipady=10)


        # Frame 7
        frame7 = ttk.Frame(self.__ventana)
        frame7.pack(side=TOP, **opts, padx=20, pady=0)
        frame7['borderwidth'] = 0

        self.alturaEntry.focus()
        self.__ventana.mainloop()

    def calcular(self):
        try:
            v1 = int(self.alturaEntry.get()) / 100
            v2 = int((self.pesoEntry.get()))
            self.__resultado.set(v2 / (v1 ** 2))
            self.comparacion()
        except ValueError:
            messagebox.showerror(title='Error', message='Debe ingresar un valor numérico')
            self.limpiar()
        self.alturaEntry.focus()

    def limpiar(self):
        self.alturaEntry.delete(0, 'end')
        self.pesoEntry.delete(0, 'end')
        self.__resultado.set(0)

    def comparacion(self):
        valor = self.__resultado.get()
        if valor < 18.5:
            self.__texto.set('Peso inferior al normal')
        elif 18.5 <= valor <= 24.9:
            self.__texto.set('Peso normal')
        elif 25.0 <= valor <= 29.9:
            self.__texto.set('Peso superior al normal')
        elif valor > 30.0:
            self.__texto.set('Obesidad')
