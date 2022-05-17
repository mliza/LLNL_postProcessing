#!/usr/local/bin/python3
import os 
import pickle 
# Import manual 
lsize = { 'l0': [ 0.1, 0.0005, -0.027, 0.1, 0.0005, 0.034 ], 
          'l1': [ 0.1, 0.0010, -0.027, 0.1, 0.0010, 0.034 ],
          'l2': [ 0.1, 0.0020, -0.027, 0.1, 0.0020, 0.034 ], 
          'l3': [ 0.1, 0.0030, -0.027, 0.1, 0.0030, 0.034 ],
          'l4': [ 0.1, 0.0050, -0.027, 0.1, 0.0050, 0.034 ],
          'l5': [ 0.13, 0.0010, -0.027, 0.13, 0.0010, 0.034 ],
          'l6': [ 0.13, 0.0020, -0.027, 0.13, 0.0020, 0.034 ], 
          'l7': [ 0.13, 0.0030, -0.027, 0.13, 0.0030, 0.034 ],
          'l8': [ 0.13, 0.0050, -0.027, 0.13, 0.0050, 0.034 ],
          'l9': [ 0.13, 0.0005, -0.027, 0.13, 0.0005, 0.034 ] }

psize = { 'p0':  [ 0.06, 0.0005, 0.003 ],  
          'p1':  [ 0.06, 0.0010, 0.003 ], 
          'p2':  [ 0.06, 0.0020, 0.003 ], 
          'p3':  [ 0.06, 0.0030, 0.003 ], 
          'p40': [ 0.101, 0.0005, 0.003 ], 
          'p4':  [ 0.101, 0.0010, 0.003 ], 
          'p5':  [ 0.101, 0.0020, 0.003 ], 
          'p6':  [ 0.101, 0.0030, 0.003 ], 
          'p7':  [ 0.12, 0.0005, 0.003 ], 
          'p8':  [ 0.12, 0.0010, 0.003 ], 
          'p9':  [ 0.12, 0.0020, 0.003 ], 
          'p90': [ 0.12, 0.0030, 0.003 ], 
          'p10': [ 0.12, 0.0005, -0.002 ], 
          'p11': [ 0.12, 0.0010, -0.002 ], 
          'p12': [ 0.12, 0.0020, -0.002 ], 
          'p14': [ 0.12, 0.0030, -0.002 ], 
          'p15': [ 0.12, 0.0005, 0.009 ], 
          'p16': [ 0.12, 0.0010, 0.009 ], 
          'p17': [ 0.12, 0.0020, 0.009 ], 
          'p18': [ 0.12, 0.0030, 0.009 ], 
          'p19': [ 0.115, -0.001, 0.003 ], 
          'p20': [ 0.145, 0.0005, 0.02 ], 
          'p21': [ 0.145, 0.0010, 0.02 ], 
          'p22': [ 0.145, 0.0020, 0.02 ], 
          'p23': [ 0.145, 0.0030, 0.02 ], 
          'p24': [ 0.145, 0.0005, -0.015 ], 
          'p25': [ 0.145, 0.0010, -0.015 ], 
          'p26': [ 0.145, 0.0020, -0.015 ], 
          'p27': [ 0.145, 0.0030, -0.015 ] } 

pickle_path = '/Users/martin/Documents/Research/UoA/Projects/LLNL/data/data_5/pickle' 
probe_points = os.path.join(pickle_path, 'probe_points.pickle') 
line_points = os.path.join(pickle_path, 'line_points.pickle') 
pickle_out_probe = open(probe_points, 'wb') 
pickle.dump(psize, pickle_out_probe)  
pickle_out_probe.close() 
pickle_out_line = open(line_points, 'wb') 
pickle.dump(lsize, pickle_out_line)  
pickle_out_line.close() 