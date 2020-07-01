#from tkinter import *
import tkinter as tk
import math
from math import sin, cos, radians 
import numpy as np
from skimage.draw import polygon as gy
from PIL import Image
from shapely.geometry import Point, Polygon

######################################

HF=64   #64
FW=HF*2


totalbitmap=np.zeros((FW, FW))

visited=np.zeros((FW, FW, 360), dtype=bool)

#record=np.zeros((FW, FW))


POPO=[]


twice=np.zeros((FW, FW, 360))
#for i in range(0,record.shape[0]):
#	for j in range(0,record.shape[1]):
#		record[i][j]=-1



#########################################

class robotlist:
	def __init__(self,):
		self.robotL=[]
		self.robotnums=0

	def setrobotnums(self,robotamount):
		self.robotnums=robotamount    #set number of robots

	def insertrobots(self,newrobot):   #insert newly created robots
		self.robotL.append(newrobot)

	def getrobotList(self,):
		return self.robotL

	def getrobotListNUM(self,):
		return self.robotnums

############################################3

class robotS:
	def __init__(self,):
		self.robotpolys=[]
		self.configureR=[]
		self.polynumR=0
		self.goal=[]
		self.controlnum=0
		self.controlPs=[]
	
	def setrobotpolys(self,ps):       #set polygons of the robot
		self.robotpolys.append(ps)
	
	def setconfigureR(self,conR):  #set initial configuration (x,y,angle)
		self.configureR=conR
	
	def setpolynumR(self,nummR):	#set number of polygons of an robot
		self.polynumR=nummR

	def getpolynumR(self,):
		return self.polynumR

	def getrobotpoly(self,Rth):
		return self.robotpolys[Rth]

	def getconfigureR(self,):
		return self.configureR

	def setgoal(self,sg):
		self.goal=sg

	def getgoal(self,):
		return self.goal

	def setcontrolnum(self,cn):
		self.controlnum=cn

	def getcontrolnum(self,):
		return self.controlnum

	def addcontrolP(self,cc):
		self.controlPs.append(cc)

	def getcontrolPs(self,):
		return self.controlPs





###########################################
class obstaclelist:
	def __init__(self,):
		self.obsL=[]
		self.obsnums=0

	def setobnums(self,obamount):
		self.obsnums=obamount    #set number of obstacles

	def insertobs(self,newob):   #insert newly created obstacles
		self.obsL.append(newob)

	def getobsList(self,):
		return self.obsL

	def getobsListNUM(self,):
		return self.obsnums

class obstacleS:
	def __init__(self,):
		self.obs=[]
		self.configure=[]
		self.polynum=0
	
	def setobs(self,obS):       #set polygons of the obstacle
		self.obs.append(obS)
	
	def setconfigure(self,con):  #set initial configuration (x,y,angle)
		self.configure=con
	
	def setpolynum(self,numm):	#set number of polygons of an obstacle
		self.polynum=numm

	def getpolynum(self,):
		return self.polynum

	def getpoly(self,pth):
		return self.obs[pth]

	def getconfigure(self,):
		return self.configure

class polygon:
	def __init__(self,):
		self.vertex=[]
		self.numvertex=0
	def setpoly(self,v):           #set vertexes of the polygon
		self.vertex=v
	
	def setvertexnum(self,numv):   #set number of vertex of a polygon
		self.numvertex=numv

	def getpolyvertex(self,):
		return self.vertex

	def getpolynum(self,):
		return self.numvertex


####################################################################


class Item():

	def __init__(self, canvas, items):

		self.previous_x = None
		self.previous_y = None
		self.selected = None

		self.items = items

		self.Canvas=canvas

		for item in self.items:
			self.Canvas.tag_bind(item, '<ButtonPress-1>',   lambda event, tag=item: self.on_press_tag(event, tag, self.items))
			self.Canvas.tag_bind(item, '<ButtonRelease-1>', lambda event, tag=item: self.on_release_tag(event, tag, self.items))
			self.Canvas.tag_bind(item, '<B1-Motion>', self.on_move_tag)
			

	def on_press_tag(self, event, tag, itemm2):
		self.selected = True
		self.previous_x = event.x
		self.previous_y = event.y

		global totalbitmap

		print('press:', event, tag)

		
		for i in itemm2:
			COO2=self.Canvas.coords(i)

			r2=[]
			c2=[]
			img2 = np.zeros((FW, FW))

			count=0

			for itr in range(0,len(COO2)):
				if (count%2)==0:
					c2.append(int(COO2[itr]))
				else:
					r2.append(int(COO2[itr]))

				count=count+1
						
			R2=np.array(r2) 
			C2=np.array(c2)
				
			rr2, cc2 = gy(R2, C2)
			img2[rr2, cc2] = -1

			totalbitmap=totalbitmap+img2







		#############################################
		#for i in itemm2:
		#	coor=self.Canvas.coords(i)
		#	count=0

		#	up=FW-1
		#	down=0

		#	left=FW-1
		#	right=0

		#	for k in range(0,len(coor)):
		#		if (count%2)==0:
		#			com=coor[k]
		#			if com<left:
		#				left=com
		#			if com>right:
		#				right=com
		#		else:
		#			com=coor[k]
		#			if com<up:
		#				up=com
		#			if com>down:
		#				down=com

		#		count=count+1

		#	up=int(up)
		#	down=int(down)
		#	left=int(left)
		#	right=int(right)

		#	for m in range(up,(down+1)):
		#		for p in range(left,(right+1)):
		#			totalbitmap[m][p]=0

		#######################################################




	def on_release_tag(self, event, tag, itemm):
		self.selected = False
		self.previous_x = None
		self.previous_y = None

		global totalbitmap

		print('release:', event)


		for i in itemm:
			COO=self.Canvas.coords(i)



			r=[]
			c=[]
			img = np.zeros((FW, FW))

			count=0

			for itr in range(0,len(COO)):
				if (count%2)==0:
					c.append(int(COO[itr]))
				else:
					r.append(int(COO[itr]))

				count=count+1
						
			R=np.array(r) 
			C=np.array(c)
				
			rr, cc = gy(R, C)
			img[rr, cc] = 1

			totalbitmap=totalbitmap+img

		#check=0
		#for i in range(0,totalbitmap.shape[0]):
		#	for j in range(0,totalbitmap.shape[1]):
		#		if totalbitmap[i][j]==-1:
		#			check=check+1

		#print(check)	

		

	def on_move_tag(self, event):
		#print(event.x, event.x)
		if self.selected:
			dx = event.x - self.previous_x
			dy = event.y - self.previous_y

			for item in self.items:
				self.Canvas.move(item, dx, dy)
			self.previous_x = event.x
			self.previous_y = event.y
	

	


##########################################################################

