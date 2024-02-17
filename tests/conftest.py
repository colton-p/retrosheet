# pylint: disable=line-too-long
import csv
import pytest

from retro.file_readers.game_logs import build_game_log_record
from retro.file_readers.events import build_event_record
from retro.file_readers.box_scores import build_box_record



@pytest.fixture
def game_log_record():
    line = '"20220930","0","Fri","BOS","AL",157,"TOR","AL",157,0,9,51,"N","","","","TOR02",37283,184,"000000000","11200401x",29,3,0,0,0,0,0,0,0,3,0,9,0,0,1,0,5,3,9,9,2,0,24,8,0,0,0,0,36,13,1,0,3,9,0,1,0,3,0,6,1,0,0,0,7,2,0,0,1,0,27,8,0,0,1,0,"fleta901","Andy Fletcher","hobep901","Pat Hoberg","bacce901","Erich Bacchus","eddid901","Doug Eddings","","(none)","","(none)","coraa001","Alex Cora","schnj801","John Schneider","manoa001","Alek Manoah","piven001","Nick Pivetta","kikuy001","Yusei Kikuchi","kirka001","Alejandro Kirk","piven001","Nick Pivetta","manoa001","Alek Manoah","duraj001","Jarren Duran",8,"dever001","Rafael Devers",5,"bogax001","Xander Bogaerts",6,"verda001","Alex Verdugo",9,"martj006","J.D. Martinez",10,"casat001","Triston Casas",3,"almoa001","Abraham Almonte",7,"mcgur002","Reese McGuire",2,"arroc001","Christian Arroyo",4,"sprig001","George Springer",8,"bichb001","Bo Bichette",6,"guerv002","Vladimir Guerrero",3,"kirka001","Alejandro Kirk",2,"chapm001","Matt Chapman",5,"hernt002","Teoscar Hernandez",9,"tapir001","Raimel Tapia",7,"jansd001","Danny Jansen",10,"merrw001","Whit Merrifield",4,"","Y"'

    (ret,) = list(csv.reader([line]))
    return build_game_log_record(ret)

@pytest.fixture
def game_log_record2():
    line = '"20220722","0","Fri","TOR","AL",94,"BOS","AL",94,28,5,54,"N","","","","BOS07",36796,229,"1274(11)2001","000301100",57,29,5,0,5,28,0,0,1,5,0,9,0,0,0,0,8,3,4,4,0,0,27,6,2,0,0,0,37,10,2,0,4,5,0,0,0,0,0,16,0,0,0,0,5,7,27,27,2,0,27,9,2,0,0,0,"eddid901","Doug Eddings","ortir901","Roberto Ortiz","millb901","Bill Miller","knigb901","Brian Knight","","(none)","","(none)","schnj801","John Schneider","coraa001","Alex Cora","gausk001","Kevin Gausman","eovan001","Nathan Eovaldi","","(none)","bichb001","Bo Bichette","gausk001","Kevin Gausman","eovan001","Nathan Eovaldi","tapir001","Raimel Tapia",8,"guerv002","Vladimir Guerrero",3,"kirka001","Alejandro Kirk",10,"bichb001","Bo Bichette",6,"hernt002","Teoscar Hernandez",9,"gurrl001","Lourdes Gurriel",7,"chapm001","Matt Chapman",5,"espis001","Santiago Espinal",4,"jansd001","Danny Jansen",2,"duraj001","Jarren Duran",8,"refsr001","Rob Refsnyder",10,"dever001","Rafael Devers",5,"bogax001","Xander Bogaerts",6,"verda001","Alex Verdugo",7,"vazqc001","Christian Vazquez",3,"plawk001","Kevin Plawecki",2,"bradj001","Jackie Bradley",9,"downj001","Jeter Downs",4,"","Y"'
    (ret,) = list(csv.reader([line]))
    return build_game_log_record(ret)

