# -*- coding: utf-8 -*-
"""
@author: Alberto Barbado González
@mail: alberto.barbado.gonzalez@gmail.com

"""
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import *
from tkinter import filedialog as FileDialog
from io import open
import PIL
from PIL import ImageTk, Image
import sys
import os
from random import shuffle
import pandas as pd
from config import PATH_USER, JOBLIB_PARAMS
from tools import file_presistance
from joblib import Parallel, delayed

from query_processing import embedding_query_stanza

def embedding_query(a,b,c,d):
    pass

restart_variable = False


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
    

# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        print (self.winfo_reqwidth(),self.winfo_reqheight()) #>>>854, 404
        self.bind("<Configure>", self.on_resize)

    def on_resize(self,event):
        self.width = event.width   #>>>854
        self.height = event.height #>>>404
        self.config(width=self.width, height=self.height)
        

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=26, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self, width=450, height=50, pady=3)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid(row=0, sticky="ew")

        self.frames = {}
        for F in (StartPage, AffectiveFeatures, SonnetRecommender, RateApp):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        
        

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        ##########################################
        # Variables
        ########################################## 
        self.controller = controller
        
        # Define timestamp for this user (initial variables)
        global timestamp, file_name
        timestamp = pd.datetime.now()
        file_name = str(timestamp.year) + '_' + str(timestamp.month) + '_' + str(timestamp.day) + '_' + str(timestamp.hour) + '_' + str(timestamp.minute) + '_' + str(timestamp.second)
#        global arousal_init
#        arousal_init = StringVar(value="1")
#        global valence_init
#        valence_init = StringVar(value="1")
        
        ##########################################
        # Layout
        ##########################################    
    
        # Creo los contenedores principales
        top_frame = Frame(self, bg="gray28", width=500, height=150, pady=3, padx=3)
        center = Frame(self, bg="black", width=50, height=40, padx=3, pady=3)
        btm_frame = Frame(self, bg="gray28", width=450, height=100, pady=3)
        btm_frame2 = Frame(self, bg='gray28', width=450, height=100, pady=3)
        
        # Layout de los contenedores
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        
        top_frame.grid(row=0, sticky="ew")
        center.grid(row=1, sticky="nsew")
        btm_frame.grid(row=3, sticky="ew")
        btm_frame2.grid(row=4, sticky="ew")
        
        # create the center widgets
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)
        
        ctr_left = Frame(center, bg='gray28', width=100, height=190)
        ctr_mid = Frame(center, bg='gray28', width=550, height=190, padx=3, pady=3)
        ctr_right = Frame(center, bg='gray28', width=400, height=190, padx=3, pady=3)
        
        ctr_left.grid(row=0, column=0, sticky="ns")
        ctr_mid.grid(row=0, column=1, sticky="nsew")
        ctr_right.grid(row=0, column=2, sticky="ns")
        
        # separate center in three parts
        ctr_mid_up = Frame(ctr_mid, bg='gray28', width=550, height=70)
        ctr_mid_mid = Frame(ctr_mid, bg='gray28', width=550, height=190)
        ctr_mid_up.grid(row=0, column=0, sticky="ns")
        ctr_mid_mid.grid(row=1, column=0, sticky="ns")


        ##########################################
        # Widgets
        ##########################################    
        
        # Title
        label = tk.Label(top_frame, text="Te regalo un soneto!", font=controller.title_font, 
                         fg="white", bg="gray28")
        label.grid(row=2, column=100)
        
        # Description
        message_intro = """
        Hola! Soy S.A.R.E.K, tu asistente poético personal. 
        
        A continuación te haré unas preguntas sobre cómo 
        te encuentras ahora mismo y te pediré que escribras 
        un mensaje para recomendarte un soneto totalmente 
        personalizado para ti."""
        label = tk.Label(ctr_mid_mid, text=message_intro, font=("Helvetica", 14, "bold italic"), 
                         fg="white", bg="gray28", justify=LEFT)
        label.grid(row=2, column=0)
        
        
        # Dummy
        label = tk.Label(ctr_mid_mid, text=" "*10, font=("Helvetica", 14, "bold italic"), 
                         fg="white", bg="gray28")
        label.grid(row=2, column=50)
        
        # Button