class project:
	def __init__(self,obsta,robota):
		##self.root=Tk()
		#self.link=None
		#self.layer=None
		#self.frames =[]
		#self.widgets =[]
		#self.numPoly=0
		#self.store=[]

		self.halfwindow=HF
		self.fullwindow=FW

		self.root = tk.Tk()
		
		self.OB=obsta
		self.RO=robota

		self.iniset=[]
		self.robotini=[]


		self.canvas=tk.Canvas(self.root,width=self.fullwindow,height=self.fullwindow,background='white',relief='raised',borderwidth=1)
		self.canvas.grid(row=0,column=0)
		self.root.title("potential field")
		#self.canvas.config(scrollregion=self.canvas.bbox(ALL))
		self.canvas.pack()


		self.inicontrolL=[]
		

	def RUN(self):
		
		
		global totalbitmap

		self.inisetting()
		self.robotsetting()


		#######################################################################
		OBNUM=self.OB.getobsListNUM()


		for adjobth in range(0,OBNUM):
			adjob=self.iniset[adjobth]

			itemm=[]
			for expoly in adjob:
				addpoly=self.canvas.create_polygon(expoly , fill="blue")
				itemm.append(addpoly)



				r=[]
				c=[]
				img = np.zeros((FW, FW))

				count=0

				for itr in range(0,len(expoly)):
					if (count%2)==0:
						c.append(int(expoly[itr]))
					else:
						r.append(int(expoly[itr]))

					count=count+1
						
				R=np.array(r) 
				C=np.array(c)
				
				rr, cc = gy(R, C)
				img[rr, cc] = 1

				totalbitmap=totalbitmap+img


			Item(self.canvas,itemm)

		#############################################################3
		
		ggr=self.RO.getrobotList()
		ggrr=ggr[0]
		ggdes=ggrr.getgoal()

		ggg1=ggdes[0]    
		ggg2=ggdes[1]

		leftcorner=[]
		leftcorner.append((ggg1-1))
		leftcorner.append((ggg2-1))

		rightcorner=[]
		rightcorner.append((ggg1+1))
		rightcorner.append((ggg2+1))

		LL=self.world_2_canvas(leftcorner)
		RR=self.world_2_canvas(rightcorner)

		self.canvas.create_oval((LL[0]),(LL[1]),(RR[0]),(RR[1]), fill='#fff')







		#####################################################################

		RONUM=self.RO.getrobotListNUM()
		roos=self.RO.getrobotList()


		#################################################################

		for adjrothR in range(0,RONUM):
			adjroR=self.robotini[adjrothR]

			contin=self.inicontrolL[adjrothR]

			confff=roos[adjrothR].getconfigureR()
			#roo=roos[adjrothR]    ##
			#roog=roo.getgoal()    ##


			itemmR=[]
			for expolyR in adjroR:
				addpolyR=self.canvas.create_polygon(expolyR , fill="red")
				itemmR.append(addpolyR)


			ItemR(self.canvas,itemmR,contin,confff)    ##, roog
		
		#########################################################

		FR= tk.Frame(self.root).pack(side = "bottom")
		#btn1 = tk.Button(FR, text = "Potential", fg = "Red",command=lambda:self.constructpotential(GO)).pack(side = "left")
		btn2 = tk.Button(FR, text = "Build", fg = "Red",command=self.constructpotential).pack(side = "left")
		#btn3 = tk.Button(FR, text = "Robot", fg = "Blue",command=self.add_robot).pack(side = "left")
		##



		###################################################################
		self.root.mainloop()



	def constructpotential(self,):

		global POPO
		global totalbitmap


		POPO=[]


		RONUMm=self.RO.getrobotListNUM()
		roosm=self.RO.getrobotList()

		for adjrothR in range(0,RONUMm):
			roo1=roosm[adjrothR]
			des=roo1.getgoal()

			g1=des[0]    
			g2=des[1]

			g1=g1    ##g1+HF
			g2=FW-g2 ##HF-g2

			g1=int(g1)
			g2=int(g2)

			goall=[]

			goall.append(g1)
			goall.append(g2)

			potentialmap=np.zeros((FW,FW))

			for i in range(0, potentialmap.shape[0]):
				for j in range(0, potentialmap.shape[1]):

					if totalbitmap[i][j]!=0:
						potentialmap[i][j]=255
					else:
						ydiff=abs((i-goall[1]))
						xdiff=abs((j-goall[0]))

						step=ydiff+xdiff
						potentialmap[i][j]=int(step)
		
			POPO.append(potentialmap)

		
		for i in range(0,len(POPO)):
			mapp=POPO[i]
			img = Image.fromarray(mapp)
			img.show()







	def robotsetting(self,):

		finalsettingR=[]

		ROL=self.RO.getrobotList()

		for i in range(0,len(ROL)):

			roth=ROL[i]
			rothPolynum=roth.getpolynumR()
			rothConfi=roth.getconfigureR()

			ctrL=roth.getcontrolPs()

			rothtransx=rothConfi[0]
			rothtransy=rothConfi[1]
			rothangle=rothConfi[2]

			centroidxR=0
			centroidyR=0

			totalvertexamountR=0
			
			for j in range(0,rothPolynum):
				polythR=roth.getrobotpoly(j)
				vvR=polythR.getpolyvertex()

				vvamountR=polythR.getpolynum()
				totalvertexamountR=totalvertexamountR+vvamountR

				for k in range(0,vvamountR):
					ppR=vvR[k]
					xxR=ppR[0]
					yyR=ppR[1]

					centroidxR=centroidxR+xxR
					centroidyR=centroidyR+yyR


			centroidxR=centroidxR/totalvertexamountR
			centroidyR=centroidyR/totalvertexamountR
			
			ROSafterRotNTrans=[]

			centerR=[centroidxR,centroidyR]

			ccr=[]
			ccr=self.rotate_polygon(ctrL, rothangle, centerR)

			ccrx=[]

			for exe in range(0,len(ccr)):
				cp=ccr[exe]
				cpx=cp[0]
				cpy=cp[1]

				cpx=cpx+rothtransx
				cpy=cpy+rothtransy

				cpx=int(float(cpx))
				cpy=int(float(cpy))

				cpf=[]
				cpf.append(cpx)
				cpf.append(cpy)

				CPF=self.world_2_canvas(cpf)

				ccrx.append(CPF)

			self.inicontrolL.append(ccrx)







			for m in range(0,rothPolynum):
				polyth1R=roth.getrobotpoly(m)
				vv1R=polyth1R.getpolyvertex()

				RRr=self.rotate_polygon(vv1R, rothangle, centerR)
				



				




				roafterRotNTrans=[]

				for seg in range(0,len(RRr)):
					tempR=[]
					poiR=RRr[seg]
					tempxR=poiR[0]+rothtransx
					tempyR=poiR[1]+rothtransy

					tempR.append(tempxR)
					tempR.append(tempyR)

					finR=self.world_2_canvas(tempR)
					
					roafterRotNTrans.append(finR[0])
					roafterRotNTrans.append(finR[1])

				finROafterRotNTrans=tuple(roafterRotNTrans)

				ROSafterRotNTrans.append(finROafterRotNTrans)

			
				
			finalsettingR.append(ROSafterRotNTrans)

		self.robotini=finalsettingR
















	#def constructpotential(self,):
	#	global totalbitmap
	#	global potential
		
	#	ori=[HF,HF]


	#	for i in range(0,totalbitmap.shape[0]):
	#		for j in range(0,totalbitmap.shape[1]):
	#			rowdif=abs((i-ori[0]))
	#			coldif=abs((j-ori[1]))

	#			step=rowdif+coldif
	#			potential[i][j]=step

		

	
	def inisetting(self,):

		finalsetting=[]

		OBL=self.OB.getobsList()

		for i in range(0,len(OBL)):

			obth=OBL[i]
			obthPolynum=obth.getpolynum()
			obthConfi=obth.getconfigure()

			obthtransx=obthConfi[0]
			obthtransy=obthConfi[1]
			obthangle=obthConfi[2]

			centroidx=0
			centroidy=0

			totalvertexamount=0
			
			for j in range(0,obthPolynum):
				polyth=obth.getpoly(j)
				vv=polyth.getpolyvertex()

				vvamount=polyth.getpolynum()
				totalvertexamount=totalvertexamount+vvamount

				for k in range(0,vvamount):
					pp=vv[k]
					xx=pp[0]
					yy=pp[1]

					centroidx=centroidx+xx
					centroidy=centroidy+yy


			centroidx=centroidx/totalvertexamount
			centroidy=centroidy/totalvertexamount
			
			OBSafterRotNTrans=[]

			center=[centroidx,centroidy]

			for m in range(0,obthPolynum):
				polyth1=obth.getpoly(m)
				vv1=polyth1.getpolyvertex()

				RR=self.rotate_polygon(vv1, obthangle, center)
				
				PolyafterRotNTrans=[]

				for seg in range(0,len(RR)):
					temp=[]
					poi=RR[seg]
					tempx=poi[0]+obthtransx
					tempy=poi[1]+obthtransy

					temp.append(tempx)
					temp.append(tempy)

					fin=self.world_2_canvas(temp)
					
					PolyafterRotNTrans.append(fin[0])
					PolyafterRotNTrans.append(fin[1])

				finPolyafterRotNTrans=tuple(PolyafterRotNTrans)

				OBSafterRotNTrans.append(finPolyafterRotNTrans)

			
				
			finalsetting.append(OBSafterRotNTrans)

		self.iniset=finalsetting





	def world_2_canvas(self,world):
		#canvas x=world x+300
		#canvas y=300-world y

		can=[]

		tr=0
		count=0
		for num in world:
			check=count%2
			if check==0:
				tr=num
				#tr=num+self.halfwindow
			else:
				tr=self.fullwindow-num
				#tr=self.halfwindow-num

			can.append(tr)
			count=count+1

		return can

	
	



	def rotate_point(self, point, angle, center_point):
		"""Rotates a point around center_point(origin by default)
		Angle is in degrees.
		Rotation is counter-clockwise
		"""
		angle_rad = radians(angle % 360)
		# Shift the point so that center_point becomes the origin
		vec = (point[0] - center_point[0], point[1] - center_point[1])
		new_point = (vec[0] * cos(angle_rad) - vec[1] * sin(angle_rad),
		vec[0] * sin(angle_rad) + vec[1] * cos(angle_rad))
		# Reverse the shifting we have done
		fnew_point = (new_point[0] + center_point[0], new_point[1] + center_point[1])
		
		ffnew_point=list(fnew_point)

		return ffnew_point



	def rotate_polygon(self, polygon, angle, center_point): 
		"""Rotates the given polygon which consists of corners represented as (x,y)
		around center_point (origin by default)
		Rotation is counter-clockwise
		Angle is in degrees
		"""
		rotated_polygon = []
		for corner in polygon:
			rotated_corner = self.rotate_point(corner, angle, center_point)

			rotated_polygon.append(rotated_corner)
	
		return rotated_polygon



	#####################################################################
	#def numObstacle(self):
	#	newWindow = Toplevel(self.root)
	#	self.layer=newWindow
	#	QO = Label(newWindow, text = "Number of Obstacles?")
	#	numOe=Entry(newWindow,width=35,borderwidth=5)
	#	self.link=numOe

	#	ok =Button(newWindow, text = "OK",command=self.createPoly)
	#	cancel = Button(newWindow, text = "cancel",command=newWindow.destroy)
	#	QO.pack()
	#	numOe.pack()
	#	ok.pack(side="left")
	#	cancel.pack(side="left")
	###############################################################



	#############################################################
	#def createPoly(self):
	#	polyWindow = Toplevel(self.layer)
	#	PO = Label(polyWindow, text = "Please type in vertices of each polygon")
	#	PO.pack(side="top")

	#	self.numPoly=int(self.link.get())

		
	#	frame = Frame(polyWindow, borderwidth=2, relief="groove")
	#	self.frames.append(frame)
	#	frame.pack(fill="x")
	#	for i in range(0,self.numPoly):
	#		widget = Entry(frame)
	#		self.widgets.append(widget)
	#		widget.pack()


	#	ok1 = Button(polyWindow, text = "OK",command=self.getvertex)
	#	cancel1 = Button(polyWindow, text = "cancel",command=polyWindow.destroy)
	#	ok1.pack(side="left")
	#	cancel1.pack(side="left")
	##################################################################



	#################################################
	#def getvertex(self):
	#	for i in range(0,self.numPoly):
	#		tempo=self.widgets[i]
	#		sub=tempo.get()
	#		sep=sub.split(",")
	#		res = [int(k) for k in sep] 
	#		can_cor=self.world_2_canvas(res)
	#		self.store.append(can_cor)			
	#################################################


	#################################################
	#def add_polygon(self):
	#	for i in range(0,len(self.store)):
	#		ret=self.store[i]
	#		self.canvas.create_polygon(ret,fill="red")
	###################################################


	

