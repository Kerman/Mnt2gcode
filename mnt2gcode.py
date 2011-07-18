#/opt/local/bin/python
import string;
import sys;
sys.stdout.softspace=0



f = open('Teensylu-0.7.mnt.mini', 'r');

##global config
#Z travel height
ZTRAVEL=0.5;
#Tape slot to start with
INDEX=1;

##Locations for first item on strip
#START=starting point of center of first item on tape
#Z=Z height for suction grabbing
#GAP=gap between part centers, assumes Y direction

C9START = [0.1,0.1];
C9Z = -0.5;
C9GAP = 0.025;
C10START= [0.2,0.2];
C10Z = -0.5;
C10GAP = 0.025;


def gcodeify(partname):
	mystart=str(partname)+"START";
	mygap=str(partname)+"GAP";
	mygap=eval(mygap);
	mystart=eval(mystart);
	myoutput="G1 X"+str(mystart[0])+" Y"+str(mystart[1]+(mygap*INDEX));
	
	return myoutput;
	
def toolhead(command):
	if command=="on":
		return "TOOLHEAD ON GCODE COMMAND HERE";
 	elif command=="off":
 		return "TOOLHEAD OFF GCODE COMMAND HERE";
 	else:
 		return "TOOLHEAD ROTATE COMMAND HERE";

##Offsets for empty strips

for line in f:
		lineitems = string.split(line);
	#go pick up a a part
		movecommand = gcodeify(lineitems[0]);
		print movecommand;
		movez=str(lineitems[0])+"Z";
		movez=eval(movez);
		print "G1 Z"+str(movez);
	#grab it
		toolheadcmd=toolhead("on");
		print toolheadcmd;
		print "G1 Z"+str(ZTRAVEL);
	#go to the location on the pcb
		print"G1 X"+str(lineitems[1])+" Y"+str(lineitems[2]);
	
	#rotate the part
		print"ROTATE PART "+lineitems[3]+" DEGREES COMMMAND HERE";
	
	#lower the part
		movez=str(lineitems[0])+"Z";
		movez=eval(movez);
		print "G1 Z"+str(movez);
	#drop the part
		toolheadcmd=toolhead("off");
		print toolheadcmd;
		print "G1 Z"+str(ZTRAVEL);
		
		print "DEBUG: ----------------";
		
		
		
		
		
		
		
	#if line[0] == 'C9':
	 	#print "line0:";
	 	
	 	#if lineitems[0] == 'C9':
	 		#Go to the location of the item C9
	
	 	 	#print "G1 X"+str(C9START[0])+" Y"+str(C9START[1]);
	 	
	#print line;