#        image = ImageTk.PhotoImage(Image.open("images/button1.png"), size=(4,4))
        button = tk.Button(ctr_right, text="Pulsa aquí para comenzar!",
                            command=lambda: controller.show_frame("AffectiveFeatures"),
                            bd=5, font=("Helvetica", 20, "bold italic"),
                            height=6, width=20, relief="raised", bg="gray28", fg="white")
        button.grid(row=4, column=10)

        # Image
        image = ImageTk.PhotoImage(Image.open("images/robot-leyendo.jpg"), size=(4,4))
        label_m = Label(ctr_left, image = image)
        label_m.image = image # linea fundamental para no perder la referencia!
        label_m.grid(row = 3, column = 3)  
        
        # Disclaimer info
        message_disclaimer = """
        Al usar este programa contribuyes a la investigación 
        en el área de la IA. Se almacenarán los datos anónimos 
        de tu uso con el sistema: tus selecciones y el texto 
        introducido de consulta"""
        
        label = tk.Label(btm_frame2, text=message_disclaimer, font=("Helvetica", 9, "bold italic"), 
                     fg="white", bg="gray28", justify=LEFT)
        label.grid(row=2, column=0)
        
        
        


class AffectiveFeatures(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ##########################################
        # Variables
        ########################################## 
        self.controller = controller
        self.result_arousal = StringVar(value = "1")
        self.result_valence = StringVar(value = "1")


        ##########################################
        # Layout
        ##########################################    
    
        # Creo los contenedores principales
        top_frame = Frame(self, bg="gray28", width=500, height=150, pady=3, padx=3)
        center = Frame(self, bg="black", width=50, height=40, padx=3, pady=3)
        btm_frame = Frame(self, bg="gray28", width=450, height=100, pady=3)
        btm_frame2 = Frame(self, bg='gray28', width=450, height=100, pady=3)
        
        # Layout de los contenedores
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        
        top_frame.grid(row=0, sticky="ew")
        center.grid(row=1, sticky="nsew")
        btm_frame.grid(row=3, sticky="ew")
        btm_frame2.grid(row=4, sticky="ew")
        
        # create the center widgets
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)
        
        ctr_left = Frame(center, bg='gray28', width=100, height=190)
        ctr_mid = Frame(center, bg='gray28', width=550, height=190, padx=3, pady=3)
        ctr_right = Frame(center, bg='gray28', width=440, height=190, padx=3, pady=3)
        
        ctr_left.grid(row=0, column=0, sticky="ns")
        ctr_mid.grid(row=0, column=1, sticky="nsew")
        ctr_right.grid(row=0, column=2, sticky="ns")
        
        # separate center in three parts
        ctr_mid_up = Frame(ctr_mid, bg='gray28', width=550, height=70)
        ctr_mid_mid = Frame(ctr_mid, bg='gray28', width=550, height=190)
        ctr_mid_up.grid(row=0, column=0, sticky="ns")
        ctr_mid_mid.grid(row=1, column=0, sticky="ns")
        
        
        ##########################################
        # Functions
        ##########################################   
        def selection_arousal():
           selection = "You selected the option " + str(self.result_arousal.get())
           print(selection)
           
           # Save info
           try:
               dct_interaction = file_presistance(PATH_USER + '/' + file_name + '.json', "json", None, "load")
               dct_interaction['selection_arousal'] = str(self.result_arousal.get())
           except:
               print()
               dct_interaction = {'selection_arousal':str(self.result_arousal.get())}
               
           # Save results  
           file_presistance(PATH_USER + '/' + file_name + '.json', "json", dct_interaction, "save")
           
           # If the other variable it's checked
           if str(self.result_valence.get()) != "1":
               self.button_next.configure(state='normal')
               

        def selection_valence():
           selection = "You selected the option " + str(self.result_valence.get())
           print(selection)
           
           # Save info
           try:
               dct_interaction = file_presistance(PATH_USER + '/' + file_name + '.json', "json", None, "load")
               dct_interaction['selection_valence'] = str(self.result_valence.get())
           except:
               dct_interaction = {'selection_valence':str(self.result_valence.get())}
        
           # Save results  
           file_presistance(PATH_USER + '/' + file_name + '.json', "json", dct_interaction, "save")
           
           # If the other variable it's checked
           if str(self.result_arousal.get()) != "1":
               self.button_next.configure(state='normal')
               
        def next_page():
            """
            When choices for affections are made it enables user to go to next page.
            It resets/set to default relevant objects within this frame (arousal, valence variables
            and next_page button status so following iterations have this frame already reset)
            """
            # Reset variables
            self.result_arousal.set("1")
            self.result_valence.set("1")