def READOBS(file):
	f1=open(file, "r")

	###############################################
	#ready for number of obstacles input 
	oblistwarn=False

	#number of obstacles
	numOB=0

	##############################################

	#show if ready to input obstacle information
	obsepwarn=False  

	##############################################
	#ready for input number of polygons of an obstacles
	polywarn=False

	#input number of polygons of an obstacle
	polynum=0 

	################################
	#ready for input info of polygons
	poowarn=False  

	#ready for input of vertex numbers of a polygon
	vnumwarn=False 

	#vertex number of a polygon
	vertexnum=0

	################################
	#ready to input vertex info
	vertexstart=False

	#judge if the input of vertex is finished
	vertexcount=0
	##################################
	#start of input of configuration
	confiwarn=False   

	###################################



	for i in f1:
		line=i.strip()

		##Part1
		#########################
		if line=='#number of obstacle':        ##--#number of obstacles
			OB=obstaclelist()      #store newly created obstacles
			oblistwarn=True
		############################

		if line!='#number of obstacle' and oblistwarn==True:       ##--#number of obstacles
			numOB=int(line)
			OB.setobnums(numOB)    #set number of obstacles
			oblistwarn=False
		###############################
		##

		##Part2
		###################################
		if '# obstacle ' in line:                  ##--# obstacle #
			obsepwarn=True   # ready to input obstacle information
			newobs=obstacleS()
		#################################
		##


		##Part3
		####################################
		if '# number of convex part' in line:            ##--# number of polygons
			polywarn=True   #for input number of polygons of an obstacle


		if line !='# number of convex part' and polywarn==True:      ##--# number of polygons
			polynum=int(line)			#input number of polygons of an obstacle
			polywarn=False
			newobs.setpolynum(polynum)	#set number of polygons of an obstacle


		#######################################
		##



		##Part4
		############################################
		if '# convex part #' in line:     ##--# polygon #
			poowarn=True   #ready for input info of polygons
			newpoly=polygon()

		if line == '# number of vertices' and poowarn==True:       ##--# number of vertices
			poowarn=False
			vnumwarn=True   #ready for input of vertex numbers of a polygon

		if line !='# number of vertices' and vnumwarn==True:       ##--# number of vertices
			vertexnum=int(line)    #vertex numbers of a polygon
			newpoly.setvertexnum(vertexnum)   #set vertex number of a polygon
			vnumwarn=False

		#################################################
		##


		##Part5
		#######################################################
		if line=='# vertices':     ##--# vertices
			vertexstart=True   #ready to input vertex info
			vertexcount=0      #judge if the input of vertex is finished
			vv=[]

		if (line!='# vertices') and vertexstart==True and vertexcount<vertexnum:     ##--# vertices
			point=[]
			wala=line.split(" ")
			point=[float(k) for k in wala]
			vv.append(point)

			vertexcount=vertexcount+1


		if vertexstart==True and (vertexcount>=vertexnum):
			newpoly.setpoly(vv) #set vertexes of the polygon
			newobs.setobs(newpoly)  #set polygons of the obstacle
			vertexstart=False   #finish to input vertex info

		###################################################
		##


		##Part6
		#########################################################
		if '#configuration' in line:        ##--# initial configuration
			obsepwarn=False   #end of obstacle info
			confiwarn=True    #start of input of configuration

		if line!='#configuration' and confiwarn==True:     ##--# initial configuration
			confiwarn=False

			confi=[]
			hala=line.split(" ")
			confi=[float(k) for k in hala]

			newobs.setconfigure(confi)    #set initial configuration   ##end of obstacle input
			OB.insertobs(newobs)          #insert newly created obstacle into obstacle list
		#########################################################
		##

	f1.close() 

	return OB











