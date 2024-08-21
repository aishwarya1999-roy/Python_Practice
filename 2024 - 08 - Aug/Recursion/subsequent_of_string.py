def subseq(str1,output,ind,ans):
    if ind>=len(str1):
        if len(output)>0:
            ans.append(''.join(output))
        return
    #exclude
    subseq(str1,output,ind+1, ans)
    #include
    output.append(str1[ind])
    subseq(str1,output,ind+1, ans)

    output.pop()

str1 = 'abc'
ans = []
subseq(str1,[],0,ans)
print(ans)