---
layout: default
title: initials
data: 
- away: CHN
  count: 8
  date: 1902-09-11
  home: NY1
  id: NY1190209111
  initial: j*
  lineup: Jimmy Slagle; John Dobbs; Johnny Kling; Joe Tinker; Jim Murray; Jack Taylor;
      Jock Menefee; Johnny Evers; Carl Lundgren
- away: PHI
  count: 7
  date: 1938-08-31
  home: SLN
  id: SLN193808312
  initial: '*m'
  lineup: Terry Moore; Stu Martin; Pepper Martin; Joe Medwick; Johnny Mize; Don Gutteridge;
      Lynn Myers; Herb Bremer; Bill McGee
- away: BSN
  count: 7
  date: 1907-07-03
  home: PHI
  id: PHI190707030
  initial: '*b'
  lineup: Al Bridwell; Fred Tenney; Dave Brain; Ginger Beaumont; Johnny Bates; Frank   Burke; Claude Ritchey; Sam Brown; Jake Boultes
- away: MIA
  count: 4
  date: 2023-07-25
  home: TBA
  id: TBA202307250
  initial: js
  lineup: Luis Arraez; Jorge Soler; Garrett Cooper; Jesus Sanchez; Bryan De La Cruz; Jean Segura; Joey Wendle; Jacob Stallings; Jon Berti
- away: HOU
  count: 4
  date: 1969-07-09
  home: SFN
  id: SFN196907090
  initial: bb
  lineup: Tito Fuentes; Ron Hunt; Bobby Bonds; Willie Mays; Jim Davenport; Ken Henderson; Bob Burda; Bob Barton; Bobby Bolin
- away: CHN
  count: 4
  date: 1965-07-30
  home: PIT
  id: PIT196507300
  initial: eb
  lineup: Jimmy Stewart; Ellis Burton; Billy Williams; Ernie Banks; Ron Santo; Ed Bailey; Glenn Beckert; Don Kessinger; Ernie Broglio
- away: SDN
  count: 4
  date: 1990-09-26
  home: SFN
  id: SFN199009260
  initial: jc
  lineup: Bip Roberts; Joey Cora; Jack Clark; Joe Carter; Mike Pagliarulo; Jerald Clark; Mark Parent; Garry Templeton; Dennis Rasmussen
- away: CHA
  count: 4
  date: 1901-09-27
  home: WS1
  id: WS1190109270
  initial: bc
  lineup: Irv Waldron; John Farrell; Sam Dungan; Boileryard Clarke; Mike Grady; Bill Coughlin; Billy Clingman; Ben Harrison; Bill Carrick

---
<h3>Batting order initials</h3>

{% for row in page.data %}
<div>
  <b>{{row.initial | upcase}}: {{row.count}} players</b>
  <div><a href="https://www.baseball-reference.com/boxes/{{row.home}}/{{row.id}}.shtml">{{row.date}} {{row.away}} at {{row.home}}</a></div>
  <i>{{row.lineup}}</i>
  <div>&nbsp;</div>
</div>
{% endfor %}


<hr>

   <pre>
            last name

      abcdefghijklmnopqrstuvwxyz *
   a  22222222122221131321113.11 5
   b  2442122312222112.233123.11 6
   c  13221222122221121222112.11 6
   d  2232222212223213.231112.11 6
   e  24211212112221111221112.12 4
   f  12211212111221221122112.11 4
   g  22221222112221121222112.11 4
   h  13212123111231111221112.11 5
   i  11111111.1111111.111.11.1. 2
f  j  23432333122232331342132.11 8
i  k  1221112211122122.221112.1. 4
r  l  12221222.21221121221112.11 4
s  m  23222222112232221232113.11 6
t  n  11211111.1122111.111.11..1 3
   o  21111122111121111121.11..1 3
n  p  12222121111221121321.12.11 4
a  q  .1..........1.1....1.1.... 1
m  r  22221223122232221332112.11 6
e  s  2222112212222112.232112.11 5
   t  12221122122222231222112.11 5
   u  .......1.1.....1..1.1.1... 1
   v  11121111.1111111.111.11..1 3
   w  22211112.1112111.121112.1. 5
   x  11..1..1.....1.1.11....... 1
   y  11111121..1.21.1.111.11.1. 3
   z  11111.11.11111.1.111.11..1 2

   *  47664465244473351664335.22 .
</pre>
