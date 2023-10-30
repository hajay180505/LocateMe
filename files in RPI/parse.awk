#!/bin/awk -f
BEGIN{
	line = ""	
}
	
{
	gsub(/          /,"",$0);


	if(NR != 1 && (NR-1)%4==0){
	#print "LINE : " line "++";
		line = "";
	}

	if ((NR-1)%4==0){
	#print $0 " conv -> "
		line = line $5 
		#print $5;
	}
	else if((NR-1)%4 == 2){
		gsub(/level=/,"",$0);
		line = line ","$3
		#print $3;
	}
	else if((NR-1)%4 == 3){
		gsub(/ESSID:/,"",$0);
		#if($0 == "Genjutsu"){
		#	print $0;
		#	line = "";
		#	next;
		#}
		line = line "," $0
		#print $0;
	}
	if (NR!=0 && (NR-1)%4 == 3){
		#print "L : [" line "] @"
		print line;
	}
#print $0;
}

