#!/usr/bin/env python

# ThreeVal`_formula.py
# F. ThreeVal et Al., MRM 67 (2012) 1609-1619
# The BeBo Company, 2018

import sys
import re
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

if ( len ( sys.argv ) == 2 ) :
        cmdarg =  sys.argv[1];
        if ( re.search ( "help$", cmdarg ) or re.match( '-h$', cmdarg ) ):
                print ( "Usage: ThreeVal_formula.py -enne <n> -alpha1 <alpha1> -alpha2 <alpha2>" \
                         " -t_arre <TR> -t_er <TER> -t_ah <TA> -t_beh <TB> -t_ceh <TC>"\
                         " -datadir <datadir>" );
                exit ( 1 );

if ( len ( sys.argv ) != 19 ) :
        print ( "Usage: ThreeVal_formula.py -enne <n> -alpha1 <alpha1> -alpha2 <alpha2>" \
                 " -t_arre <TR> -t_er <TER> -t_ah <TA> -t_beh <TB> -t_ceh <TC>"\
                 " -datadir <datadir>" );
        exit ( 1 )

while ( sys.argv ):
        cmdarg = sys.argv.pop ( 0 );
        if ( cmdarg == '-enne' ):
                enne = int ( sys.argv.pop ( 0 ) )
        elif ( cmdarg == "-alpha1" ):
                alpha_1 = float ( sys.argv.pop ( 0 ) ) * 2 * np.pi / 360
        elif ( cmdarg == "-alpha2" ):
                alpha_2 = float ( sys.argv.pop ( 0 ) ) * 2 * np.pi / 360
        elif ( cmdarg == "-T1" ):
                T1 = float ( sys.argv.pop ( 0 ) ) 
        elif ( cmdarg == "-t_arre" ):
                TR = float ( sys.argv.pop ( 0 ) ) 
        elif ( cmdarg == "-t_er" ):
                TER = float ( sys.argv.pop ( 0 ) ) 
        elif ( cmdarg == "-t_ah" ):
                TA = float ( sys.argv.pop ( 0 ) ) 
        elif ( cmdarg == "-t_beh" ):
                TB = float ( sys.argv.pop ( 0 ) ) 
        elif ( cmdarg == "-t_ceh" ):
                TC = float ( sys.argv.pop ( 0 ) ) 
        elif ( cmdarg == "-datadir" ):
                data_dir = sys.argv.pop ( 0 )

T1 = np.array([]);
T1 = np.arange(0.5, 3.6, 0.5)
B1 = np.array([]);
B1 = np.arange(0.005, 3.5, 0.05)
#print ( B1 )
print ( T1.shape[0], B1.shape[0] )
E1 = np.array([])
E1 = np.exp( -TER / T1 )
EA = np.array([])
EA = np.exp ( - TA / T1 )
EB = np.array([])
EB = np.exp ( - TB / T1 )
EC = np.array([])
EC = np.exp ( - TC / T1 )
ED = np.array([])
ED = np.exp (  TC / T1 )

