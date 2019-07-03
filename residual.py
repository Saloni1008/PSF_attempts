#import numpy as np
#import emcee
from astropy.io import fits
from subprocess import call
import sys;
from scipy.optimize import *
from scipy import signal
from scipy import interpolate
hdulist=fits.open("data_image.fits")#the name of the input image
data1=hdulist[0].data;
hdulist.close();
hdulist=fits.open("1_image.fits")              #the name of the input image
mod1=hdulist[0].data;
hdulist.close();             
hdu = fits.PrimaryHDU(data1-mod1[3]);
hdu.writeto('res_light_image.fits')