#            global timestamp, file_name
#            timestamp = pd.datetime.now()
#            file_name = str(timestamp.year) + '_' + str(timestamp.month) + '_' + str(timestamp.day) + '_' + str(timestamp.hour) + '_' + str(timestamp.minute) + '_' + str(timestamp.second)
            self.button_next.config(state="disabled")
            controller.show_frame("SonnetRecommender")

        def reset_affective():
            """
            Restart session - go back to first page and save data for a new user
            """
                    
            # Reset variables
            self.result_arousal.set("1")
            self.result_valence.set("1")
            global timestamp, file_name
            timestamp = pd.datetime.now()
            file_name = str(timestamp.year) + '_' + str(timestamp.month) + '_' + str(timestamp.day) + '_' + str(timestamp.hour) + '_' + str(timestamp.minute) + '_' + str(timestamp.second)
            self.button_next.config(state="disabled")
            controller.show_frame("StartPage")
            
        
        ##########################################
        # Widgets
        ##########################################    
        
        # Title
        label = tk.Label(top_frame, text="Te regalo un soneto!", font=controller.title_font, 
                             fg="white", bg="gray28")
        label.grid(row=2, column=100)
        
        # Subtitle
        label = tk.Label(ctr_mid_up, text="¿Cómo te sientes ahora?", 
                         font=("Helvetica", 22, "bold italic"), 
                         bg="gray28")
        label.grid(row=0, column=7)
    
        # Radiobutton - arousal
        """
        Variable: define que variable usar | value: valor que se da a esa variable | command: que hacer al presionar,
        en este caso mostrar el valor presionado
        """
        MODES = [
        ("Muy tranquilo/a", "muy_tranquilo"),
        ("Tranquilo/a", "tranquilo"),
        ("Activo/a", "activo"),
        ("Muy activo/a", "muy_activo")
        ]
        
#        shuffle(MODES) # random order of choices
        
        i = 2
        for text, mode in MODES:
            radiobutton = tk.Radiobutton(ctr_mid_mid, text=text, 
                                         variable=self.result_arousal, 
                                         value=mode, bg="gray28",
                                         font=("Helvetica", 22, "bold italic"),
                                         command=selection_arousal, state=NORMAL)
            
            radiobutton.grid(row=i+1, column=6, sticky="w")
            i +=1
        
        # Radiobutton - valence
        MODES = [
        ("Triste", "triste"),
        ("Irritado/a", "irritado"),
        ("Entusiasmado/a", "entusiasmado"),
        ("Alegre", "alegre"),
        ("Frustrado/a", "Frustrado"),
        ("Seguro/a", "seguro"),
        ]
        
        shuffle(MODES) # random order of choices
        
        i = 2
        for text, mode in MODES:
            radiobutton = tk.Radiobutton(ctr_mid_mid, text=text, 
                                         variable=self.result_valence, 
                                         value=mode, bg="gray28",
                                         font=("Helvetica", 22, "bold italic"),
                                         command=selection_valence, state=NORMAL)
            
            radiobutton.grid(row=i+1, column=18, sticky="w")
            i +=1
            
        
        # Image
        image = ImageTk.PhotoImage(Image.open("images/robot-leyendo.jpg"), size=(4,4))
        label_m = Label(ctr_left, image = image)
        label_m.image = image # linea fundamental para no perder la referencia!
        label_m.grid(row = 3, column = 3)
        
        # Button - reset
        self.button_reset = tk.Button(btm_frame, text="Reiniciar",
                            command=reset_affective,
                            bd=5, font=("Helvetica", 16, "bold italic"),
                            height=3, width=18, relief="raised", bg="gray28", fg="white",
                            state=NORMAL)
        self.button_reset.grid(row=4, column=34)
        
        
        # Button - next page
        self.button_next = tk.Button(btm_frame, text="Siguiente página",
                            command=next_page,
                            bd=5, font=("Helvetica", 16, "bold italic"),
                            height=3, width=18, relief="raised", bg="gray28", fg="white",
                            state=DISABLED)
        self.button_next.grid(row=4, column=60)





