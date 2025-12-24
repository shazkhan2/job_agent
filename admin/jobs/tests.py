# def caesar_cipher(text, shift, encrypt=True):
#     if not isinstance (shift, int):
#         return 'Shift must be an integer value.'
#     if shift < 0 or shift > 25:
#         return 'Shift must be an integer between 1 and 25.'
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     shifted_alphabet = alphabet[shift:] + alphabet[:shift]
#     translation_table = str.maketrans(alphabet+alphabet.upper(), shifted_alphabet+shifted_alphabet.upper())
#     return text.translate(translation_table)
# def encrypt(text, shift):
#     return caesar_cipher(text, shift, encrypt=True)
# def decrypt(text, shift, encrypt=False):
#     return caesar_cipher(text, shift, encrypt=True)

# decrypted_text = decrypt("Pbhentr vf sbhaq va hayvxryl cynprf", 13)    
# print(decrypted_text)
full_dot = '●'
empty_dot = '○'
def create_character(character_name, strength, intelligence, charisma):
    stats = [strength, intelligence, charisma]
    if not isinstance(character_name, str):
        return "The character name should be a string"
    if len(character_name) > 10:
        return "The character name is too long"
    if " " in character_name:
        return "The character name should not contain spaces"
    for stat in stats:
        if not isinstance(stat, int):
            return "All stats should be integers"
        if stat < 1:
            return "All stats should be no less than 1"
        if stat > 4:
            return "All stats should be no more than 4"
    if sum(stats) != 7:
        return "The character should start with 7 points"
    str_bar = (full_dot * strength) + (empty_dot * (10 - strength))
    int_bar = (full_dot * intelligence) + (empty_dot * (10 - intelligence))
    cha_bar = (full_dot * charisma) + (empty_dot * (10 - charisma))
    result = f"{character_name}\nSTR {str_bar}\nINT {int_bar}\nCHA {cha_bar}"
    return result
print(create_character("ren", 4, 2, 1))