# the steady-state
mon_z_ss = np.arange( T1.shape[0] * B1.shape[0], dtype = np.float64 ).reshape( T1.shape[0], B1.shape[0] )
first_expr = np.arange( T1.shape[0] * B1.shape[0], dtype=np.float64 ).reshape( T1.shape[0],B1.shape[0] )
second_expr = np.arange( T1.shape[0] * B1.shape[0], dtype=np.float64 ).reshape( T1.shape[0], B1.shape[0] )
third_expr = np.arange( T1.shape[0] * B1.shape[0], dtype=np.float64 ).reshape( T1.shape[0], B1.shape[0] )
fourth_expr = np.arange( T1.shape[0] * B1.shape[0], dtype=np.float64 ).reshape( T1.shape[0], B1.shape[0] )
denom = np.arange( T1.shape[0] * B1.shape[0], dtype=np.float64 ).reshape( T1.shape[0], B1.shape[0] )
Factor_1n = np.arange( T1.shape[0] * B1.shape[0], dtype=np.float64 ).reshape( T1.shape[0], B1.shape[0] )
Factor_2n = np.arange( T1.shape[0] * B1.shape[0], dtype=np.float64 ).reshape( T1.shape[0], B1.shape[0] )
Factor_2np = np.arange( T1.shape[0] * B1.shape[0], dtype=np.float64 ).reshape( T1.shape[0], B1.shape[0] )
Factor_1d = np.arange( T1.shape[0] * B1.shape[0], dtype=np.float64 ).reshape( T1.shape[0], B1.shape[0] )
Factor_2d = np.arange( T1.shape[0] * B1.shape[0], dtype=np.float64 ).reshape( T1.shape[0], B1.shape[0] )
GRE_I = np.arange( T1.shape[0] * B1.shape[0], dtype=np.float64 ).reshape( T1.shape[0], B1.shape[0] )
GRE_II = np.arange( T1.shape[0] * B1.shape[0], dtype=np.float64 ).reshape( T1.shape[0], B1.shape[0] )
SA2RAGE = np.arange( T1.shape[0] * B1.shape[0], dtype=np.float64 ).reshape( T1.shape[0], B1.shape[0] )
print ( first_expr.dtype )
first_expr[0,0] = 3.141592
print ( first_expr.dtype )
print ( first_expr[0,0] )
for i in range (0, len ( T1 ) ):
    for j in range (0, len ( B1 ) ):
        first_expr[i,j] = ( (1 - EA[i] ) * np.power ( np.cos ( alpha_1 * B1[j] ) * E1[i], enne ) )
        second_expr[i,j] = ( 1 - E1[i] ) * ( ( 1 - np.power ( np.cos ( alpha_1 * B1[j] ) * E1[i], enne ) ) \
                      / ( 1 - np.cos ( alpha_1 * B1[j] ) * E1[i] ) )
        third_expr[i,j] = np.power ( np.cos ( alpha_2 * B1[j]  ) * E1[i], enne )
        fourth_expr[i,j] = ( 1 - E1[i] ) * ( ( 1 - np.power ( np.cos ( alpha_2 * B1[j] ) * E1[i], enne ) ) \
                      / ( 1 - np.cos ( alpha_2 * B1[j] ) * E1[i] ) ) 
        denom[i,j] = 1 - np.cos ( 0.5 * np.pi * B1[j] ) * np.power ( np.cos ( alpha_1 * B1[j] ) * np.cos ( alpha_2 * B1[j] ), enne ) \
                * np.exp ( - TR / T1[i] )
        mon_z_ss[i,j] = ( ( ( ( first_expr[i,j] + second_expr[i,j] ) * EB[i] + ( 1 - EB[i] ) ) * third_expr[i,j] + \
                        fourth_expr[i,j] ) * EC[i] + ( 1 - EC[i] ) ) / denom[i,j]
#
        Factor_1n[i,j] = np.power ( np.cos ( alpha_1 * B1[j] ) * E1[i], enne/2 - 1 )  
        Factor_2n[i,j] = np.power ( np.cos ( alpha_2 * B1[j] ) * E1[i], enne/2 )  
        Factor_2np[i,j] = np.power ( np.cos ( alpha_2 * B1[j] ) * E1[i], -enne/2 )  
        Factor_1d[i,j] = 1 - E1[i] * np.cos ( alpha_1 * B1[j] )
        Factor_2d[i,j] = 1 - np.cos ( alpha_2 * B1[j] ) * E1[i]
        GRE_I[i,j] = np.sin ( alpha_1 * B1[j] ) * ( ( ( 1 - EA[i] ) + ( np.cos ( 0.5 * np.pi * B1[j] ) * mon_z_ss[i,j] * EA[i]) ) * Factor_1n[i,j] + \
                     ( 1 - E1[i] ) * ( ( 1 - Factor_1n[i,j] ) / Factor_1d[i,j] ) )
        GRE_II[i,j] = np.sin ( alpha_2 * B1[j] ) * ( ( mon_z_ss[i,j] - ( 1 - EC[i] ) ) / ( EC[i] * Factor_2n[i,j] ) - \
                      ( 1 - E1[i] ) * ( ( Factor_2n[i,j] - 1 ) / Factor_2d[i,j] ) )
        SA2RAGE[i,j] = GRE_I[i,j] / GRE_II[i,j]
        #SA2RAGE[i,j] = np.divide ( np.multiply ( GRE_I, GRE_II ), ( np.multiply ( GRE_I, GRE_I ) + \
        #               np.multiply ( GRE_II, GRE_II ) ) )
    plt.plot ( SA2RAGE[i,:],B1 )
plt.show()
#plt.plot ( SA2RAGE, T1, B1 )
#plt.show()

#SA2RAGEFil = data_dir + "/SA2Rage-B1"
#MMF = open (SA2RAGEFil, 'w' )
#for i in range(0, len(B1)):
#     s = str ( SA2RAGE[i] ) + "\t" + str ( B1[i] ) + "\n"
#     MMF.write ( s )
#MMF.close ( )


#c=np.append(a,np.zeros(0 if (len(b) - len(a))<0 else (len(b) - len(a))))*np.append(b,np.zeros(0 if (len(a) - len(b))<0 else (len(a) - len(b))))