@pytest.fixture
def play_by_play_lines():
    events ="""id,TOR202209300
version,2
info,visteam,BOS
info,hometeam,TOR
info,site,TOR02
info,date,2022/09/30
info,number,0
info,starttime,7:07PM
info,daynight,night
info,innings,9
info,tiebreaker,2
info,usedh,true
info,umphome,fleta901
info,ump1b,hobep901
info,ump2b,bacce901
info,ump3b,eddid901
info,umplf,(none)
info,umprf,(none)
info,inputtime,2022/10/03 09:01:04
info,howscored,unknown
info,pitches,pitches
info,oscorer,starh701
info,temp,68
info,winddir,unknown
info,windspeed,0
info,fieldcond,unknown
info,precip,none
info,sky,dome
info,timeofgame,184
info,attendance,37283
info,wp,manoa001
info,lp,piven001
info,save,kikuy001
start,duraj001,"Jarren Duran",0,1,8
start,dever001,"Rafael Devers",0,2,5
start,bogax001,"Xander Bogaerts",0,3,6
start,verda001,"Alex Verdugo",0,4,9
start,martj006,"J.D. Martinez",0,5,10
start,casat001,"Triston Casas",0,6,3
start,almoa001,"Abraham Almonte",0,7,7
start,mcgur002,"Reese McGuire",0,8,2
start,arroc001,"Christian Arroyo",0,9,4
start,piven001,"Nick Pivetta",0,0,1
start,sprig001,"George Springer",1,1,8
start,bichb001,"Bo Bichette",1,2,6
start,guerv002,"Vladimir Guerrero",1,3,3
start,kirka001,"Alejandro Kirk",1,4,2
start,chapm001,"Matt Chapman",1,5,5
start,hernt002,"Teoscar Hernandez",1,6,9
start,tapir001,"Raimel Tapia",1,7,7
start,jansd001,"Danny Jansen",1,8,10
start,merrw001,"Whit Merrifield",1,9,4
start,manoa001,"Alek Manoah",1,0,1
play,1,0,duraj001,11,BCX,43/G4D
play,1,0,dever001,32,BBBFTB,W
play,1,0,bogax001,22,BCFFFB*S,K
play,1,0,verda001,22,FBBSX,8/L78
play,1,1,sprig001,00,X,S8/L8D+
play,1,1,bichb001,10,BX,S7/L7+.1-2
play,1,1,guerv002,22,BSBFFX,9/F89S
play,1,1,kirka001,00,B,WP.2-3
play,1,1,kirka001,11,B.CX,43/G34.3-H;1-2
play,1,1,chapm001,32,FBBC*BX,9/F9D
play,2,0,martj006,11,BSX,9/F9D
play,2,0,casat001,12,CBSS,K
play,2,0,almoa001,32,BCBBFX,5/P6S
play,2,1,hernt002,32,SBBSBX,S8/L8D
play,2,1,tapir001,12,CB*S>FFX,65(1)/FO/G4.B-1
play,2,1,jansd001,32,B1CBBS>B,W.1-2
play,2,1,merrw001,01,FB,WP.2-3;1-2
play,2,1,merrw001,21,FB.BX,9/SF/F89D.3-H;2-3
play,2,1,sprig001,00,X,9/F9L
play,3,0,mcgur002,32,BBCBCC,K
play,3,0,arroc001,12,BFFX,7/L78D
play,3,0,duraj001,22,FFFBBX,13/G4MS
play,3,1,bichb001,32,FFBBBFFFB,W
play,3,1,guerv002,01,FX,HR/L7D.1-H
play,3,1,kirka001,32,BBCBCB,W
play,3,1,chapm001,32,.FBSB*BS,K
play,3,1,hernt002,12,SFBX,54(1)/FO/G56S.B-1
play,3,1,tapir001,02,SFX,3/L3
play,4,0,dever001,32,CFBBFBB,W
play,4,0,bogax001,02,FSX,9/F89S
play,4,0,verda001,00,B,WP.1-2
play,4,0,verda001,22,B.SBCX,7/F78D
play,4,0,martj006,12,BCFX,43/G34
play,4,1,jansd001,12,BSSS,K
play,4,1,merrw001,11,BFX,S7/L78D+
play,4,1,sprig001,00,X,46(1)/FO/G4.B-1
play,4,1,bichb001,12,FBTF>B,SB2
play,4,1,bichb001,32,FBTF>B.FBFFX,8/F8XD
play,5,0,casat001,22,CBBFC,K
play,5,0,almoa001,10,BX,S3/G3
play,5,0,mcgur002,22,BBCFX,8/F8D
play,5,0,arroc001,01,FX,6/P6D
play,5,1,guerv002,01,CX,7/L7D
play,5,1,kirka001,11,SBX,S49/L34
play,5,1,chapm001,21,SB*BX,8/L8XD
play,5,1,hernt002,10,BX,9/F9LSF/FL
play,6,0,duraj001,31,BBCBX,S9/F89
play,6,0,dever001,22,FBBCX,45(1)3/GDP/G34
play,6,0,bogax001,02,CCX,43/G34
play,6,1,tapir001,00,,NP
sub,danit001,"Tyler Danish",0,0,1
play,6,1,tapir001,02,.CSX,HR/F9LD
play,6,1,jansd001,11,BCX,S8/L8D
play,6,1,merrw001,00,X,S7/G6+.1-2
play,6,1,sprig001,20,.BBX,HR/F78XD.2-H;1-H
play,6,1,bichb001,02,FSS,K
play,6,1,guerv002,22,CBFBC,K
play,6,1,kirka001,12,FCBX,13/G1S
play,7,0,verda001,00,,NP
sub,kikuy001,"Yusei Kikuchi",1,0,1
play,7,0,verda001,01,.SX,43/G34
play,7,0,martj006,22,BTSFBS,K
play,7,0,casat001,31,BBBCB,W
play,7,0,almoa001,32,SBCF*B*B>S,K
play,7,1,chapm001,12,CFBC,K
play,7,1,hernt002,32,BBBCFX,63/G6D
play,7,1,tapir001,11,BCX,S8/G4
play,7,1,jansd001,00,X,43/G13-
play,8,0,mcgur002,02,SFFX,S4/G4
play,8,0,arroc001,02,FSFS,K
play,8,0,duraj001,02,CCX,63/G6S.1-2
play,8,0,dever001,00,,NP
sub,dalbb001,"Bobby Dalbec",0,2,11
play,8,0,dalbb001,02,.SSS,K
play,8,1,merrw001,00,,NP
sub,dalbb001,"Bobby Dalbec",0,2,5
play,8,1,merrw001,00,.,NP
sub,chany001,"Yu Chang",0,3,6
play,8,1,merrw001,00,..,NP
sub,germf002,"Franklin German",0,0,1
play,8,1,merrw001,01,...FX,DGR/L9LD
play,8,1,sprig001,00,,NP
sub,zimmb001,"Bradley Zimmer",1,1,11
play,8,1,zimmb001,12,.BSFC,K
play,8,1,bichb001,00,X,S9/G3.2-H
play,8,1,guerv002,00,X,54(1)/FO/G56.B-1
play,8,1,kirka001,10,BX,4/L4
play,9,0,chany001,00,,NP
sub,zimmb001,"Bradley Zimmer",1,1,8
play,9,0,chany001,00,.,NP
sub,lopeo001,"Otto Lopez",1,2,6
play,9,0,chany001,02,..SSS,K
play,9,0,verda001,01,CX,8/L8D+
play,9,0,martj006,22,BCFBFX,8/L8D+
data,er,danit001,4
data,er,germf002,1
data,er,piven001,4
data,er,manoa001,0
data,er,kikuy001,0"""

    lines = list(csv.reader(events.split("\n")))

    records = [build_event_record(row) for row in lines]
    return [rec for rec in records if rec]

