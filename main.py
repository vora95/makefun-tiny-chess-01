import json,os,sys,urllib.request as U;E=os.environ.get("MAKEFUN_ENV_URL","");W=100000
V=[0,100,320,330,500,900,0];KN=[-31,-33,-14,-18,14,18,31,33];BI=[15,17,-15,-17];RO=[1,-1,16,-16];KI=RO+BI
b=[0]*128;c=0;e=-1
S=lambda a:"abcdefgh"[a&7]+str(a//16+1)
Q=lambda s,a:(int(s[a+1])-1)*16+ord(s[a])-97
def F(f):
 global b,s,n,u,kw,kb;p=f.split();b=[0]*128;n=[0]*13;q=112
 for h in p[0]:
  if h=="/":q-=24
  elif h.isdigit():q+=int(h)
  else:d="PNBRQKpnbrqk".index(h)+1;b[q]=d;n[d]+=1;q+=1
 s=2*(p[1]=="w")-1;u=[];kw=b.index(6);kb=b.index(12)
def K(q,w):
 o=0 if w else 6
 for t in(q-15,q-17)if w else(q+15,q+17):
  if not t&0x88 and b[t]==1+o:return True
 for z,y in((KN,2),(KI,6)):
  for d in z:
   t=q+d
   if not t&0x88 and b[t]==y+o:return True
 for z,y in((BI,3),(RO,4)):
  for d in z:
   t=q+d
   while not t&0x88:
    p=b[t]
    if p:
     if p in(y+o,5+o):return True
     break
    t+=d
 return False
def ev():
 sc=0
 for q in range(128):
  if q&0x88 or not(p:=b[q]):continue
  w=p<=6;t=p if w else p-6;r=q>>4;f=q&7;l=r if w else 7-r;g=min(f,7-f)+min(l,7-l)
  if t==1:
   v=100+[0,0,4,8,14,24,40,0][l]+([0,0,0,10,15,10,5,0][l] if f in(3,4) else 0);j=kw if w else kb
   if abs(f-(j&7))<=1 and l==(j>>4 if w else 7-(j>>4))+1:v+=5
  else:v=(0,0,320+6*g-20,330+4*g-8,500+(15 if l==6 else 0)+(5 if l==0 and f in(3,4) else 0),900+2*g-6,0)[t]
  sc+=v if w else -v
 h=sum(V[i]*(n[i]+n[i+6])for i in(2,3,4,5));h=min(h,6400)
 for j,g in((kw,1),(kb,-1)):
  f=j&7;l=j>>4 if g>0 else 7-(j>>4);c=min(f,7-f);m=[20,25,10,0][c] if l==0 else max(-50,-15*l);z=8*(c+min(l,7-l))-24;sc+=g*(m*h+z*(6400-h))//6400
 sc+=30*((n[3]>1)-(n[9]>1));return sc if s>0 else -sc
def G():
 w=s>0;m=[]
 def A(a,y):
  if(y>>4)==(7,0)[w==0]:
   for r in(5,4,3,2):m.append(a|(y<<7)|(r<<14))
  else:m.append(a|(y<<7))
 for q in range(128):
  if q&0x88 or not(p:=b[q])or(p<=6)!=w:continue
  t=p if p<=6 else p-6
  if t==1:
   d=(16,-16)[w==0];v=q+d
   if b[v]==0:
    A(q,v)
    if(q>>4)==(1,6)[w==0]:
     x=q+2*d
     if b[x]==0:m.append(q|(x<<7))
   for z in(d-1,d+1):
    y=q+z
    if y&0x88:continue
    r=b[y]
    if r and(r<=6)!=w and r%6:A(q,y)
  else:
   for d in(KN,BI,RO,BI+RO,KI)[t-2]:
    y=q+d
    while not y&0x88:
     r=b[y]
     if r==0:m.append(q|(y<<7))
     else:
      if(r<=6)!=w and r%6:m.append(q|(y<<7))
      break
     if t in(2,6):break
     y+=d
 return m
def k(v):
 global s,kw,kb;f=v&127;y=(v>>7)&127;r=(v>>14)&7;p=b[f];w=p<=6;z=b[y];u.append((v,z))
 if z:b[y]=0;n[z]-=1
 a=(r if w else r+6) if r else p;b[y]=a;b[f]=0
 if p==6:kw=y
 elif p==12:kb=y
 n[p]-=1;n[a]+=1;s=-s;return z
def X():
 global s,kw,kb;v,z=u.pop();f=v&127;y=(v>>7)&127;r=(v>>14)&7;p=b[y];s=-s;n[p]-=1
 if r:p=1 if p<=6 else 7
 n[p]+=1;b[f]=p;b[y]=0
 if z:b[y]=z;n[z]+=1
 if p==6:kw=f
 elif p==12:kb=f
def o(v):v.sort(key=lambda m:(W+10*V[b[(m>>7)&127]%6 or 6]-V[b[m&127]%6 or 6]if b[(m>>7)&127]else 0)+(90000+V[(m>>14)&7]if(m>>14)&7 else 0),reverse=True)
def N(d,a,A,y):
 global nn,ab
 if d<=0:return ev()
 nn+=1
 if nn>=lm:ab=True;return 0
 v=G();o(v);z=-W-1;l=0
 for m in v:
  k(m)
  if K(kb if s>0 else kw,s>0):X();continue
  l+=1;g=-N(d-1,-A,-a,y+1);X()
  if ab:return 0
  if g>z:z=g
  if g>a:a=g
  if a>=A:break
 if l==0:return -W+y if K(kw if s>0 else kb,s<0) else 0
 return z
def t(v):
 global nn,lm,ab
 g={m:0 for m in v};o(v);z=v[0]
 for d in range(1,33):
  nn=0;lm=15e3;ab=False;v.sort(key=lambda m:-g[m]);a=-W-1;A=W+1;h=v[0]
  for m in v:
   k(m);x=-N(d-1,-A,-a,1);X()
   if ab:break
   g[m]=x
   if x>a:a=x;h=m
  if ab:break
  z=h
 return z
def C(m):r=(m>>14)&7;return S(m&127)+S((m>>7)&127)+("  nbrq"[r] if r else "")
def P(u):
 f=Q(u,0);y=Q(u,2);r=" pnbrqk".index(u[4]) if len(u)==5 else 0;return f|(y<<7)|(r<<14)
def q(a,z):
 try:
  with U.urlopen(E+a,json.dumps(z).encode()) as r:return json.load(r)
 except U.HTTPError as x:sys.exit(x.code)
def M():
 if not E:sys.exit(1)
 while 1:
  g=q("/game",{})
  if g["status"]=="done":break
  F(g["fen"])
  while g["status"]=="your_move":
   g=q("/move",{"game":g["game"],"move":C(t([P(x) for x in g["legal_moves"]]))})
   if g["status"]=="your_move":F(g["fen"])
M()
