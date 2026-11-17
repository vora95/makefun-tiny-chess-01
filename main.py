import json,os
from urllib.request import urlopen,Request
V=[0,100,320,330,500,900,0]
D=4
Z=100000
R='kkkljkkkjkkkjkkkjkkkjkkklmmmkkkk'
PS=['kkkklmmgljikkkkollmpmmoquuuukkkk','aceecgklelmneknoelnoekmncgkkacee','giiiilkkimmmikmmillmiklmikkkgiii',R,R,'oqmkookkiggggeececcaeccaeccaecca']
KN=[14,18,31,33,-14,-18,-31,-33];KG=[1,15,16,17,-1,-15,-16,-17]
DS=[KN,[15,17,-15,-17],[1,16,-1,-16],KG,KG];CS=[(4,1,6,5,7),(4,2,2,3,0),(116,4,118,117,119),(116,8,114,115,112)]
PT=[[(ord(t[(q>>4)*4+min(q&7,7-(q&7))])-97)*5-50 if not q&136 else 0 for q in range(128)] for t in PS]
O=lambda m:V[abs(b[(m>>7)&127])]*10-V[abs(b[m&127])]
P=lambda u,o:json.load(urlopen(Request(u,json.dumps(o).encode())))
b=[0]*128;s=1;c=15;e=-1;kw=4;kb=116;U=[]
def F(f):
 global b,s,c,e,kw,kb
 b=[0]*128;p=f.split();r=7;q=0
 for ch in p[0]:
  if(ch=='/'):r-=1;q=0
  elif ch.isdigit():q+=int(ch)
  else:
   sq=r*16+q;pc='PNBRQK'.index(ch.upper())+1
   if ch.islower():pc=-pc
   b[sq]=pc;q+=1
   if pc==6:kw=sq
   elif pc==-6:kb=sq
 s=1 if p[1]=='w' else -1;c=sum(1<<i for i,k in enumerate('KQkq') if k in p[2])
 e=-1
 if p[3]!='-':e=ord(p[3][0])-97+(int(p[3][1])-1)*16
def A(q,w):
 P2=1 if w else -1
 for d in(15,17):
  t=q-d*P2
  if t&136==0 and b[t]==P2:return 1
 for d in KN:
  t=q+d
  if t&136==0 and b[t]==2*P2:return 1
 for d in KG:
  t=q+d
  if t&136==0 and b[t]==6*P2:return 1
  while t&136==0:
   p=b[t]
   if p:
    if p==5*P2 or p==(3 if abs(d) in(15,17) else 4)*P2:return 1
    break
   t+=d
 return 0
def G(o=False):
 ms=[]
 for q in range(128):
  if q&136:continue
  p=b[q]
  if not p or(p>0)!=(s==1):continue
  a=abs(p)
  if a==1:
   d=16*s
   for dd in(0,-1,1):
    t=q+d+dd
    if t&136:continue
    if(dd==0 and b[t])or(dd and b[t] and(b[t]>0)==(s==1))or(dd and not b[t] and t!=e):continue
    if(t>>4)==(7 if s==1 else 0):ms.append(q|(t<<7)|(5<<14))
    elif dd or not o:
     ms.append(q|(t<<7))
     if not dd and(q>>4)==(1 if s==1 else 6) and b[t+d]==0:ms.append(q|((t+d)<<7))
  else:
   ds=DS[a-2]
   for dd in ds:
    t=q+dd
    while t&136==0:
     if b[t]:
      if(b[t]>0)!=(s==1):ms.append(q|(t<<7))
      break
     if not o:ms.append(q|(t<<7))
     if not 2<a<6:break
     t+=dd
   if a==6 and not o:
    for K,R,k,d,r in CS:
     if q==K and c&R and b[d]==b[k]==b[k-1]==0 and b[r]==4*s and not A(K,s==-1) and not A(d,s==-1):ms.append(K|(k<<7))
 return ms
def M(m):
 global s,c,e,kw,kb
 U.append((b[:],s,c,e,kw,kb))
 f=m&127;t=(m>>7)&127;q=m>>14;pc=b[f];cp=b[t]
 if abs(pc)==1 and t==e and cp==0:
  x=t-16 if s==1 else t+16;cp=b[x];b[x]=0
 b[t]=q if q else pc;b[f]=0
 if abs(pc)==6:
  if abs(t-f)==2:
   r=t+1 if t>f else t-2;w=t-1 if t>f else t+1;b[w]=b[r];b[r]=0
  if pc==6:kw=t
  else:kb=t
 for sq,bit in((0,2),(7,1),(112,8),(119,4),(4,3),(116,12)):
  if f==sq or t==sq:c&=~bit
 e=(f+t)//2 if abs(pc)==1 and abs(t-f)==32 else -1
 s=-s
def W():
 global s,c,e,kw,kb
 bb,s,c,e,kw,kb=U.pop()
 b[:]=bb
def E():
 sc=0
 for q in range(128):
  p=b[q]
  if q&136 or not p:continue
  a=abs(p)
  if p>0:sc+=V[a]+PT[a-1][q]
  else:sc-=V[a]+PT[a-1][q^112]
 return sc if s==1 else -sc
def S(d,a,bb,pl):
 chk=A(kw if s==1 else kb,s==-1)
 if d<=0:
  if pl>64:return E()
  if not chk:
   v=E()
   if v>=bb:return v
   if v>a:a=v
  ms=G(True) if not chk else G()
 else:ms=G()
 ms.sort(key=O,reverse=True)
 n=0
 for m in ms:
  M(m)
  if A(kb if s==1 else kw,s==1):W();continue
  n+=1
  sc=-S(d-1,-bb,-a,pl+1)
  W()
  if sc>a:a=sc
  if a>=bb:break
 if d<=0:
  if chk and n==0:return -Z+pl
  return a
 if n==0:return -Z+pl if chk else 0
 return a
def R(lg):
 bm=lg[0];a=-Z
 lg.sort(key=O,reverse=True)
 for m in lg:
  M(m)
  if A(kb if s==1 else kw,s==1):W();continue
  sc=-S(D-1,-Z,-a,1)
  W()
  if sc>a:a=sc;bm=m
 return bm
Y=lambda x:chr(97+(x&7))+str((x>>4)+1)
def C(m):
 return Y(m&127)+Y((m>>7)&127)+('nbrq'[(m>>14)-2] if m>>14 else '')
def main():
 u=os.environ['MAKEFUN_ENV_URL']
 while True:
  g=P(u+'/game',{})
  if g['status']=='done':break
  while g['status']=='your_move':
   F(g['fen'])
   ms=[m for m in G() if C(m) in g['legal_moves']]
   g=P(u+'/move',{'game':g['game'],'move':C(R(ms))})
main()
