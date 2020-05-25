a = "bilal123"
random.seed("key")
a = random.sample(a,len(a)

#variabel a udah keacak
random.seed("ini text yang mau di enc")
result="".join([random.choice(a) for i in range(10)])
print result
