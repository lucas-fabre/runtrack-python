def pyramid(string):
    start = 0
    length = 1
    while start < len(string):
        line = string[start: start+length]
        
        print(line)
        start += length
        length += 1

pyramid("abcdefghijklmnopqrstuvwxyz" * 10)