class SonnetRecommender(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        ##########################################
        # Variables
        ##########################################
        self.controller = controller
        self.choice = StringVar(value = "1")
        self.sonnet1_type = StringVar(value = "1")
        self.sonnet2_type = StringVar(value = "1")

        ##########################################
        # Layout
        ##########################################    
    
        # Creo los contenedores principales
        top_frame = Frame(self, bg="gray28", width=500, height=150, pady=3, padx=3)
        center = Frame(self, bg="black", width=50, height=40, padx=3, pady=3)
        btm_frame = Frame(self, bg="gray28", width=450, height=100, pady=3)
        btm_frame2 = Frame(self, bg='gray28', width=450, height=100, pady=3)
        
        # Layout de los contenedores
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        
        top_frame.grid(row=0, sticky="ew")
        center.grid(row=1, sticky="nsew")
        btm_frame.grid(row=3, sticky="ew")
        btm_frame2.grid(row=4, sticky="ew")
        
        # create the center widgets
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)
        
        ctr_left = Frame(center, bg='gray28', width=100, height=190)
        ctr_mid = Frame(center, bg='gray28', width=550, height=190, padx=3, pady=3)
        ctr_right = Frame(center, bg='gray28', width=10, height=190, padx=3, pady=3)
        
        ctr_left.grid(row=0, column=0, sticky="ns")
        ctr_mid.grid(row=0, column=1, sticky="nsew")
        ctr_right.grid(row=0, column=2, sticky="ns")
        
        # separate center in three parts
        ctr_mid_up = Frame(ctr_mid, bg='gray28', width=550, height=70)
        ctr_mid_mid = Frame(ctr_mid, bg='gray28', width=550, height=190)
        ctr_mid_up.grid(row=0, column=0, sticky="ns")
        ctr_mid_mid.grid(row=1, column=0, sticky="ns")
        
        
        ##########################################
        # Functions
        ##########################################
        
        def reset_recommender():
            """
            Restart session - go back to first page and save data for a new user
            """
            
            # Reset variables
#            self.result_arousal.set("1")
#            self.result_valence.set("1")
            global timestamp, file_name
            timestamp = pd.datetime.now()
            file_name = str(timestamp.year) + '_' + str(timestamp.month) + '_' + str(timestamp.day) + '_' + str(timestamp.hour) + '_' + str(timestamp.minute) + '_' + str(timestamp.second)
            # Reset variables
            self.text_box_1.delete(1.0, END)
            self.text_box_2.delete(1.0, END)
            self.query_text.delete(1.0, END)
            self.text_box_1.config(state="disabled")
            self.text_box_2.config(state="disabled")
            self.button_sel1.config(state="disabled")
            self.button_sel2.config(state="disabled")
            self.choice.set("1")
            self.sonnet1_type.set("1")
            self.sonnet2_type.set("1")
            # Go to first page
            controller.show_frame("StartPage")


        def go_query():
            """
            Send text query
            """
            query_content = self.query_text.get(1.0, 'end-1c')
#            self.label.config(text="Procesando... Puedo tardar un poco...")
            print("la consulta introducida es: ", query_content)
            
            # Save info
            try:
                dct_interaction = file_presistance(PATH_USER + '/' + file_name + '.json', "json", None, "load")
                dct_interaction['query_text'] = str(query_content)
            except:
                dct_interaction = {'query_text':str(query_content)}
            
            # Save results  
            file_presistance(PATH_USER + '/' + file_name + '.json', "json", dct_interaction, "save")
            
            ######
            # # TODO
            # Embedding of the query -> obtain sonnets most simmilar -> save info as self. variables