def READROBOT(file2):
	f2=open(file2, "r")

	#ready for number of robots input 
	robotlistwarn=False

	#number of robots
	numRobot=0

	##############################################

	#show if ready to input robot information
	robotsepwarn=False  

	##############################################
	#ready for input number of polygons of an robot
	polywarn=False

	#input number of polygons of an robot
	polynum=0 

	################################
	#ready for input info of polygons
	poowarn=False  

	#ready for input of vertex numbers of a polygon
	vnumwarn=False 

	#vertex number of a polygon
	vertexnum=0

	################################
	#ready to input vertex info
	vertexstart=False

	#judge if the input of vertex is finished
	vertexcount=0
	##################################
	#start of input of configuration
	confiwarnR=False   

	###################################
	#warn of start of input of goal configuration 
	goalwarn=False

	#####################################
	#warn of number of control points
	controlnumwarn=False

	#########################################
	#ready to input control points
	controlinputwarn=False

	#########################################
	#record countdown of control point
	controlcount=0 

	##########################################
	#ready to input series of control points
	controlstart=False

	##########################################

	for i in f2:
		line=i.strip()

		##Part1
		#########################
		if line=='# number of robots':      ##--# number of robots
			RL=robotlist()      #store newly created robots
			robotlistwarn=True
		############################

		if line!='# number of robots' and robotlistwarn==True:      ##--# number of robots
			numRobot=int(line)
			RL.setrobotnums(numRobot)    #set number of robots
			robotlistwarn=False
		###############################
		##

		##Part2
		###################################
		if '# robot #' in line:      ##--# robot #
			robotsepwarn=True   # ready to input robot information
			newrobots=robotS()
		#################################
		##


		##Part3
		####################################
		if '# number of convex parts' in line:     ##--# number of polygons
			polywarn=True   #for input number of polygons of an robot


		if line !='# number of convex parts' and polywarn==True:     ##--# number of polygons
			polynum=int(line)			#input number of polygons of an obstacle
			polywarn=False
			newrobots.setpolynumR(polynum)	#set number of polygons of an obstacle


		#######################################
		##



		##Part4
		############################################
		if '# part #' in line:        ##--# polygon #
			poowarn=True   #ready for input info of polygons
			newpoly=polygon()

		if line == '# number of vertices' and poowarn==True:      ##--# number of vertices
			poowarn=False
			vnumwarn=True   #ready for input of vertex numbers of a polygon

		if line !='# number of vertices' and vnumwarn==True:      ##-# number of vertices
			vertexnum=int(line)    #vertex numbers of a polygon
			newpoly.setvertexnum(vertexnum)   #set vertex number of a polygon
			vnumwarn=False

		#################################################
		##


		##Part5
		#######################################################
		if line=='# vertices':      ##--# vertices
			vertexstart=True   #ready to input vertex info
			vertexcount=0      #judge if the input of vertex is finished
			vv=[]

		if (line!='# vertices') and vertexstart==True and vertexcount<vertexnum:    ##--# vertices
			point=[]
			walaR=line.split(" ")
			point=[float(k) for k in walaR]
			vv.append(point)

			vertexcount=vertexcount+1


		if vertexstart==True and (vertexcount>=vertexnum):
			newpoly.setpoly(vv) #set vertexes of the polygon
			newrobots.setrobotpolys(newpoly)  #set polygons of the robot
			vertexstart=False   #finish to input vertex info

		###################################################
		##


		##Part6
		#########################################################
		if '# initial configuraion' in line:                  ##--# initial configuration
			
			confiwarnR=True    #start of input of configuration

		if line!='# initial configuraion' and confiwarnR==True:      ##--# initial configuration
			confiwarnR=False

			confi2=[]
			hala2=line.split(" ")
			confi2=[float(k) for k in hala2]

			newrobots.setconfigureR(confi2)    #set initial configuration   ##end of robot input
			
		#########################################################
		##


		##Part7
		###########################################################
		if '# goal configuration' in line:   ##--# goal configuration
			goalwarn=True


		if line!='# goal configuration' and goalwarn==True:     ##--# goal configuration
			goalwarn=False
			
			gcon=[]
			gc=line.split(" ")
			gcon=[int(float(k)) for k in gc]

			newrobots.setgoal(gcon)

		#############################################################
		##



		##Part8
		##############################################################
		if '# number of control points' in line:     ##--# number of control points
			controlnumwarn=True
			
			
		if line!='# number of control points' and controlnumwarn==True:   ##--# number of control points
			CNUM=int(line)    #vertex numbers of a controlpoints
			newrobots.setcontrolnum(CNUM)   #set number of a controlpoints of a robot
			controlnumwarn=False
			controlstart=True   #ready to input series of control points
			controlcount=0      #judge if control point input is finished

		#################################################################
		##


		##Part9
		###################################################################
		if '# control point #' in line:    ##--# control point #1
			controlinputwarn=True
			

		if ('# control point #' not in line) and controlinputwarn==True and controlcount<CNUM:    ##--# control point #1
			controlinputwarn=False
			cs=[]
			ci=line.split(" ")
			cs=[float(k) for k in ci]
			newrobots.addcontrolP(cs)

			controlcount=controlcount+1

		if controlstart==True and (controlcount>=CNUM):
			controlstart=False
			robotsepwarn=False                  #end of robot info
			RL.insertrobots(newrobots)          #insert newly created robot into robot list
		##############################################################3
		##

	f2.close() 

	return RL




class ItemR():

	def __init__(self, canvasR, itemsR, CTR, conff):

		self.previous_xR = None
		self.previous_yR = None
		self.selectedR = None

		self.itemsR = itemsR

		self.CanvasR=canvasR

		self.ctr=CTR


		newheadxx=conff[0]
		newheadyy=FW-conff[1]
		newheadang=360-conff[2]

		self.head=[]

		self.head.append(newheadxx)
		self.head.append(newheadyy)
		self.head.append(newheadang)


		#self.des=[]
		#g1=gg[0]    ##goal
		#g2=gg[1]

		#g1=g1    ##g1+HF
		#g2=FW-g2	##HF-g2

		#g1=int(g1)
		#g2=int(g2)

		#self.des.append(g1)
		#self.des.append(g2)

		#self.potential=np.zeros((FW,FW))

		#for i in range(0, self.potential.shape[0]):
		#	for j in range(0, self.potential.shape[1]):
		#		ydiff=abs((i-self.des[1]))
		#		xdiff=abs((j-self.des[0]))

		#		step=ydiff+xdiff
		#		self.potential[i][j]=int(step)


		for item in self.itemsR:
			self.CanvasR.tag_bind(item, '<ButtonPress-1>',   lambda event, tag=item: self.on_press_tagR(event, tag, self.itemsR))
			self.CanvasR.tag_bind(item, '<ButtonRelease-1>', lambda event, tag=item: self.on_release_tagR(event, tag, self.itemsR))
			self.CanvasR.tag_bind(item, '<B1-Motion>', self.on_move_tagR)
			self.CanvasR.tag_bind(item, '<Double-Button-1>', self.start)





		centx=0
		centy=0

		totalvert=0

		for poly in self.itemsR:
			coo=self.CanvasR.coords(poly)

			polyvnum=len(coo)/2

			totalvert=totalvert+polyvnum

			count=0

			for i in range(0,len(coo)):

				if count%2==0:
					centx=centx+coo[i]
				else:
					centy=centy+coo[i]

				count=count+1



		centx=centx/totalvert
		centy=centy/totalvert

		self.center=[]

		self.center.append(centx)
		self.center.append(centy)




	def on_press_tagR(self, event, tag, itemm2R):
		self.selectedR = True
		self.previous_xR = event.x
		self.previous_yR = event.y


		#print('press:', event, tag)

		
		#for i in itemm2:
		#	COO2=self.Canvas.coords(i)

		#	r2=[]
		#	c2=[]
		#	img2 = np.zeros((FW, FW))

		#	count=0

		#	for itr in range(0,len(COO2)):
		#		if (count%2)==0:
		#			r2.append(int(COO2[itr]))
		#		else:
		#			c2.append(int(COO2[itr]))

		#		count=count+1
						
		#	R2=np.array(r2) 
		#	C2=np.array(c2)
				
		#	rr2, cc2 = gy(R2, C2)
		#	img2[rr2, cc2] = -1

		#	totalbitmap=totalbitmap+img2




	def on_release_tagR(self, event, tag, itemmR):
		self.selectedR = False
		self.previous_xR = None
		self.previous_yR = None

		

		#print('release:', event)


		#for i in itemm:
		#	COO=self.Canvas.coords(i)

		#	r=[]
		#	c=[]
		#	img = np.zeros((FW, FW))

		#	count=0

		#	for itr in range(0,len(COO)):
		#		if (count%2)==0:
		#			r.append(int(COO[itr]))
		#		else:
		#			c.append(int(COO[itr]))

		#		count=count+1
						
		#	R=np.array(r) 
		#	C=np.array(c)
				
		#	rr, cc = gy(R, C)
		#	img[rr, cc] = 1

		#	totalbitmap=totalbitmap+img
		#print(self.ctr)

		
		

	def on_move_tagR(self, event):
		#print(event.x, event.x)
		if self.selectedR:
			dxR = event.x - self.previous_xR
			dyR = event.y - self.previous_yR

			for item in self.itemsR:
				self.CanvasR.move(item, dxR, dyR)
			
			self.previous_xR = event.x
			self.previous_yR = event.y


			headx=self.head[0]
			heady=self.head[1]
			headang=self.head[2]

			nheadx=headx+dxR
			nheady=heady+dyR
			nheadang=headang

			nhead=[]
			nhead.append(nheadx)
			nhead.append(nheady)
			nhead.append(nheadang)

			self.head=nhead


			###########################
			temctr=[]

			for i in range(0,len(self.ctr)):
				Ectr=self.ctr[i]
				Ectrx=Ectr[0]
				Ectry=Ectr[1]

				Ectrx=Ectrx+dxR
				Ectry=Ectry+dyR

				Dctr=[]
				Dctr.append(Ectrx)
				Dctr.append(Ectry)    #canvas y

				temctr.append(Dctr)

			self.ctr=temctr
			################################

			temcent=[]
			temcentx=self.center[0]
			temcenty=self.center[1]

			temcentx=temcentx+dxR
			temcenty=temcenty+dyR

			temcent.append(temcentx)
			temcent.append(temcenty)

			self.center=temcent




	def rotate_point2(self, point2, ang2, center_point2):
		
		#canvas x=world x+300
		#canvas y=300-world y

		worldx=point2[0]           ##point2[0]-HF
		worldy=FW-point2[1]        ##HF-point2[1]

		worldcenterx=center_point2[0]   ##center_point2[0]-HF   
		worldcentery=FW-center_point2[1]   ##HF-center_point2[1]

		angle_rad2 = radians(ang2 % 360)
		
		vec2 = (worldx - worldcenterx, worldy - worldcentery)

		new_point2 = (vec2[0] * cos(angle_rad2) - vec2[1] * sin(angle_rad2),
		vec2[0] * sin(angle_rad2) + vec2[1] * cos(angle_rad2))

		finalx=new_point2[0] + worldcenterx      ##new_point2[0] + worldcenterx+ HF
		finaly=FW-(new_point2[1] + worldcentery)    ##HF-(new_point2[1] + worldcentery)

		# Reverse the shifting we have done
		fnew_point2 = (finalx,finaly)
		ffnew_point2=list(fnew_point2)

		return ffnew_point2


	def rotate_polygon2(self, polygon, angle, center_point): 
		
		rotated_polygon2 = []

		for corner in polygon:
			rotated_corner = self.rotate_point2(corner, angle, center_point)

			rotated_polygon2.append(rotated_corner)
	
		return rotated_polygon2






	def getangle(self, pp, cent):

		xx=pp[0]
		yy=pp[1]

		dx = xx - cent[0]
		dy = yy - cent[1]

		try:
			return complex(dx, dy) / abs(complex(dx, dy))
		except ZeroDivisionError:
			return 0.0 # cannot determine angle



	def rotate(self, ang):

		####################
		for robotpoly in self.itemsR:

			#xy = [(50, 50), (150, 50), (150, 150), (50, 150)]
			#polygon_item = c.create_polygon(xy)

			co=self.CanvasR.coords(robotpoly)

			xy=[]

			count=0

			for i in range(0,len(co)):
				if count%2==0:
					xx=co[i]
					temxy=[]
					temxy.append(xx)
				else:
					yy=co[i]
					temxy.append(yy)

					xy.append(temxy)

				count=count+1




			p1=xy[0]
			start=self.getangle(p1, self.center)

			p2=self.rotate_point2(p1, ang, self.center)
			end=self.getangle(p2, self.center)

			angle = end/start

			offset = complex(self.center[0], self.center[1])

			newxy = []
			for x, y in xy:
				v = angle * (complex(x, y) - offset) + offset
				newxy.append(v.real)
				newxy.append(v.imag)

			self.CanvasR.coords(robotpoly, *newxy)

		##############################################
		temRctr=[]

		for i in range(0,len(self.ctr)):
			ERctr=self.ctr[i]
			Rctr=self.rotate_point2(ERctr, ang, self.center)
			temRctr.append(Rctr)

		self.ctr=temRctr


		##########################
		rheadx=self.head[0]
		rheady=self.head[1]
		rheadang=self.head[2]

		rrhead=[]
		rrhead.append(rheadx)
		rrhead.append(rheady)

		newrheadxy=self.rotate_point2(rrhead, ang, self.center)

		newheadang=rheadang+ang

		if newheadang<0:
			newheadang=360+newheadang
		if newheadang>359:
			newheadang=newheadang%360

		#################################
		newhead=[]
		newhead.append(newrheadxy[0])
		newhead.append(newrheadxy[1])
		newhead.append(newheadang)

		self.head=newhead




	def moving(self, tx, ty):

		for item in self.itemsR:
			self.CanvasR.move(item, tx, ty)

		#########################
		temcent2=[]
		temcentx2=self.center[0]
		temcenty2=self.center[1]

		temcentx2=temcentx2+tx
		temcenty2=temcenty2+ty

		temcent2.append(temcentx2)
		temcent2.append(temcenty2)

		self.center=temcent2
		###########################
		temctr2=[]

		for i in range(0,len(self.ctr)):
			Ectr2=self.ctr[i]
			Ectrx2=Ectr2[0]
			Ectry2=Ectr2[1]

			Ectrx2=Ectrx2+tx
			Ectry2=Ectry2+ty

			Dctr2=[]
			Dctr2.append(Ectrx2)
			Dctr2.append(Ectry2)    #canvas y

			temctr2.append(Dctr2)

		self.ctr=temctr2


		##########################################
		mheadx=self.head[0]
		mheady=self.head[1]
		mheadang=self.head[2]

		mheadx=mheadx+tx
		mheady=mheady+ty

		mewhead=[]
		mewhead.append(mheadx)
		mewhead.append(mheady)
		mewhead.append(mheadang)

		self.head=mewhead

























