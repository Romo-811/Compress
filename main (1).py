def compress_a_string(string):
    final_string = ""
    current_cout = 0
    previous_letter = string[0]
    for letter in string:
        if letter == previous_letter:
            current_cout += 1
        else:
            final_string += str(current_cout) + previous_letter
            current_cout = 1
            previous_letter = letter
    
    return final_string
        
compressed_string = compress_a_string("aaaaabbbbcccdde")
print(compressed_string)
