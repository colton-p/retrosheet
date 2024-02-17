---
layout: default
title: alphabetical batting orders
data:
- order: (1, 2, 3, 4, 5, 6, 7, 8, 9)
  count: 13
  date: 1934-05-12
  home: Cincinnati Reds
  away: Boston Braves
  id: CIN/CIN193405120
  lineup: Sparky Adams; Linc Blakely; Jim Bottomley; Chick Hafey; Mark Koenig; Johnny Moore; Bob O'Farrell; Gordon Slade; Allyn Stout
- order: (1, 2, 3, 4, 5, 6, 7, 9, 8)
  count: 1
  date: 1911-09-25
  home: Philadelphia Athletics
  away: Detroit Tigers
  id: PHA/PHA191109250
  lineup: Donie Bush; Ty Cobb; Sam Crawford; Jim Delahanty; Delos Drake; Del Gainer; George Moriarty; Oscar Stanage; George Mullin
- order: (1, 2, 3, 4, 5, 7, 6, 8, 9)
  count: 1
  date: 2023-09-15
  home: Miami Marlins
  away: Atlanta Braves
  id: MIA/MIA202309150
  lineup: Luis Arraez; Josh Bell; Jake Burger; Jazz Chisholm; Bryan De La Cruz; Jesus Sanchez; Xavier Edwards; Jacob Stallings; Joey Wendle
- order: (1, 2, 3, 4, 6, 5, 7, 8, 9)
  count: 1
  date: 1964-08-04
  home: Kansas City Athletics
  away: New York Yankees
  id: KC1/KC1196408040
  lineup: Bert Campaneris; Wayne Causey; Ed Charles; Rocky Colavito; Jim Gentile; Doc Edwards; Manny Jimenez; Nelson Mathews; John O'Donoghue
- order: (2, 1, 3, 4, 5, 6, 7, 8, 9)
  count: 1
  date: 2010-04-19
  home: New York Mets
  away: Chicago Cubs
  id: NYN/NYN201004190
  lineup: Marlon Byrd; Jeff Baker; Derrek Lee; Xavier Nady; Aramis Ramirez; Alfonso Soriano; Geovany Soto; Ryan Theriot; Randy Wells
---

A team's batting order has been in alphabetical order 13 times. Most recently by the 1934 Reds; and 12 times in September 1911 by the Detroit Tigers.

There have been four near-misses with one player out-of-order, most recently by the 2023 Marlins.

{% for row in page.data %}
<div>
  <b>{{row.order}}: {{row.count}} games</b>
  <div><a href="https://www.baseball-reference.com/boxes/{{row.id}}.shtml">{{row.date}}</a>: {{row.away}} at {{row.home}}</div>
  <i>{{row.lineup}}</i>
  <div>&nbsp;</div>
</div>
{% endfor %}