###############################################################################






	def getcommand(self,):
		
		global visited
		global POPO

		rotateunit=1
		moveunit=1
		################################
		specialright=4
		specialup=8
		specialrotate=5

		##
		specialcenter=[]

		specialcenter.append((self.center[0]+specialright))
		specialcenter.append((self.center[1]-specialup))
		###################3
		potclock=0
		potUclock=0

		potL=0
		potR=0
		potU=0
		potD=0

		potcom1=0


		judgecpx=self.head[0]
		judgecpy=self.head[1]
		judgecpang=self.head[2]

		####################################
		#firstpoly=self.itemsR[0]
		#fco=self.CanvasR.coords(firstpoly)
		#judgecpx=fco[0]
		#judgecpy=fco[1]


		################3
		#judgecp=self.ctr[1]
		#judgecpx=judgecp[0]
		#judgecpy=judgecp[1]
		#################


		###########
		#k1=self.des[0]
		#k2=self.des[1]
		#see=self.potential[k2][k1]
		###########

		potentialList=[]


		potential=POPO[0]     ##



		for i in range(0,len(self.ctr)):
			ctp=self.ctr[i]

			ctpx=ctp[0]  #canvasx  at col
			ctpy=ctp[1]  #canvasy  at row

			ctpx=int(ctpx)
			ctpy=int(ctpy)

			##############################################3
			clockctr=self.rotate_point2(ctp, rotateunit, self.center)

			clockctrx=clockctr[0]
			clockctry=clockctr[1]

			clockcol=int(clockctrx)
			clockrow=int(clockctry)

			tempoclock=potential[clockrow][clockcol]
			###################################################3

			Uclockctr=self.rotate_point2(ctp, -rotateunit, self.center)

			Uclockctrx=Uclockctr[0]
			Uclockctry=Uclockctr[1]

			Uclockcol=int(Uclockctrx)
			Uclockrow=int(Uclockctry)

			tempoUclock=potential[Uclockrow][Uclockcol]
			#################################################



			tempoL=potential[ctpy][(ctpx-moveunit)]
			tempoR=potential[ctpy][(ctpx+moveunit)]

			tempoU=potential[(ctpy-moveunit)][ctpx]
			tempoD=potential[(ctpy+moveunit)][ctpx]

			################################################

			spp=[]
			spp.append((ctpx+specialright))
			spp.append((ctpy-specialup))

			specialclockctr=self.rotate_point2(spp, -specialrotate, specialcenter)

			specialclockctrx=specialclockctr[0]
			specialclockctry=specialclockctr[1]

			specialclockcol=int(specialclockctrx)
			specialclockrow=int(specialclockctry)

			tempocom1=potential[specialclockrow][specialclockcol]

			#tempocom1=potential[(ctpy-specialup)][ctpx+specialright]

			#################################################

			potclock=potclock+tempoclock
			potUclock=potUclock+tempoUclock

			################################################3
			potL=potL+tempoL
			potR=potR+tempoR
			potU=potU+tempoU
			potD=potD+tempoD
			###########################################
			potcom1=potcom1+tempocom1
			############################################

		    
		potentialList.append(potL)		 
		potentialList.append(potR)
		potentialList.append(potU)
		potentialList.append(potD)
		potentialList.append(potclock)
		potentialList.append(potUclock)

		potentialList.append(potcom1)
		##################################
		
		Dict = {} 
		for i in range(0,len(potentialList)):
			Dict[i]=potentialList[i]

		ss={k: v for k, v in sorted(Dict.items(), key=lambda item: item[1])}


		CMD=-1


		##########################################################
		global twice

		BUMPLIST=self.bumpcheck()


		#########################################################
		##


		Dict2 = {} 

		twicecount=[]

		for i in range(0,len(potentialList)):

			if i==0:
				coll=int(judgecpx-moveunit)
				roww=int(judgecpy)

				angg=int(judgecpang)

			if i==1:
				coll=int(judgecpx+moveunit)
				roww=int(judgecpy)

				angg=int(judgecpang)

			if i==2:
				coll=int(judgecpx)
				roww=int(judgecpy-moveunit)

				angg=int(judgecpang)

			if i==3:
				coll=int(judgecpx)
				roww=int(judgecpy+moveunit)

				angg=int(judgecpang)

			if i==4:
				dc=[]
				dc.append(judgecpx)
				dc.append(judgecpy)
				
				dcr=self.rotate_point2(dc, rotateunit, self.center)

				dcrx=dcr[0]
				dcry=dcr[1]

				coll=int(dcrx)
				roww=int(dcry)

				angg=int(judgecpang+rotateunit)

				if angg>359:
					angg=angg%360

				
			if i==5:
				dc2=[]
				dc2.append(judgecpx)
				dc2.append(judgecpy)
				
				dcr2=self.rotate_point2(dc2, -rotateunit, self.center)

				dcrx2=dcr2[0]
				dcry2=dcr2[1]

				coll=int(dcrx2)
				roww=int(dcry2)

				angg=int(judgecpang-rotateunit)

				if angg<0:
					angg=360+angg


			if i==6:
				spedc2=[]
				spedc2.append((judgecpx+specialright))
				spedc2.append((judgecpy-specialup))
				
				spedcr2=self.rotate_point2(spedc2, -specialrotate, specialcenter)

				spedcrx2=spedcr2[0]
				spedcry2=spedcr2[1]

				coll=int(spedcrx2)
				roww=int(spedcry2)

				angg=int(judgecpang-specialrotate)

				if angg<0:
					angg=360+angg

			twibuffer=twice[roww,coll,angg]
			twicecount.append(twibuffer)



		for i in range(0,len(potentialList)):
			see=list(ss.keys())[i]
			Dict2[see]=twicecount[see]

		ss2={k: v for k, v in sorted(Dict2.items(), key=lambda item: item[1])}



		#for i in range(0,len(potentialList)):
		#	see=list(ss.keys())[i]


		##
		###############################################################

		for i in range(0,len(potentialList)):
			see2=list(ss2.keys())[i]
			#see=list(ss.keys())[i]

			if see2==0:
				coll=int(judgecpx-moveunit)
				roww=int(judgecpy)

				angg=int(judgecpang)

			if see2==1:
				coll=int(judgecpx+moveunit)
				roww=int(judgecpy)

				angg=int(judgecpang)

			if see2==2:
				coll=int(judgecpx)
				roww=int(judgecpy-moveunit)

				angg=int(judgecpang)

			if see2==3:
				coll=int(judgecpx)
				roww=int(judgecpy+moveunit)

				angg=int(judgecpang)

			if see2==4:
				dc=[]
				dc.append(judgecpx)
				dc.append(judgecpy)
				
				dcr=self.rotate_point2(dc, rotateunit, self.center)

				dcrx=dcr[0]
				dcry=dcr[1]

				coll=int(dcrx)
				roww=int(dcry)

				angg=int(judgecpang+rotateunit)

				if angg>359:
					angg=angg%360

				

			if see2==5:
				dc2=[]
				dc2.append(judgecpx)
				dc2.append(judgecpy)
				
				dcr2=self.rotate_point2(dc2, -rotateunit, self.center)

				dcrx2=dcr2[0]
				dcry2=dcr2[1]

				coll=int(dcrx2)
				roww=int(dcry2)

				angg=int(judgecpang-rotateunit)

				if angg<0:
					angg=360+angg

			if see2==6:
				spedc2=[]
				spedc2.append((judgecpx+specialright))
				spedc2.append((judgecpy-specialup))
				
				spedcr2=self.rotate_point2(spedc2, -specialrotate, specialcenter)

				spedcrx2=spedcr2[0]
				spedcry2=spedcr2[1]

				coll=int(spedcrx2)
				roww=int(spedcry2)

				angg=int(judgecpang-specialrotate)

				if angg<0:
					angg=360+angg



			repeat=False
			check=False


			check=BUMPLIST[see2]


			##############################################
			


			if check==True:
				visited[roww,coll,angg]=True
				twice[roww,coll,angg]=2

			
			if twice[roww,coll,angg]==2:
				repeat=True

			#############################################
			#if check==True:
			#	visited[roww,coll,angg]=True


			#if visited[roww,coll,angg]==True:
			#	repeat=True




			#####################################
			#if visited[roww,coll,angg]==True:
			#	repeat=True
			#else:
			#	check=self.bumpcheck(see)

				#print(f"command: {see} , bump: {check}.") 


			#	if check==True:
			#		visited[roww,coll,angg]=True
			##########################################












			###################################################
			#flowleft=int(judgecpx-1)
			#flowright=int(judgecpx+1)

			#flowup=int(judgecpy-1)
			#flowdown=int(judgecpy+1)

			#flownowx=int(judgecpx)
			#flownowy=int(judgecpy)


			#if ((visited[flowup,flownowx,angg]==True) and (visited[flownowy,flowright,angg]==True)) or ((visited[flowdown,flownowx,angg]==True) and (visited[flownowy,flowright,angg]==True)) or ((visited[flowup,flownowx,angg]==True) and (visited[flownowy,flowleft,angg]==True)) or ((visited[flowdown,flownowx,angg]==True) and (visited[flownowy,flowleft,angg]==True)) or ((visited[flowup,flownowx,angg]==True) and (visited[flowdown,flownowx,angg]==True)) or (visited[flownowy,flowright,angg]==True) or (visited[flowdown,flownowx,angg]==True):
			#	visited[flownowy,flownowx,angg]=True










			###################################################################


			#if (check==False) and (repeat==False):
			#	CMD=see

			#	visited[roww,coll,angg]=True
			#	break
			##############################################################
			if repeat==False:
				CMD=see2
				visited[roww,coll,angg]=True
				twice[roww,coll,angg]+=1
				break


		#print('######################')


		return CMD