@pytest.fixture
def box_score_lines():
    box="""id,CHN195505140
version,3
info,visteam,NY1
info,hometeam,CHN
info,site,CHI11
info,date,1955/05/14
info,number,0
info,starttime,0:00
info,daynight,day
info,usedh,false
info,umphome,boggd901
info,ump1b,gormt101
info,ump2b,engeb902
info,ump3b,pineb101
info,pitches,none
info,temp,0
info,winddir,unknown
info,windspeed,-1
info,fieldcond,unknown
info,precip,unknown
info,sky,unknown
info,timeofgame,152
info,attendance,17818
info,wp,rushb101
info,lp,antoj103
info,save,
start,willd102,"Davey Williams",0,1,4
start,darka101,"Al Dark",0,2,6
start,mueld101,"Don Mueller",0,3,9
start,irvim101,"Monte Irvin",0,4,7
start,maysw101,"Willie Mays",0,5,8
start,thomh103,"Hank Thompson",0,6,5
start,lockw101,"Whitey Lockman",0,7,3
start,kattr101,"Ray Katt",0,8,2
start,antoj103,"Johnny Antonelli",0,9,1
start,mikse101,"Eddie Miksis",1,1,9
start,bakeg101,"Gene Baker",1,2,4
start,jackr102,"Randy Jackson",1,3,5
start,saueh101,"Hank Sauer",1,4,7
start,banke101,"Ernie Banks",1,5,6
start,fondd101,"Dee Fondy",1,6,3
start,chith101,"Harry Chiti",1,7,2
start,bolgj101,"Jim Bolger",1,8,8
start,rushb101,"Bob Rush",1,9,1
stat,bline,willd102,0,1,1,4,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0
stat,bline,darka101,0,2,1,4,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
stat,bline,mueld101,0,3,1,4,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
stat,bline,irvim101,0,4,1,3,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0
stat,bline,maysw101,0,5,1,4,0,0,0,0,0,0,0,0,0,0,0,2,0,0,1,0
stat,bline,thomh103,0,6,1,3,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0
stat,bline,lockw101,0,7,1,3,0,2,0,0,0,0,0,0,0,0,0,0,0,1,1,0
stat,bline,kattr101,0,8,1,3,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
stat,bline,antoj103,0,9,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
stat,bline,grism101,0,9,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
stat,bline,rhodd101,0,9,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
stat,bline,wilhh101,0,9,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
stat,bline,mikse101,1,1,1,3,0,1,0,0,0,2,0,0,0,1,0,0,0,0,0,0
stat,bline,bakeg101,1,2,1,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0
stat,bline,jackr102,1,3,1,4,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0
stat,bline,saueh101,1,4,1,3,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0
stat,bline,kingj101,1,4,2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
stat,bline,banke101,1,5,1,2,2,0,0,0,0,0,0,0,0,2,0,1,0,0,0,0
stat,bline,fondd101,1,6,1,4,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0
stat,bline,chith101,1,7,1,2,1,1,0,0,0,1,0,0,0,2,0,1,0,0,0,0
stat,bline,bolgj101,1,8,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0
stat,bline,tappt101,1,8,2,2,1,1,0,0,0,2,0,0,1,0,0,0,0,0,0,0
stat,bline,rushb101,1,9,1,3,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0
stat,phline,rhodd101,8,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
stat,phline,tappt101,5,1,1,1,1,0,0,0,2,0,0,0,0,0,0,0,0,0,0
stat,prline,kingj101,8,1,1,0,0
stat,dline,antoj103,0,1,1,12,1,2,1,0,0,0
stat,dline,grism101,0,1,1,9,0,0,0,0,0,0
stat,dline,wilhh101,0,1,1,3,0,0,0,0,0,0
stat,dline,kattr101,0,1,2,24,5,1,0,0,0,0
stat,dline,lockw101,0,1,3,24,12,1,0,1,0,0
stat,dline,thomh103,0,1,5,24,1,3,0,0,0,0
stat,dline,maysw101,0,1,8,24,0,1,0,0,0,0
stat,dline,irvim101,0,1,7,24,1,0,0,0,0,0
stat,dline,mueld101,0,1,9,24,1,0,0,0,0,0
stat,dline,darka101,0,1,6,24,0,6,2,1,0,0
stat,dline,willd102,0,1,4,24,3,1,0,1,0,0
stat,dline,rushb101,1,1,1,27,2,3,0,1,0,0
stat,dline,bolgj101,1,1,8,15,1,0,0,0,0,0
stat,dline,tappt101,1,1,9,12,1,0,0,0,0,0
stat,dline,chith101,1,1,2,27,2,1,0,0,0,0
stat,dline,fondd101,1,1,3,27,12,2,0,3,0,0
stat,dline,banke101,1,1,6,27,3,5,1,3,0,0
stat,dline,saueh101,1,1,7,24,0,0,0,0,0,0
stat,dline,kingj101,1,1,7,3,1,0,0,0,0,0
stat,dline,jackr102,1,1,5,27,0,2,0,0,0,0
stat,dline,bakeg101,1,1,4,27,5,5,0,1,0,0
stat,dline,mikse101,1,1,9,15,0,0,0,0,0,0
stat,dline,mikse101,1,2,8,12,0,0,0,0,0,0
stat,pline,antoj103,0,1,12,0,16,1,-1,-1,0,3,2,2,0,2,0,0,0,0,0
stat,pline,grism101,0,2,9,0,13,4,-1,-1,0,3,2,1,0,1,1,0,0,1,0
stat,pline,wilhh101,0,3,3,0,7,0,-1,-1,0,2,0,3,0,2,0,0,0,0,0
stat,pline,rushb101,1,1,27,0,33,7,-1,-1,0,0,0,2,0,2,0,0,0,0,0
line,0,0,0,0,0,0,0,0,0,0
line,1,0,0,0,0,3,1,2,2
stat,tline,0,6,4,1,0
stat,tline,1,4,0,3,0
event,dpline,0,darka101,willd102,lockw101
event,dpline,1,banke101,bakeg101,fondd101
event,dpline,1,banke101,fondd101
event,dpline,1,rushb101,banke101,fondd101
event,hpline,0,grism101,tappt101
event,csline,0,lockw101,,,-1
event,csline,1,fondd101,,,-1"""

    lines = list(csv.reader(box.split("\n")))
    records = [build_box_record(row) for row in lines]
    return [rec for rec in records if rec]