#            mensajeA = embedding_query_stanza(dct_interaction['query_text'], 
#                                       composition_type="joint", metric="icm", 
#                                       use_prefilter=True, log=False)
#            mensajeA = mensajeA['text'] + '\n' + '*'*10 + '\n Título: ' +  mensajeA['title'] + '\n Autor: ' +  mensajeA['author'] + '\n Año: ' +  mensajeA['year']
#            
#            mensajeB = embedding_query_stanza(dct_interaction['query_text'], 
#                                       composition_type="sum", metric="icm", 
#                                       use_prefilter=False, log=False)
#            mensajeB = mensajeB['text'] + '\n' + '*'*10 + '\n Título: ' +  mensajeB['title'] + '\n Autor: ' +  mensajeB['author'] + '\n Año: ' +  mensajeB['year']
#            
            
            def query_result(args):
                print("prueba")
                mensaje = embedding_query_stanza(query_text = args['query_text'], 
                                       composition_type= args['composition_type'], metric=args['metric'], 
                                       use_prefilter=args['use_prefilter'], log=args['log'])
                
                mensaje = mensaje['text'] + '\n' + '*'*10 + '\n Título: ' +  mensaje['title'] + '\n Autor: ' +  mensaje['author'] + '\n Año: ' +  mensaje['year']
                print(args['composition_type'])
                
                return args['composition_type'], mensaje
                
                
            arg_instances = [{'query_text':dct_interaction['query_text'], 'composition_type':"joint" , 'metric':"cosine", 'use_prefilter':False,'log':False},
                    {'query_text':dct_interaction['query_text'], 'composition_type':"sum" , 'metric':"cosine", 'use_prefilter':False,'log':False}]
            
            results = Parallel(**JOBLIB_PARAMS)(map(delayed(query_result), arg_instances))
            self.label.config(text="Completado! Aquí tienes tus sonetos   ")
            
            list_sonnet_types = []
            for composition_type, message in results:
                list_sonnet_types.append(composition_type)
                if composition_type == 'joint':
                    mensajeB = message
                else:
                    mensajeA = message

#            mensajeA = "Soneto A \n\n -------- \n Author: XXXXXX"
#            mensajeB = "Soneto B \n\n -------- \n Author: XXXXXX"
            
            # Random assing of sonnets to place 1 or place 2
