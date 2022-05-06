#!/opt/homebrew/bin/python3
import os 
import pickle 
# Pickle path 
pickle_path = '/Users/martin/Documents/Research/UoA/Projects/LLNL/plate_data/data_7/pickle' 

# Import manual 
lsize = { 'l0': [ 0.09, 0.0, -0.015, 0.09, 0.05, -0.015 ], 
          'l1': [ 0.10, 0.0, -0.015, 0.10, 0.05, -0.015 ],
          'l2': [ 0.11, 0.0, -0.015, 0.11, 0.05, -0.015 ], 
          'l3': [ 0.12, 0.0, -0.015, 0.12, 0.05, -0.015 ],
          'l4': [ 0.13, 0.0, -0.015, 0.13, 0.05, -0.015 ],
          'l5': [ 0.14, 0.0, -0.015, 0.14, 0.05, -0.015 ],
          'l6': [ 0.15, 0.0, -0.015, 0.15, 0.05, -0.015 ] } 

'''
lsize = { 'l00' : [ 0.09, 0.0, -0.015, 0.09, 0.05, -0.015 ], 
          'l01' : [ 0.09, 0.0, -0.010, 0.09, 0.05, -0.010 ], 
          'l02' : [ 0.09, 0.0, -0.0085, 0.09, 0.05, -0.0085 ], 
          'l03' : [ 0.09, 0.0, 0.0085, 0.09, 0.05, 0.0085 ], 
          'l04' : [ 0.09, 0.0, 0.010, 0.09, 0.05, 0.010 ], 
          'l05' : [ 0.09, 0.0, 0.015, 0.09, 0.05, 0.015 ], 

          'l10' : [ 0.10, 0.0, -0.015, 0.10, 0.05, -0.015 ], 
          'l11' : [ 0.10, 0.0, -0.010, 0.10, 0.05, -0.010 ], 
          'l12' : [ 0.10, 0.0, -0.0085, 0.10, 0.05, -0.0085 ], 
          'l13' : [ 0.10, 0.0, 0.0085, 0.10, 0.05, 0.0085 ], 
          'l14' : [ 0.10, 0.0, 0.010, 0.10, 0.05, 0.010 ], 
          'l15' : [ 0.10, 0.0, 0.015, 0.10, 0.05, 0.015 ], 

          'l20' : [ 0.11, 0.0, -0.015, 0.11, 0.05, -0.015 ], 
          'l21' : [ 0.11, 0.0, -0.010, 0.11, 0.05, -0.010 ], 
          'l22' : [ 0.11, 0.0, -0.0085, 0.11, 0.05, -0.0085 ], 
          'l23' : [ 0.11, 0.0, 0.0085, 0.11, 0.05, 0.0085 ], 
          'l24' : [ 0.11, 0.0, 0.010, 0.11, 0.05, 0.010 ], 
          'l25' : [ 0.11, 0.0, 0.015, 0.11, 0.05, 0.015 ], 

          'l30' : [ 0.12, 0.0, -0.015, 0.12, 0.05, -0.015 ], 
          'l31' : [ 0.12, 0.0, -0.010, 0.12, 0.05, -0.010 ], 
          'l32' : [ 0.12, 0.0, -0.0085, 0.12, 0.05, -0.0085 ], 
          'l33' : [ 0.12, 0.0, 0.0085, 0.12, 0.05, 0.0085 ], 
          'l34' : [ 0.12, 0.0, 0.010, 0.12, 0.05, 0.010 ], 
          'l35' : [ 0.12, 0.0, 0.015, 0.12, 0.05, 0.015 ], 

          'l40' : [ 0.13, 0.0, -0.015, 0.13, 0.05, -0.015 ], 
          'l41' : [ 0.13, 0.0, -0.010, 0.13, 0.05, -0.010 ], 
          'l42' : [ 0.13, 0.0, -0.0085, 0.13, 0.05, -0.0085 ], 
          'l43' : [ 0.13, 0.0, 0.0085, 0.13, 0.05, 0.0085 ], 
          'l44' : [ 0.13, 0.0, 0.010, 0.13, 0.05, 0.010 ], 
          'l45' : [ 0.13, 0.0, 0.015, 0.13, 0.05, 0.015 ], 

          'l50' : [ 0.14, 0.0, -0.015, 0.14, 0.05, -0.015 ], 
          'l51' : [ 0.14, 0.0, -0.010, 0.14, 0.05, -0.010 ], 
          'l52' : [ 0.14, 0.0, -0.0085, 0.14, 0.05, -0.0085 ], 
          'l53' : [ 0.14, 0.0, 0.0085, 0.14, 0.05, 0.0085 ], 
          'l54' : [ 0.14, 0.0, 0.010, 0.14, 0.05, 0.010 ], 
          'l55' : [ 0.14, 0.0, 0.015, 0.14, 0.05, 0.015 ], 

          'l60' : [ 0.15, 0.0, -0.015, 0.15, 0.05, -0.015 ], 
          'l61' : [ 0.15, 0.0, -0.010, 0.15, 0.05, -0.010 ], 
          'l62' : [ 0.15, 0.0, -0.0085, 0.15, 0.05, -0.0085 ], 
          'l63' : [ 0.15, 0.0, 0.0085, 0.15, 0.05, 0.0085 ], 
          'l64' : [ 0.15, 0.0, 0.010, 0.15, 0.05, 0.010 ], 
          'l65' : [ 0.15, 0.0, 0.015, 0.15, 0.05, 0.015 ] } 
'''
          

