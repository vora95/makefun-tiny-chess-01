import json,time,os
import urllib.request as R
W=99999
V=":PQbz0"
K=(-33,-31,-18,-14,14,18,31,33);I=(-17,-15,15,17);O=(-16,-1,1,16);J=sorted(I+O)
F='abcdefgh'
S="ACEGFHJLKMOQPRTVUWY[Z]^`_acedfhi<@DH@DHLDHLPHLPTHLPTDHLP@DHL<@DH>BDHBDHJDHJNHJNPHJNPDHJNBDHJ>BDHFGHIHIJKJKLMLMNONOPQPQRS^_`aTUVWFGHIBCDE>?@A:;<=67892345./01----IJKLIJKLIJKLIJKLGHIJCDEF?@AB;<=>"
n=[0]
u=[];nn=0;ab=0;dl=0
def fen(p):
 global b,s,c,e,kw,kb
 f=p.split();b=[0]*128;i=0
 for x in f[0].split('/')[::-1]:
  for ch in x:
   if ch>'9':b[i]='PNBRQKpnbrqk'.index(ch)+1;i+=1
   else:i+=int(ch)
  i+=8
 s=(f[1]>'b')*2-1;c=sum(1<<'KQkq'.index(x)for x in f[2]if x>'-');e=-1 if f[3]<'a'else pu(f[3]+'a1')&127;kw,kb=b.index(6),b.index(12)
def atk(q,w):
 for k in(15,17):
  v=q-k if w else q+k
  if not v&136 and b[v]==1+6*(not w):return 1
 for dd in K:
  v=q+dd
  if not v&136 and b[v]==2+6*(not w):return 1
 for dd in J:
  v=q+dd
  while not v&136:
   if b[v]:
    t=b[v]-6*(not w)
    if t==5 or(t==4 and dd in O)or(t==3 and dd not in O)or(t==6 and v==q+dd):return 1
    break
   v+=dd
 return 0
def gen():
 m=[]
 def A(v):
  for x in(5,4,3,2)if v>>4==7*(s==1)else[0]:m.append(q|v<<7|x<<14)
 for q in range(128):
  p=b[q]
  if not p or(s==1)!=(p<7):continue
  if p in(1,7):
   st=q+16*s
   if not b[st]:A(st)
   if q>>4==1+5*(s<0)and not(b[st]or b[st+16*s]):m.append(q|(st+16*s)<<7)
   for dd in sorted((15*s,17*s)):
    v=q+dd
    if v&136:continue
    if b[v]and(s==1)!=(b[v]<7)and b[v]!=9+3*s:A(v)
    if not b[v]and v==e:m.append(q|v<<7)
  else:
   if p in(6,12):ds=J;sl=0
   else:ds=[0,0,K,I,O,I+O][p%6];sl=p%6>2
   for dd in ds:
    v=q+dd
    while 1:
     if v&136:break
     if not b[v]:
      m.append(q|v<<7)
      if not sl:break
      v+=dd
     else:
      if(s==1)!=(b[v]<7)and b[v]!=9+3*s:m.append(q|v<<7)
      break
   if p in(6,12)and q in(4,116):
    for d in(2,-2):
     if c>>((q//116)*2+(2-d)//4)&1 and not(b[q+d]or b[q+d//2]or(d<0 and b[q-3]))and not(atk(q,s!=1)or atk(q+d//2,s!=1)):m.append(q|(q+d)<<7)
 return m
def mk(mv):
 global s,c,e,kw,kb
 fr=mv&127;to=(mv>>7)&127;pr=(mv>>14)&7;pc=b[fr];u.append((b[:],s,c,e,kw,kb))
 if pc%6==1 and to==e and not b[to]:
  ep=to-16*s;b[ep]=0
 if pc in(6,12)and abs(to-fr)==2:
  k=to-fr;r=fr+3 if k==2 else fr-4;b[fr+k//2]=b[r];b[r]=0
 b[to]=pc;b[fr]=0
 if pr:
  pp=pr+6*(pc>6);b[to]=pp
 if pc==6:kw=to
 if pc==12:kb=to
 e=(fr+to)//2 if pc%6==1 and abs(to-fr)==32 else-1
 for x in(fr,to):c&=~(int('20003001'[x%16])*((x<8)+4*(x>111)))
 s=-s
def un():
 global s,c,e,kw,kb
 b[:],s,c,e,kw,kb=u.pop()
def uc(x):
 a=x&127;b=(x>>7)&127;p=(x>>14)&7
 return F[a&7]+str((a>>4)+1)+F[b&7]+str((b>>4)+1)+('nbrq'[p-2] if p else'')
def pu(x):
 f=lambda y:ord(y[0])-97+(int(y[1])-1)*16
 return f(x[:2])|(f(x[2:4])<<7)|((('nbrq'.index(x[4])+2)<<14)if x[4:]else 0)
def ev():
 mg=0
 for q in range(128):
  p=b[q]
  if p:
   w=p>6;t=p-6*w;g=1-2*w;r=q>>4;f=q&7;i=(r+w*(7-2*r))*4+min(f,7-f)
   mg+=g*((ord(V[t-1])-48)*10+ord(S[i+(t-1)*32])-70)
   if p in(1,7):
    t=2*(p==1)-1;a=r-3 if t==1 else 4-r
    if a>=0 and not any(b[rr*16+ff]==8-p for rr in range(r+t,8-9*(t==-1),t)for ff in(f-1,f,f+1)):mg+=([8,18,32,55,55][a])*t
 return s*mg
def ng(a,bb,d):
 global nn,ab
 nn+=1
 if nn%1024==0 and time.time()>dl:
  ab=1;return 0
 if d<=0:return ev()
 ck=atk((kw,kb)[s==-1],s!=1)
 m=gen()
 lg=0
 for mv in m:
  mk(mv)
  if atk((kb,kw)[s==-1],s==1):un();continue
  lg+=1;sc=-ng(-bb,-a,d-1);un()
  if ab:return 0
  a=max(a,sc)
  if a>=bb:break
 if not lg:return -W*ck
 return a
def rt(lg):
 global nn,ab,dl
 bm=lg[0];bs=-W;dl=time.time()+8
 for d in range(1,17):
  nn=0;ab=0
  for mv in lg:
   mk(mv)
   if atk((kb,kw)[s==-1],s==1):un();continue
   sc=-ng(-W,W,d-1);un()
   if ab:break
   if sc>bs:bs=sc;bm=mv
  if ab:break
 return bm
E=os.getenv("MAKEFUN_ENV_URL","")
def P(pa,bo):
 return json.loads(R.urlopen(R.Request(E+pa,json.dumps(bo).encode(),{'Content-Type':'application/json'})).read())
def M():
 while 1:
  g=P('/next',{}).get('game')
  if not g:return
  fen(g['fen']);v=uc(rt([pu(x)for x in g['legal_moves']]))
  P('/move',{'game_id':g['game_id'],'move':v})
__name__=='__main__'and M()
