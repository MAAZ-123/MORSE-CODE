
class MorseCodeTranslator(object):
    """
    class for alphabet that accept from user
    """

    __morse_code = {
        'A':'.-',
        'B':'-...',
        'C':'-.-.',
        'D':'-..',
        'E':'.',
        'F':'..-.',
        'G':'--.',
        'H':'....',
        'I':'..',
        'J':'.---',
        'K':'-.-',
        'L':'.-..',
        'M':'--',
        'N':'-.',
        'O':'---',
        'P':'.--.',
        'Q':'--.-',
        'R':'.-.',
        'S':'...',
        'T':'-',
        'U':'..-',
        'V':'...-',
        'W':'.--',
        'X':'-..-',
        'Y':'-.--',
        'Z':'--..',

        '1':'.----',
        '2':'..---',
        '3':'...--',
        '4':'....-',
        '5':'.....',
        '6':'-....',
        '7':'--...',
        '8':'---..',
        '9':'----.',
        '0':'-----',

        '.':'.-.-.-',
        ',':'--..--',
        '?':'..--..',
        '‘':'.----.',
        '!':'.-.--',
        '/':'-..-.',
        '(':'-.--.',
        ')':'-.--.-',
        '&':'.-...',
        ':':'---...',
        ';':'-.-.-.',
        '=':'-...-',
        '-':'-....-',
        '_':'..--.-',
        '"':'.-..-.',
        '$':'...-..-',
        '@':'.--.-.',
    }

    errorChar = "�"


    @staticmethod
    def getMorseCodeTable():
       
        return MorseCodeTranslator.__morse_code


    @staticmethod
    def isMorse(text):
      
        return all( 
            map( lambda char: False if not char in [".","-"," ","/","\n",MorseCodeTranslator.errorChar] else True , text) 
        )


    @staticmethod
    def translate(text):
       

        new_text = ""

        # this method is used for aplhabet to verify the symbol.

        if MorseCodeTranslator.isMorse(text):


            # dividing the letter.
            text = text.split(" ")
            

            for char in text:

                # Caso o caractere seja uma barra, ele será substituído por espaçamento.

                if char == "/":
                    new_text += " "
                    continue
                # Verify to possible to convert into character.
                if char == MorseCodeTranslator.errorChar:
                    if "\n" in char:
                        new_text += "\n"
                    continue
                

                for (key,value) in MorseCodeTranslator.__morse_code.items():
                    

                    # is used to verify that is matching the alphabet in the morse code.

                    if "\n" in char:
                        nextLine_i = char.index("\n")
                    else:
                        nextLine_i = -1

                    # transfer morse to ASCii.

                    if char.replace("\n","") == value:


                        # adding character to the text.

                        if nextLine_i != -1:

                            # is used to check its goes to next line or not.
                            if nextLine_i == 0:
                                new_text += "\n" + key
                            else:
                                new_text += key + "\n"
                        else:
                            new_text += key
        

        # covert character to morse code.
        else:
            for char in text.upper():
                
                # it verify whether the character is in line or not.
                if char == "\n":
                    new_text += "\n"
                    continue
                
                # space .
                elif char.isspace():
                    new_text += "/ "
                    continue
                
                # after space again it gona convert.
                try:  
                    new_text += MorseCodeTranslator.__morse_code[char] + " "
                except KeyError:
                    new_text += MorseCodeTranslator.errorChar + " "

            # retire end with /.
            if new_text.endswith("/"):
                new_text = new_text[:-2]

        # return to new text.
        return new_text.strip().capitalize()
