import json,os,urllib.request as U;E=os.getenv('MAKEFUN_ENV_URL');W=100000;V=[0,100,320,330,500,900,0];J=[-31,-33,-14,-18,14,18,31,33];B=[15,17,-15,-17];R=[1,-1,16,-16];b=[0]*128;s=1;c=0;e=-1;n=[0]*13;u=[]
def dec(a):
 return(a&127,a>>7&127,a>>14)
nn=0;lm=0;ab=0
def F(h):
 global b,s,c,e,n,u,kw,kb;f=h.split();b=[0]*128;n=[0]*13;a=112
 for d in f[0]:
  if d=='/':
   a-=24
  elif d.isdigit():
   a+=int(d)
  else:
   g='PNBRQKpnbrqk'.index(d)+1;b[a]=g;n[g]+=1;a+=1
 s=2*(f[1]=='w')-1;c=0;e=-1;u=[];kw=b.index(6);kb=b.index(12)
def K(c,f):
 d=6-6*f
 for a in(c-15,c-17)if f else(c+15,c+17):
  if not a&136 and b[a]==1+d:
   return 1
 for i,j,g in((J,2,0),(R+B,6,0),(B,3,1),(R,4,1)):
  for h in i:
   a=c+h
   while not a&136:
    e=b[a]
    if e:
     if e==j+d or(g and e==5+d):
      return 1
     break
    if not g:
     break
    a+=h
 return 0
def ev():
 S=0
 for sq in range(128):
  if sq&136:
   continue
  p=b[sq]
  if not p:
   continue
  w=p<=6;t=p if w else p-6;r=sq>>4;f=sq&7;rl=r if w else 7-r;cc=min(f,7-f)+min(rl,7-rl)
  if t==1:
   vv=100+[0,0,4,8,14,24,40,0][rl]+([0,0,0,10,15,10,5,0][rl]if f in(3,4)else 0);kq=kw if w else kb
   if abs(f-(kq&7))<=1 and rl==(kq>>4 if w else 7-(kq>>4))+1:
    vv+=5
  elif t==2:
   vv=320+6*cc-20
  elif t==3:
   vv=330+4*cc-8
  elif t==4:
   vv=500+(15 if rl==6 else 0)+(5 if rl==0 and f in(3,4)else 0)
  elif t==5:
   vv=900+2*cc-6
  else:
   vv=0
  S+=vv if w else-vv
 ph=320*(n[2]+n[8])+330*(n[3]+n[9])+500*(n[4]+n[10])+900*(n[5]+n[11])
 if ph>6400:
  ph=6400
 for w,sg in((True,1),(False,-1)):
  kq=kw if w else kb;f=kq&7;rl=kq>>4 if w else 7-(kq>>4);mg=[20,25,10,0][min(f,7-f)]if rl==0 else max(-50,-15*rl);eg=8*(min(f,7-f)+min(rl,7-rl))-24;S+=sg*(mg*ph+eg*(6400-ph))//6400
 S+=30*((n[3]>1)-(n[9]>1));return S if s==1 else-S
def G(k=0):
 l=[];e=s==1;f=lambda b,s=0:l.append(c|b<<7|s<<14);m=lambda b:[f(b,z)for z in(5,4,3,2)];n=lambda b:(b>6)==e and b%6
 for c in range(128):
  if c&136:
   continue
  g=b[c]
  if g==0 or(g<=6)!=e:
   continue
  i=g if g<=6 else g-6
  if i==1:
   o=c>>4;d=32*e-16;q=6-5*e;p=7*e;j=c+d
   if b[j]==0:
    if o+(d>>4)==p:
     m(j)
    elif not k:
     f(j)
     if o==q and b[c+2*d]==0:
      f(c+2*d)
   for r in(d-1,d+1):
    a=c+r
    if a&136:
     continue
    h=b[a]
    if n(h):
     if a>>4==p:
      m(a)
     else:
      f(a)
  else:
   for d in(J,B,R,B+R,R+B)[i-2]:
    a=c+d
    while not a&136:
     h=b[a]
     if not h and(not k)or n(h):
      f(a)
     if h or i==2 or i==6:
      break
     a+=d
 return l
def k(h):
 global s,kw,kb;e,a,d=dec(h);c=b[e];i=c<=6;f=b[a];u.append((b[:],n[:],kw,kb))
 if f:
  b[a]=0;n[f]-=1
 g=(d if i else d+6)if d else c;b[a]=g;b[e]=0
 if c==6:
  kw=a
 elif c==12:
  kb=a
 n[c]-=1;n[g]+=1;s=-s
def X():
 global s,kw,kb;b[:],n[:],kw,kb=u.pop();s=-s
def o(a):
 def S(f):
  g,h,c=dec(f);d=b[h];e=W+10*V[d%6]-V[b[g]%6]if d else 0
  if c:
   e+=90000+V[c]
  return e
 a.sort(key=S,reverse=1)
def N(e,a,g,h):
 global nn,ab;nn+=1
 if nn>=lm:
  ab=1;return 0
 if e<=0:
  return ev()
 i=K((kw,kb)[s==-1],s==-1);b=[]
 for c in G():
  k(c)
  if not K((kb,kw)[s==-1],s==1):
   b.append(c)
  X()
 if not b:
  return-90000+h if i else 0
 o(b);f=-W
 for c in b:
  k(c);d=-N(e-1,-g,-a,h+1);X()
  if ab:
   return 0
  if d>f:
   f=d
  if d>a:
   a=d
   if a>=g:
    break
 return f
def t(a):
 global nn,lm,ab;c=a[0]
 for g in range(1,33):
  nn=0;lm=15000;ab=0;b=-W-1;h=W+1;d=a[0]
  for e in a:
   k(e);f=-N(g-1,-h,-b,1);X()
   if ab:
    break
   if f>b:
    b=f;d=e
  if ab:
   break
  c=d
 return c
def Q(a,b):
 return json.load(U.urlopen(E+a,data=json.dumps(b).encode()))
def C(c):
 a=lambda f:chr(97+(f&7))+str((f>>4)+1);d,e,b=dec(c);return a(d)+a(e)+('nbrq'[b-2]if b else'')
def P(a):
 b=int(a[1])*16+ord(a[0])-113;c=int(a[3])*16+ord(a[2])-113;d=' pnbrqk'.index(a[4:]);return b|c<<7|d<<14
def M():
 if not E:
  exit(1)
 while 1:
  a=Q('/game',{})
  if a['status']=='done':
   break
  F(a['fen'])
  while a['status']=='your_move':
   b=a['legal_moves'];c=[P(x)for x in b];d=C(t(c));a=Q('/move',{'game':a['game'],'move':d})
   if a['status']=='your_move':
    F(a['fen'])
M()
