import os
import sys
from numpy import *
from matplotlib.pyplot import *
import ss as pypl
import ss.pload as pp
import ss.Image as img

plutodir = os.environ['PLUTO_DIR']
wdir = plutodir+'/Test_Problems/MHD/Orszag_Tang/'
nlinf = pypl.nlast_info(w_dir=wdir)

D = pp.pload(nlinf['nlast'],w_dir=wdir) # Loading the data into a pload object D.
I = img.Image()
I.pldisplay(D, D.rho,x1=D.x1,x2=D.x2,label1='x',label2='y',title=r'Density $\rho$ [Orszag Tang test]',cbar=(True,'vertical'))
savefig('orszag_tang_1.png') # Only to be saved as either .png or .jpg
show()
