
from translator import MorseCodeTranslator
from tkinter import Tk,Label,Text,Frame,Button,Scrollbar,IntVar
import sys
 
if "win" in sys.platform:
    from winsound import Beep


class App(object):
    """
    Classe principal
    """

    __button_width = 15
    __button_height = 1
    __button_bg = "red"
    __button_fg = "blue"
    __button_font = ("Autumn",27)
    __button_relief = "flat"

    __inputText_height = 5

    __label_fg = "#F5F5F5"
    __label_font = ("Impact",20)

    __outputText_height = 7

    __text_width = 50
    __text_bg = "yellow"
    __text_fg = "black"
    __text_font = ("Arial",14)

    frequency = 1500

    window_title = "Morse Code Translator"
    window_geometry = [600,500]
    window_bg = "gray50"



    def __init__(self):

        #  configure TK
        self.__root = Tk()
        self.__root.geometry("{}x{}".format(*self.window_geometry))
        self.__root["bg"] = self.window_bg
        self.__root.title(self.window_title)
        self.__root.resizable(False,False)
        self.__root.focus_force()
        self.__root.bind("<Return>",self.translate)

        self.__playing = False
        self.__waitVar = IntVar()

        # construct interface to the program
        self.build()



    def build(self):
        """
        mwethod for interface do program.
        """

        # text.
        Label(
            self.__root,
            bg = self.window_bg,
            font = self.__label_font,
            fg = self.__label_fg,
            text = "Input:",
            pady = 10
            ).pack()


        # frame paracolor to the input.
        input_frame = Frame(self.__root,bg=self.window_bg)
        input_frame.pack()

        # text of input height and width.
        self.__inputText = Text(
            input_frame,
            width = self.__text_width,
            height = self.__inputText_height,
            bg = self.__text_bg,
            fg= self.__text_fg,
            font = self.__text_font,
            wrap = "word"
            )
        self.__inputText.insert(0.0," ")

        # adding scrollbar to the input.
        scrollbar = Scrollbar(input_frame)
        scrollbar.pack(side="right",fill="y")
        self.__inputText.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.__inputText.yview)

        self.__inputText.pack()
        

        # label output screen for text.
        Label(
            self.__root,
            bg = self.window_bg,
            font = self.__label_font,
            fg = self.__label_fg,
            text = "Output:",
            pady = 10
            ).pack()


        # frame for the output.
        output_frame = Frame(self.__root,bg=self.window_bg)
        output_frame.pack()


        # paracolor text for the output.
        self.__outputText = Text(
            output_frame,
            width = self.__text_width,
            height = self.__outputText_height,
            bg = self.__text_bg,
            fg= self.__text_fg,
            font = self.__text_font,
            wrap = "word"
            )
        self.__outputText.insert(0.0," ")


        # scrollbar for the out put screen.
        scrollbar = Scrollbar(output_frame)
        scrollbar.pack(side="right",fill="y")
        self.__outputText.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.__outputText.yview)

        self.__outputText.pack()

        
        # frame for the insert.
        buttons_frame = Frame(self.__root,bg=self.window_bg,pady=20)
        buttons_frame.pack()

        # buttons for the left side color is black.
        button1_frame = Frame(buttons_frame,bg="black",padx=2,pady=2)
        button1_frame.pack(side="left")

        # button text ,color.
        self.__button1 = Button(
            button1_frame,
            width = self.__button_width,
            height = self.__button_height,
            relief = self.__button_relief,
            bg = self.__button_bg,
            fg = self.__button_fg,
            font = self.__button_font,
            text = "Translate",
            command = self.translate
        )
        self.__button1.pack()



        #operating system
        if "win" in sys.platform:

            Label(buttons_frame,bg=self.window_bg,padx=5).pack(side="left")

            # Cria uma "borda" para o botão.
            button2_frame = Frame(buttons_frame,bg="black",padx=2,pady=2)
            button2_frame.pack(side="left")

            # Cria botão para reproduzir som do código morse.
            self.__button2 = Button(
                button2_frame,
                width = self.__button_width,
                height = self.__button_height,
                relief = self.__button_relief,
                bg = self.__button_bg,
                fg = self.__button_fg,
                font = self.__button_font,
                text = "Play",
                command = self.play
            )
            self.__button2.pack()

        self.__root.mainloop()



    def play(self):
        

        # Para a reprodução.
        if self.__playing:
            self.__playing = False
            return

        # text for the output screen.
        text = self.__outputText.get(0.0,"end")
        if not text or text.isspace() or not MorseCodeTranslator.isMorse(text): return

        # playing sound on text .
        self.__playing = True
        self.__button2.config(text = "Stop")


        #dividing the text .
        for char in text.split(" "):

            # for the char to be split.
            for l in char:

                if not self.__playing:
                    break
                
                # verify wheter the symbol matches to morse code.
                if l == MorseCodeTranslator.errorChar:
                    continue

                # To beep for dot 0,3 
                if l == ".":
                    Beep(self.frequency,300)

                # To beep for dash 0.6 .
                elif l == "-":
                    Beep(self.frequency,600)

                # wait if the symbol comes /.
                elif l == "/":
                    self.wait(2100)
            
            
            if not self.__playing:
                break

            # wait for 0.9 sec.
            self.wait(900)


        # Inform to play .
        self.__playing = False
        self.__button2.config(text = "Play")



    def translate(self,event=None):
        """
        method for translate to morse code
        """


        # input text.
        text = self.__inputText.get(0.0,"end")
        if not text: return

        # for the output text.
        self.__outputText.delete(0.0,"end")
        self.__outputText.insert(0.0,MorseCodeTranslator.translate(text))



    def wait(self,ms):
        """
        sound wait for ms.
        """

        self.__waitVar.set(0)
        self.__root.after(ms,self.__waitVar.set,1)
        self.__root.wait_variable(self.__waitVar)
        self.__waitVar.set(0)



if __name__ == "__main__":
    App()

    
