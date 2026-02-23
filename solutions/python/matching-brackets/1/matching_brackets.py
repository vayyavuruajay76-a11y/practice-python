def is_paired(input_string):
    stack=[]
    mapping={")": "(", "}": "{", "]": "["}
    for ch in input_string:
        if ch in mapping.values():
            stack.append(ch)
        elif ch in mapping.keys():
            if not stack or stack.pop()!=mapping[ch]:
                return False

    return len(stack)==0
        
