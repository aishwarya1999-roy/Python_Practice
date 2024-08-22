def solve(digits,output,index, ans, mapping):
    if not digits:
            return []
    if index>=len(digits):
        ans.append(''.join(output[:]))
        return
    num = int(digits[index])
    str_value = mapping[num]
    for i in range(len(str_value)):
        output.append(str_value[i])
        solve(digits,output,index+1, ans, mapping)
        output.pop()

digit = ""
mapping = [' ', ' ', 'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
output= []
ans = []
solve(digit,output, 0, ans, mapping)
print(ans)