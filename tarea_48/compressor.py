

class Compressor():

    def __init__(self, max_window=300):
        # numero máximo de caracteres previos de búsqueda
        self.max_window = max_window

    def compress(self, text):
        index = 0
        output = []
        while index < len(text):
            offset = 1
            length = 1
            best_offset = 0
            best_length = 0
            # buscar coincidencias en los caracteres previos
            while index - offset >= 0 or offset >= self.max_window:
                if text[index] == text[index-offset]:
                    length = 1
                    extra_length = 1
                    # si hay coincidencia se mira si los siguientes caracteres tambien son iguales
                    while extra_length < self.max_window and \
                        index + extra_length < len(text) and \
                            text[index + extra_length] == text[index-offset+extra_length]:
                        extra_length = extra_length + 1
                        length = length + 1
                    # si la coincidencia es más larga que una previa se guarda
                    if length > best_length:
                        best_length = length
                        best_offset = offset
                offset = offset + 1
            # se genera la tupla correspondiente
            # en formato offset,length, char (vacío si hay coincidencia previa)
            current_char = ""
            if best_length == 0:
                best_length = 1
                current_char = text[index]
            output.append((best_offset, best_length, current_char))
            # se avanza en la cadena de entrada la longitud de la coincidencia
            index = index + best_length
        return output

    def decompress(self, compressed_text):
        text = ""
        index = 0
        while index < len(compressed_text):
            offset, length, character = compressed_text[index]
            # si no había offset se añade el caracter
            if offset == 0:
                text = text + character
            else:
                # si habia offset
                # se añaden las coincidencias una a una
                # hasta la longitud codificada
                inserted_chars = 0
                text_index = len(text)
                while inserted_chars < length:
                    text = text + text[text_index-offset+inserted_chars]
                    inserted_chars = inserted_chars + 1
            index = index + 1
        return text