#            list_sonnet_types = ["bert_sum", "bert_avg"]
            shuffle(list_sonnet_types)
            print(list_sonnet_types)
            
            
            if list_sonnet_types[0] == "sum":
                self.text_box_1.config(state=NORMAL)
                self.text_box_1.insert(1.0, mensajeA) # insert this text from position 1
                self.sonnet1_type.set("sum")
                self.text_box_2.config(state=NORMAL)
                self.text_box_2.insert(1.0, mensajeB)
                self.sonnet2_type.set("joint")
            else:
                self.text_box_1.config(state=NORMAL)
                self.text_box_1.insert(1.0, mensajeB) # insert this text from position 1
                self.sonnet1_type.set("joint")
                self.text_box_2.config(state=NORMAL)
                self.text_box_2.insert(1.0, mensajeA)
                self.sonnet2_type.set("sum")
            
            # Make selection buttons clickable
            self.button_sel1.config(state=NORMAL)
            self.button_sel2.config(state=NORMAL)
            
            #####
            
        def choice1():
            """
            Action triggered when selecting a sonnet
            """
            
            # Save info
            try:
                dct_interaction = file_presistance(PATH_USER + '/' + file_name + '.json', "json", None, "load")
                dct_interaction['sonnet_selected'] = str(self.sonnet1_type.get())
            except:
                dct_interaction = {'sonnet_selected':str(self.sonnet1_type.get())}
                
            # Save results  
            file_presistance(PATH_USER + '/' + file_name + '.json', "json", dct_interaction, "save")
            # Reset variables
            self.text_box_1.config(state="disabled")
            self.text_box_2.config(state="disabled")
            self.button_sel1.config(state="disabled")
            self.button_sel2.config(state="disabled")
            self.text_box_1.delete(1.0, END)
            self.text_box_2.delete(1.0, END)
            self.query_text.delete(1.0, END)
            self.choice.set("1")
            self.sonnet1_type.set("1")
            self.sonnet2_type.set("1")
            # Change window
            controller.show_frame("RateApp")

        def choice2():
            """
            Action triggered when selecting a sonnet
            """
            
            # Save info
            try:
                dct_interaction = file_presistance(PATH_USER + '/' + file_name + '.json', "json", None, "load")
                dct_interaction['sonnet_selected'] = str(self.sonnet2_type.get())
            except:
                dct_interaction = {'sonnet_selected':str(self.sonnet2_type.get())}
                
            # Save results  
            file_presistance(PATH_USER + '/' + file_name + '.json', "json", dct_interaction, "save")
            # Reset variables
            self.text_box_1.delete(1.0, END)
            self.text_box_2.delete(1.0, END)
            self.query_text.delete(1.0, END)
            self.text_box_1.config(state="disabled")
            self.text_box_2.config(state="disabled")
            self.button_sel1.config(state="disabled")
            self.button_sel2.config(state="disabled")
            self.choice.set("1")
            self.sonnet1_type.set("1")
            self.sonnet2_type.set("1")
            # Change window
            controller.show_frame("RateApp")
            
            
        
        ##########################################
        # Widgets
        ##########################################
        
        # Title
        label = tk.Label(top_frame, text="Te regalo un soneto!", font=controller.title_font, 
                             fg="white", bg="gray28")
        label.grid(row=2, column=100)
        
        # Subtitle
        self.label = tk.Label(ctr_mid_up, text="Dime una palabra y te sugeriré un par de sonetos: ", 
                         font=("Helvetica", 20, "bold italic"), 
                         bg="gray28")
        self.label.grid(row=0, column=0)
        
        # Image
        image = ImageTk.PhotoImage(Image.open("images/robot-leyendo.jpg"), size=(4,4))
        label_m = Label(ctr_left, image = image)
        label_m.image = image # linea fundamental para no perder la referencia!
        label_m.grid(row = 3, column = 3)
        
        # Button - reset
        self.button_reset = tk.Button(btm_frame, text="Reiniciar",
                            command=reset_recommender,
                            bd=5, font=("Helvetica", 16, "bold italic"),
                            height=3, width=18, relief="raised", bg="gray28", fg="white",
                            state=NORMAL)
        self.button_reset.grid(row=4, column=34)
        
        
        # Button - go
        self.button_go = tk.Button(ctr_mid_up, text="consultar!",
                            command=go_query,
                            bd=5, font=("Helvetica", 16, "bold italic"),
                            height=1, width=8, relief="raised", bg="gray28", fg="white",
                            state=NORMAL)
        self.button_go.grid(row=0, column=55)
        
        
        # Query text box
        self.query_text = Text(ctr_mid_up, height=2, width=30)
        self.query_text.config(bd = 0, font = ("Consolas", 12))
        self.query_text.grid(row=0, column=32)
        
        # Dummy space below title
        label = tk.Label(ctr_mid_up, text=" "*5, 
                         font=("Helvetica", 22, "bold italic"), 
                         bg="gray28")
        label.grid(row=5, column=0)
        
        # Text box sonnet 1
        self.text_box_1 = Text(ctr_mid_mid, height=20, width=40)
        self.text_box_1.config(bd = 0, font = ("Consolas", 12), state=DISABLED)
        self.text_box_1.grid(row=0, column=0)
        
        # Dummy space between boxes
        label = tk.Label(ctr_mid_mid, text=" "*5, 
                         font=("Helvetica", 22, "bold italic"), 
                         bg="gray28")
        label.grid(row=0, column=7)
        
        # Text box sonnet 2
        self.text_box_2 = Text(ctr_mid_mid, height=20, width=40)
        self.text_box_2.config(bd = 0, font = ("Consolas", 12), state=DISABLED)
        self.text_box_2.grid(row=0, column=40)
        
    
        # Select Sonnet 1
        self.button_sel1 = tk.Button(ctr_mid_mid, text="Click aquí si prefieres este",
                            command=choice1,
                            bd=5, font=("Helvetica", 16, "bold italic"),
                            height=2, width=22, relief="raised", bg="gray28", fg="white",
                            state=DISABLED)
        self.button_sel1.grid(row=65, column=0)
        
        # Button - reset
        self.button_sel2 = tk.Button(ctr_mid_mid, text="Click aquí si prefieres este",
                            command=choice2,
                            bd=5, font=("Helvetica", 16, "bold italic"),
                            height=2, width=22, relief="raised", bg="gray28", fg="white",
                            state=DISABLED)
        self.button_sel2.grid(row=65, column=40)
        

        


