

class Compressor():

    def __init__(self, max_window=300):
        self.max_window = max_window

    def compress(self, text):
        index = 0
        output = []
        salida = ""
        while index < len(text):
            offset = 1
            length = 1
            best_offset = 0
            best_length = 0
            while index - offset >= 0:
                if text[index] == text[index-offset]:
                    length = 1
                    extra_length = 1
                    while extra_length < self.max_window and index + extra_length < len(text) and text[index + extra_length] == text[index-offset+extra_length]:
                        extra_length = extra_length + 1
                        length = length + 1

                    if length > best_length:
                        best_length = length
                        best_offset = offset
                offset = offset + 1
                current_char = ""
            if best_length == 0:
                best_length = 1
                current_char = text[index]
            output.append((best_offset, best_length, current_char))
            index = index + best_length
        return output

    def decompress(self, compressed_text):
        text = ""
        index = 0
        while index < len(compressed_text):
            offset, length, character = compressed_text[index]
            if offset == 0:
                text = text + character
            else:
                inserted_chars = 0
                text_index = len(text)
                while inserted_chars < length:
                    text = text + text[text_index-offset+inserted_chars]
                    inserted_chars = inserted_chars + 1
            index = index + 1
        return text