psize = { 'p00': [ 0.09, 0.00025, 0.0085 ],  
          'p01': [ 0.09, 0.00050, 0.0085 ], 
          'p02': [ 0.09, 0.00075, 0.0085 ], 
          'p03': [ 0.09, 0.00100, 0.0085 ], 
          'p04': [ 0.09, 0.00200, 0.0085 ], 
          'p05': [ 0.09, 0.00300, 0.0085 ], 
          'p06': [ 0.09, 0.00400, 0.0085 ], 
          'p07': [ 0.09, 0.00500, 0.0085 ], 

          'p10': [ 0.10, 0.00025, 0.0085 ], 
          'p11': [ 0.10, 0.00050, 0.0085 ], 
          'p12': [ 0.10, 0.00075, 0.0085 ], 
          'p13': [ 0.10, 0.00100, 0.0085 ], 
          'p14': [ 0.10, 0.00200, 0.0085 ], 
          'p15': [ 0.10, 0.00300, 0.0085 ], 
          'p16': [ 0.10, 0.00400, 0.0085 ], 
          'p17': [ 0.10, 0.00500, 0.0085 ], 

          'p20': [ 0.11, 0.00025, 0.0085 ], 
          'p21': [ 0.11, 0.00050, 0.0085 ], 
          'p22': [ 0.11, 0.00075, 0.0085 ], 
          'p23': [ 0.11, 0.00100, 0.0085 ], 
          'p24': [ 0.11, 0.00200, 0.0085 ], 
          'p25': [ 0.11, 0.00300, 0.0085 ], 
          'p26': [ 0.11, 0.00400, 0.0085 ], 
          'p27': [ 0.11, 0.00500, 0.0085 ], 

          'p30': [ 0.12, 0.00025, 0.0085 ], 
          'p31': [ 0.12, 0.00050, 0.0085 ], 
          'p32': [ 0.12, 0.00075, 0.0085 ], 
          'p33': [ 0.12, 0.00100, 0.0085 ], 
          'p34': [ 0.12, 0.00200, 0.0085 ], 
          'p35': [ 0.12, 0.00300, 0.0085 ], 
          'p36': [ 0.12, 0.00400, 0.0085 ], 
          'p37': [ 0.12, 0.00500, 0.0085 ], 

          'p40': [ 0.13, 0.00025, 0.0085 ], 
          'p41': [ 0.13, 0.00050, 0.0085 ], 
          'p42': [ 0.13, 0.00075, 0.0085 ], 
          'p43': [ 0.13, 0.00100, 0.0085 ], 
          'p44': [ 0.13, 0.00200, 0.0085 ], 
          'p45': [ 0.13, 0.00300, 0.0085 ], 
          'p46': [ 0.13, 0.00400, 0.0085 ], 
          'p47': [ 0.13, 0.00500, 0.0085 ], 

          'p50': [ 0.14, 0.00025, 0.0085 ], 
          'p51': [ 0.14, 0.00050, 0.0085 ], 
          'p52': [ 0.14, 0.00075, 0.0085 ], 
          'p53': [ 0.14, 0.00100, 0.0085 ], 
          'p54': [ 0.14, 0.00200, 0.0085 ], 
          'p55': [ 0.14, 0.00300, 0.0085 ], 
          'p56': [ 0.14, 0.00400, 0.0085 ], 
          'p57': [ 0.14, 0.00500, 0.0085 ], 

          'p60': [ 0.15, 0.00025, 0.0085 ], 
          'p61': [ 0.15, 0.00050, 0.0085 ], 
          'p62': [ 0.15, 0.00075, 0.0085 ], 
          'p63': [ 0.15, 0.00100, 0.0085 ], 
          'p64': [ 0.15, 0.00200, 0.0085 ], 
          'p65': [ 0.15, 0.00300, 0.0085 ], 
          'p66': [ 0.15, 0.00400, 0.0085 ], 
          'p67': [ 0.15, 0.00500, 0.0085 ] } 

probe_points = os.path.join(pickle_path, 'probe_points.pickle') 
line_points  = os.path.join(pickle_path, 'line_points.pickle') 
pickle_out_probe = open(probe_points, 'wb') 
pickle.dump(psize, pickle_out_probe)  
pickle_out_probe.close() 
pickle_out_line = open(line_points, 'wb') 
pickle.dump(lsize, pickle_out_line)  
pickle_out_line.close() 