class RateApp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        ##########################################
        # Variables
        ##########################################
        self.result_rating = IntVar(value = 0)
        
        ##########################################
        # Layout
        ##########################################
        # Creo los contenedores principales
        top_frame = Frame(self, bg="gray28", width=500, height=150, pady=3, padx=3)
        center = Frame(self, bg="black", width=50, height=40, padx=3, pady=3)
        btm_frame = Frame(self, bg="gray28", width=450, height=100, pady=3)
        btm_frame2 = Frame(self, bg='gray28', width=450, height=100, pady=3)
        
        # Layout de los contenedores
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        
        top_frame.grid(row=0, sticky="ew")
        center.grid(row=1, sticky="nsew")
        btm_frame.grid(row=3, sticky="ew")
        btm_frame2.grid(row=4, sticky="ew")
        
        # create the center widgets
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)
        
        ctr_left = Frame(center, bg='gray28', width=100, height=190)
        ctr_mid = Frame(center, bg='gray28', width=550, height=190, padx=3, pady=3)
        ctr_right = Frame(center, bg='gray28', width=400, height=190, padx=3, pady=3)
        
        ctr_left.grid(row=0, column=0, sticky="ns")
        ctr_mid.grid(row=0, column=1, sticky="nsew")
        ctr_right.grid(row=0, column=2, sticky="ns")
        
        # separate center in three parts
        ctr_mid_up = Frame(ctr_mid, bg='gray28', width=550, height=70)
        ctr_mid_mid = Frame(ctr_mid, bg='gray28', width=550, height=190)
        ctr_mid_up.grid(row=0, column=0, sticky="ns")
        ctr_mid_mid.grid(row=1, column=0, sticky="ns")
        
        
        ##########################################
        # Functions
        ##########################################
        def reset_recommender():
            """
            Restart session - go back to first page and save data for a new user
            """
            # Reset variables
            global timestamp, file_name
            timestamp = pd.datetime.now()
            file_name = str(timestamp.year) + '_' + str(timestamp.month) + '_' + str(timestamp.day) + '_' + str(timestamp.hour) + '_' + str(timestamp.minute) + '_' + str(timestamp.second)
            
            self.result_rating.set(0)
            self.button_reset.configure(state='disabled')
            controller.show_frame("StartPage")
            
        
        def select_rating():
           selection = "You selected the option " + str(self.result_rating.get())
           print(selection)
           
           # Save info
           try:
               dct_interaction = file_presistance(PATH_USER + '/' + file_name + '.json', "json", None, "load")
               dct_interaction['selection_rating'] = str(self.result_rating.get())
           except:
               print()
               dct_interaction = {'selection_rating':str(self.result_rating.get())}
               
           # Save results  
           file_presistance(PATH_USER + '/' + file_name + '.json', "json", dct_interaction, "save")
           
           # If the other variable it's checked
           if str(self.result_rating.get()) != 0:
               self.button_reset.configure(state='normal')
        
        
        ##########################################
        # Widgets
        ##########################################
        
        # Title
        label = tk.Label(top_frame, text="Te regalo un soneto!", font=controller.title_font, 
                             fg="white", bg="gray28")
        label.grid(row=2, column=100)
        
        # Subtitle
        label = tk.Label(ctr_mid_mid, text="¿Cómo puntuas tu experiencia? \n 5 (max) - 1 (min)", 
                         font=("Helvetica", 16, "bold italic"),
                         fg="white", bg="gray28")
        label.grid(row=5, column=0)
        
        # Dummy
        label_dummy = tk.Label(ctr_mid_mid, text=" "*5, 
                         font=("Helvetica", 16, "bold italic"),
                         fg="white", bg="gray28")
        label_dummy.grid(row=4, column=10)
        
        # Radiobutton - scoring
        MODES = [
        ("5", 5),
        ("4", 4),
        ("3", 3),
        ("2", 2),
        ("1", 1)
        ]
        
        
        i = 2
        for text, mode in MODES:
            radiobutton = tk.Radiobutton(ctr_mid_mid, text=text, 
                                         variable=self.result_rating, 
                                         value=mode, bg="gray28",
                                         font=("Helvetica", 22, "bold italic"),
                                         command=select_rating, state=NORMAL)
            
            radiobutton.grid(row=i+1, column=18, sticky="w")
            i +=1
            
        
        # Button - reset
        self.button_reset = tk.Button(btm_frame, text="Reiniciar",
                            command=reset_recommender,
                            bd=5, font=("Helvetica", 16, "bold italic"),
                            height=3, width=18, relief="raised", bg="gray28", fg="white",
                            state=DISABLED)
        self.button_reset.grid(row=4, column=34)
        
        # Image
        image = ImageTk.PhotoImage(Image.open("images/robot-leyendo.jpg"), size=(4,4))
        label_m = Label(ctr_left, image = image)
        label_m.image = image # linea fundamental para no perder la referencia!
        label_m.grid(row = 3, column = 3)
        
        
if __name__ == "__main__":
    
    app = SampleApp()
    app.title("Te regalo un soneto!")
    app.resizable(width=False, height=False)
    app.iconbitmap(os.path.join(os.getcwd(), "images", "Logo.ico"))

    app.mainloop()