def get_email(s):
    
    output = ""
    for i in range(len(s)):
        if s[i] == '@':
            output = "@"
            j = i
            while s[i] != ' ' and i < len(s)-1:
                print(s[i])
                i = i+1
                output = output + s[i]
            while s[j] != ' ' and j > 0 and s[j] != ':':
                j = j-1
                output = s[j] + output
            if '.' in output:
                if output[-1] == ' ':
                    output = output[:-1]
                return output[1:]
            else:
                output = ''
    return output
            
print(len(get_email('mailto:info@hope-village.com')))