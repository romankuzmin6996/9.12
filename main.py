listeven=[ ]
listodd=[ ]
listpos=[ ]
listneg=[ ]
listtens=[ ]
listhundreds=[ ]

N = int(input("Cik veselu skaitļu: "))
for x in range(N):
  x = int(input("Ievadi tos:"))
  if x%2==0:
    listeven.append(x)
  if x%2==0:
    listodd.append(x)
  if x>0:
    listpos.append(x)
  if x<0:
    listneg.append(x)
  if 10<=x<100:
    listtens.append(x)
  if x>100:
    listhundreds.append(x)
  if len(listeven)>len(listodd):
    print("Vairak ir para skaitlu")
  else:
    print("Vairkas ir nepara skaitlu")
  if len(listpos)>len(listneg):
    print("Vairak ir pozitivo skaitlu")
  else:
    print("Vairakas ir negativo skaitlu")
  if len(listtens)>len(listhundreds):
    print("Vairāk ir divciparu skaitlu")
  else:
    print("Vairak ir trisciparu skaitlu")