########################################################################################

	#def checkcheck(self,):


	#	global totalbitmap

	#	checkmap=np.zeros((FW, FW))


	#	for polyp in self.itemsR:
	#		COO=self.CanvasR.coords(polyp)

	#		r=[]
	#		c=[]
	#		img = np.zeros((FW, FW))

	#		count=0

	#		for itr in range(0,len(COO)):
	#			if (count%2)==0:
	#				c.append(int(COO[itr]))
	#			else:
	#				r.append(int(COO[itr]))

	#			count=count+1
						
	#		R=np.array(r) 
	#		C=np.array(c)
				
	#		rr, cc = gy(R, C)
	#		img[rr, cc] = 1

	#		checkmap=checkmap+img


	#	checkmap=checkmap+totalbitmap

	#	have2=False

	#	for i in range(0,checkmap.shape[0]):
	#		for j in range(0,checkmap.shape[1]):
	#			if checkmap[i][j]==2:
	#				have2=True
	#				return have2
		##############################################

		#for i in range(0,totalbitmap.shape[0]):
		#	for j in range(0,totalbitmap.shape[1]):
		#		if totalbitmap[i][j]==2:
		#			have2=True
		#			return have2


		################################################



	#	return have2






####################################################################3


	def bumpcheck(self,):
		
		#bump=False

		global totalbitmap


		rotateunit=1
		moveunit=1

		specialright=4
		specialup=8
		specialrotate=5


		bumpL=False
		bumpR=False
		bumpU=False
		bumpD=False

		bumpclock=False
		bumpUclock=False

		bumpcom1=False

		#################################################
		specialcenter=[]

		specialcenter.append((self.center[0]+specialright))
		specialcenter.append((self.center[1]-specialup))


		##################################################
		for robotpoly in self.itemsR:
			co=self.CanvasR.coords(robotpoly)

			fincooL=[]
			fincooR=[]
			fincooU=[]
			fincooD=[]

			fincooclock=[]
			fincooUclock=[]

			fincoo=[]

			fincom1=[]


			for i in range(0,len(co)):
				if i%2==0:
					temcoL=[]
					temcoR=[]
					temcoU=[]
					temcoD=[]

					temcocom1=[]
					##################################
					temc=[]
					####################################
					temx=co[i]

					temxL=temx-moveunit
					temxR=temx+moveunit
					temxU=temx
					temxD=temx

					temxcom1=temx+specialright

				else:
					temy=co[i]

					temyL=temy
					temyR=temy
					temyU=temy-moveunit
					temyD=temy+moveunit

					temycom1=temy-specialup

					######################################
					temcoL.append(temxL)
					temcoL.append(temyL)

					temcoR.append(temxR)
					temcoR.append(temyR)

					temcoU.append(temxU)
					temcoU.append(temyU)

					temcoD.append(temxD)
					temcoD.append(temyD)

					################################3
					temc.append(temx)
					temc.append(temy)
					############################
					temcocom1.append(temxcom1)
					temcocom1.append(temycom1)

					##############################
					fincooL.append(temcoL)
					fincooR.append(temcoR)
					fincooU.append(temcoU)
					fincooD.append(temcoD)
					##################################
					fincoo.append(temc)
					#################################
					fincom1.append(temcocom1)

			#############
			fincooclock=self.rotate_polygon2(fincoo, rotateunit, self.center)
			fincooUclock=self.rotate_polygon2(fincoo, -rotateunit, self.center)

			##############################
			

			specialclock=self.rotate_polygon2(fincom1, -specialrotate, specialcenter)

			#############################

			polyL = Polygon(fincooL)
			polyR = Polygon(fincooR)
			polyU = Polygon(fincooU)
			polyD = Polygon(fincooD)
			polyclock = Polygon(fincooclock)
			polyUclock = Polygon(fincooUclock)

			polycom1=Polygon(specialclock)





			for m in range(0,totalbitmap.shape[0]):
				for n in range(0,totalbitmap.shape[1]):
					obb=totalbitmap[m][n]

					if obb!=0:
						oby=m
						obx=n
						pc = Point(obx,oby)

						if bumpL==False:
							bumpL=polyL.contains(pc)

						if bumpR==False:
							bumpR=polyR.contains(pc)

						if bumpU==False:
							bumpU=polyU.contains(pc)

						if bumpD==False:
							bumpD=polyD.contains(pc)

						if bumpclock==False:
							bumpclock=polyclock.contains(pc)

						if bumpUclock==False:
							bumpUclock=polyUclock.contains(pc)

						if bumpcom1==False:
							bumpcom1=polycom1.contains(pc)

						
						
		bumplist=[]

		bumplist.append(bumpL)
		bumplist.append(bumpR)
		bumplist.append(bumpU)
		bumplist.append(bumpD)

		bumplist.append(bumpclock)
		bumplist.append(bumpUclock)

		bumplist.append(bumpcom1)



		###################################################

		#if comm==0:
		#	self.moving(-1,0)
		#	bump=self.checkcheck()
		#	self.moving(1,0)
		#if comm==1:
		#	self.moving(1,0)
		#	bump=self.checkcheck()
		#	self.moving(-1,0)

		#if comm==2:
		#	self.moving(0,-1)
		#	bump=self.checkcheck()
		#	self.moving(0,1)
		#if comm==3:
		#	self.moving(0,1)
		#	bump=self.checkcheck()
		#	self.moving(0,-1)

		#if comm==4:
		#	self.rotate(1)
		#	bump=self.checkcheck()
		#	self.rotate(-1)

		#if comm==5:
		#	self.rotate(-1)
		#	bump=self.checkcheck()
		#	self.rotate(1)
		############################################







		#########################################################
		#for robotpoly in self.itemsR:
		#	co=self.CanvasR.coords(robotpoly)
		#	count=0


		#	if comm<4:
		#		for i in range(0,len(co)):
		#			if count%2==0:
		#				xx=co[i]   #col
		#			else:
		#				yy=co[i]   #row
					
		#				if comm==0:   #left
		#					col=xx-1
		#					row=yy
		#				if comm==1:   #right
		#					col=xx+1
		#					row=yy
		#				if comm==2:   #up
		#					col=xx
		#					row=yy-1
		#				if comm==3:   #down
		#					col=xx
		#					row=yy+1

		#				row=int(row)
		#				col=int(col)
		#				if totalbitmap[row][col]!=0:
		#					bump=True

		#			count=count+1
		#	else:

		#		xys=[]

		#		count=0

		#		for j in range(0,len(co)):
		#			if count%2==0:
		#				xx=co[j]
		#				temxy=[]
		#				temxy.append(xx)
		#			else:
		#				yy=co[j]
		#				temxy.append(yy)

		#				xys.append(temxy)

		#			count=count+1


		#		if comm==4:
		#			rot=self.rotate_polygon2(xys, 1, self.center)

		#			for m in rot:
		#				col=m[0]  #x after rotation
		#				row=m[1]  #y after rotation
		#				col=int(col)
		#				row=int(row)

		#				if totalbitmap[row][col]!=0:
		#					bump=True

		#		if comm==5:
		#			rot2=self.rotate_polygon2(xys, -1, self.center)

		#			for m2 in rot2:
		#				col=m2[0]  #x after rotation
		#				row=m2[1]  #y after rotation
		#				col=int(col)
		#				row=int(row)

		#				if totalbitmap[row][col]!=0:
		#					bump=True


		#############################################################






		return bumplist
		#return bump





































	'''
	#################################################################################
	def selectrotate(self,):
		#global visited
		global POPO

		ch1,ch2=self.bumpcheckrotate()

		cL=ch1[0]
		ucL=ch1[1]

		mcL=ch2[0]
		mucL=ch2[1]

		#############################################
		coll=int(self.head[0])
		roww=int(self.head[1])
		anglenow=int(self.head[2])

		potential=POPO[0]

		############################################
		rotcandi=[]

		for cc in range(0,len(cL)):
			candy=cc+1
			endclock=anglenow-candy

			#visited[roww,coll,endclock]=True

			if (cL[cc]==0) and (mcL[cc]!=1):
				rotcandi.append(candy)


		rotcandiU=[]

		for ccU in range(0,len(ucL)):
			candyU=-(ccU+1)
			endclockU=anglenow-candyU
			#visited[roww,coll,endclockU]=True

			if (ucL[ccU]==0) and (mucL[ccU]!=1):
				rotcandiU.append(candyU)

		################################################
		rotval=[0]*len(rotcandi)
		rotvalU=[0]*len(rotcandiU)
		###############################################

		for i in range(0,len(self.ctr)):
			ctp=self.ctr[i]
			
			################################################
			tempolist=[]

			for can in range(0,len(rotcandi)):

				ann=rotcandi[can]
				clockctr=self.rotate_point2(ctp, ann, self.center)
				clockctrx=clockctr[0]
				clockctry=clockctr[1]
				
				clockcol=int(clockctrx)
				clockrow=int(clockctry)
				
				tempoclock=potential[clockrow][clockcol]

				tempolist.append(tempoclock)

			rotval=rotval+tempolist

			#################################################
			tempolistU=[]


			for canU in range(0,len(rotcandiU)):
				annU=rotcandiU[canU]
				Uclockctr=self.rotate_point2(ctp, annU, self.center)

				Uclockctrx=Uclockctr[0]
				Uclockctry=Uclockctr[1]

				Uclockcol=int(Uclockctrx)
				Uclockrow=int(Uclockctry)

				tempoUclock=potential[Uclockrow][Uclockcol]

				tempolistU.append(tempoUclock)

			rotvalU=rotvalU+tempolistU
		###################################################3
		smallestrotatecandy=0
		smallestrotateval=255

		smallestrotatecandyU=0
		smallestrotatevalU=255

		#######################################################3
		for i in range(0,len(rotval)):
			sese=rotval[i]

			if sese<smallestrotateval:
				smallestrotatecandy=rotcandi[i]
				smallestrotateval=sese
			
		#################################################
		for i in range(0,len(rotvalU)):
			seseU=rotvalU[i]

			if seseU<smallestrotatevalU:
				smallestrotatecandyU=rotcandiU[i]
				smallestrotatevalU=seseU


		finrot=0

		if smallestrotateval<=smallestrotatevalU:
			finrot=smallestrotatecandy
		else:
			finrot=smallestrotatecandyU



		#####################################################
		return finrot










	#########################################################################

	def bumpcheckrotate(self,):
		###########################################
		global totalbitmap
		
		highest=127
		leftmost=127

		lowest=0
		rightmost=0
		############################################


		for robotpoly in self.itemsR:
			co=self.CanvasR.coords(robotpoly)

			for i in range(0,len(co)):
				if i%2==0:

					xx=co[i]

					if xx<leftmost:
						leftmost=xx
					if xx>rightmost:
						rightmost=xx
				else:
					yy=co[i]

					if yy<highest:
						highest=yy
					if yy>lowest:
						lowest=yy

		#################################################

		searchrange=15

		highsearch=int(highest-searchrange)
		lowsearch=int(lowest+searchrange)

		leftsearch=int(leftmost-searchrange)
		rightsearch=int(rightmost+searchrange)

		if highsearch<0:
			highsearch=0
		if lowsearch>127:
			lowsearch=127
		if leftsearch<0:
			leftsearch=0
		if rightsearch>127:
			rightsearch=127
		##################################################

		finbumplist=[]

		anglenow=self.head[2]
		maxUclockdif=int(360-anglenow)
		maxclockdif=int(anglenow-0)

		marktotal=[]
		##################################################
		for robotpoly in self.itemsR:
			co=self.CanvasR.coords(robotpoly)
			fincoo=[]
			#####################################
			for i in range(0,len(co)):
				if i%2==0:
					temc=[]
					temx=co[i]
				else:
					temy=co[i]
					temc.append(temx)
					temc.append(temy)
					fincoo.append(temc)
			########################################



			clocklist=[]
			fincooclock=[]


			stop=False

			markclock=[]

			if maxclockdif>0:
				for cc in range(1,(maxclockdif+1)):

					fincooclock=self.rotate_polygon2(fincoo, cc, self.center)
					polyclock = Polygon(fincooclock)

					bumpclock=False

					for m in range(highsearch,lowsearch):
						for n in range(leftsearch,rightsearch):
							obb=totalbitmap[m][n]

							if obb!=0:
								oby=m
								obx=n
								pc = Point(obx,oby)

								if bumpclock==False:
									bumpclock=polyclock.contains(pc)

					bumpans=0

					if bumpclock==True:
						bumpans=1
						stop=True
					else:
						bumpans=0

					if (bumpclock==False) and (stop==True):
						markclock.append(1)
					else:
						markclock.append(0)

					clocklist.append(bumpans)

			finbumplist.append(clocklist)
			marktotal.append(markclock)





			###########################################################
			Uclocklist=[]
			fincooUclock=[]

			stop2=False
			markclock2=[]


			if maxUclockdif>1:
				for uu in range(1,maxUclockdif):
					fincooUclock=self.rotate_polygon2(fincoo, -uu, self.center)
					polyUclock = Polygon(fincooUclock)

					bumpUclock=False

					for m1 in range(highsearch,lowsearch):
						for n1 in range(leftsearch,rightsearch):
							obb1=totalbitmap[m1][n1]

							if obb1!=0:
								oby1=m1
								obx1=n1
								pc1 = Point(obx1,oby1)

								if bumpUclock==False:
									bumpUclock=polyUclock.contains(pc1)

					bumpansU=0

					if bumpUclock==True:
						bumpansU=1
						stop2=True
					else:
						bumpansU=0


					if (bumpUclock==False) and (stop2==True):
						markclock2.append(1)
					else:
						markclock2.append(0)


					Uclocklist.append(bumpansU)

			
			finbumplist.append(Uclocklist)
			marktotal.append(markclock2)
			################################################################


		return finbumplist,marktotal

	#######################################################################################

	def bumpcheckmoving(self,):
		global totalbitmap


		bumpL=False
		bumpR=False
		bumpU=False
		bumpD=False

	
		##################################################
		for robotpoly in self.itemsR:
			co=self.CanvasR.coords(robotpoly)

			fincooL=[]
			fincooR=[]
			fincooU=[]
			fincooD=[]

			for i in range(0,len(co)):
				if i%2==0:
					temcoL=[]
					temcoR=[]
					temcoU=[]
					temcoD=[]

					temx=co[i]

					temxL=temx-1
					temxR=temx+1
					temxU=temx
					temxD=temx

				else:
					temy=co[i]

					temyL=temy
					temyR=temy
					temyU=temy-1
					temyD=temy+1

					##############
					temcoL.append(temxL)
					temcoL.append(temyL)

					temcoR.append(temxR)
					temcoR.append(temyR)

					temcoU.append(temxU)
					temcoU.append(temyU)

					temcoD.append(temxD)
					temcoD.append(temyD)

	
					##############################
					fincooL.append(temcoL)
					fincooR.append(temcoR)
					fincooU.append(temcoU)
					fincooD.append(temcoD)
					##################################

			polyL = Polygon(fincooL)
			polyR = Polygon(fincooR)
			polyU = Polygon(fincooU)
			polyD = Polygon(fincooD)
	

			for m in range(0,totalbitmap.shape[0]):
				for n in range(0,totalbitmap.shape[1]):
					obb=totalbitmap[m][n]

					if obb!=0:
						oby=m
						obx=n
						pc = Point(obx,oby)

						if bumpL==False:
							bumpL=polyL.contains(pc)

						if bumpR==False:
							bumpR=polyR.contains(pc)

						if bumpU==False:
							bumpU=polyU.contains(pc)

						if bumpD==False:
							bumpD=polyD.contains(pc)

						
		bumplist=[]

		bumplist.append(bumpL)
		bumplist.append(bumpR)
		bumplist.append(bumpU)
		bumplist.append(bumpD)

		return bumplist




	###################################################################################3

	def getcommand2(self,):
		global visited
		global POPO

		potrot=0

		potL=0
		potR=0
		potU=0
		potD=0

		judgecpx=self.head[0]
		judgecpy=self.head[1]
		judgecpang=self.head[2]


		potentialList=[]
		potential=POPO[0]     

		angsel=self.selectrotate()

		for i in range(0,len(self.ctr)):
			ctp=self.ctr[i]

			ctpx=ctp[0]  #canvasx  at col
			ctpy=ctp[1]  #canvasy  at row

			ctpx=int(ctpx)
			ctpy=int(ctpy)

			##############################################3
			rotctr=self.rotate_point2(ctp, angsel, self.center)

			rotctrx=rotctr[0]
			rotctry=rotctr[1]

			rotcol=int(rotctrx)
			rotrow=int(rotctry)

			temporot=potential[rotrow][rotcol]
			###################################################3

			tempoL=potential[ctpy][(ctpx-1)]
			tempoR=potential[ctpy][(ctpx+1)]

			tempoU=potential[(ctpy-1)][ctpx]
			tempoD=potential[(ctpy+1)][ctpx]


			#################################################

			potrot=potrot+temporot

			potL=potL+tempoL
			potR=potR+tempoR
			potU=potU+tempoU
			potD=potD+tempoD
			###########################################

		    
		potentialList.append(potL)		 
		potentialList.append(potR)
		potentialList.append(potU)
		potentialList.append(potD)

		potentialList.append(potrot)

		##################################
		
		Dict = {} 
		for i in range(0,len(potentialList)):
			Dict[i]=potentialList[i]

		ss={k: v for k, v in sorted(Dict.items(), key=lambda item: item[1])}


		CMD=-1

		##########################################################
		oldcpx=int(self.head[0])
		oldcpy=int(self.head[1])
		
		#########################################################
		BUMPLIST=self.bumpcheckmoving()

		for i in range(0,len(potentialList)):
			repeat=False
			check=False
			angsent=0

			see2=list(ss.keys())[i]

			if see2==4:
				dc=[]
				dc.append(judgecpx)
				dc.append(judgecpy)
				
				dcr=self.rotate_point2(dc, angsel, self.center)

				dcrx=dcr[0]
				dcry=dcr[1]

				coll=int(dcrx)
				roww=int(dcry)
				angg=int(judgecpang-angsel)

				if angg<0:
					angg=360+angg
				if angg>359:
					angg=angg%360

				angsent=angg

			else:
				check=BUMPLIST[see2]

				angsent=0

				if see2==0:
					coll=int(judgecpx-1)
					roww=int(judgecpy)
					angg=int(judgecpang)

				if see2==1:
					coll=int(judgecpx+1)
					roww=int(judgecpy)
					angg=int(judgecpang)

				if see2==2:
					coll=int(judgecpx)
					roww=int(judgecpy-1)
					angg=int(judgecpang)

				if see2==3:
					coll=int(judgecpx)
					roww=int(judgecpy+1)
					angg=int(judgecpang)
				
				if check==True:
					visited[roww,coll,angg]=True
			
			###########################################
			if visited[roww,coll,angg]==True:
				repeat=True

			##########################################
			if repeat==False:
				CMD=see2

				for kk in range(0,360):
					visited[oldcpy,oldcpx,kk]=True

				#visited[roww,coll,angg]=True
				break
			##############################################################
	
		return CMD,angsent

	###############################################################################################
	'''

	






	def start(self, event):
		
	################################################
		steps=0

		rotateunit=1
		moveunit=1

		specialright=4
		specialup=8
		specialrotate=5



		while steps<10:
			cmmd=self.getcommand()
			#cmmd,agg=self.getcommand2()

			#print(cmmd)

			if cmmd==0:
				self.moving(-moveunit,0)       #left

			if cmmd==1:
				self.moving(moveunit,0)       #right

			if cmmd==2:                #up
				self.moving(0,-moveunit)

			if cmmd==3:                #down
				self.moving(0,moveunit)

			if cmmd==4:                #rotate
				self.rotate(rotateunit)

			if cmmd==5:                #rotate
				self.rotate(-rotateunit)

			if cmmd==-1:
				self.moving(0,-16)



			#if cmmd==6:
			#	self.moving(0,-specialup)
			#	self.moving(specialright, 0)
			#	self.rotate(-specialrotate)

			steps=steps+1

			


		 

###################################################################
#obt=READOBS("obstacle.dat.txt")
#rbt=READROBOT("robot.dat.txt")
######################################################################

obt=READOBS("obstacle0.dat")
rbt=READROBOT("robot0.dat")

###############################################################


p= project(obt,rbt)
p.RUN()

