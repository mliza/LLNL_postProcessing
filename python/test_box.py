#!/opt/homebrew/bin/python3
import numpy as np 
import matplotlib.pyplot as plt 
import IPython 
import sys 
import os 
scripts_path   = os.environ.get('SCRIPTS')
python_scripts = os.path.join(scripts_path, 'Python')
#sys.path.insert(1, python_scripts)
sys.path.append(python_scripts)
sys.path.append('../fortran_modules')
# Helper class 
import helper_class as helper 
import box_class as box  
# Fortran subroutines 
import f_mapping
import f_gridReader
import f_scalarReader 
import f_vectorReader

# User Inputs 
data_path    = '../../plate_data/data_11'
pickle_path  = os.path.join(data_path, 'pickle')
temp_path    = os.path.join(data_path, 'temp_data')  
box_path     = os.path.join(data_path, 'BOX')  
saving_path  = '/Users/martin/Desktop/results'
nx           = 1439
ny           = 85
nz           = 638 
time_step    = '0900000'
fortran_flag = False  
mapping_flag = False 
writing_flag = False 
working_flag = True 
scalar_in    = [ 'T', 'RHO', 'P',
                 'RHOE', 'GRADRHOMAG', 
                 'GRADV_11', 'GRADV_12', 'GRADV_13',
                 'GRADV_21', 'GRADV_22', 'GRADV_23',
                 'GRADV_31', 'GRADV_32', 'GRADV_33' ]

# Loading my classes 
helper = helper.Helper()
box    = box.Box(nx=nx, ny=ny, nz=nz)

# Use fortran subroutines 
if fortran_flag:
    n_max = nx * ny * nz
    f_mapping.mapping(nx, ny, nz, temp_path)
    f_gridReader.grid_reader(n_max, box_path, temp_path, 'U') 
    f_vectorReader.vector_reader(n_max, box_path, temp_path, 'U', time_step) 
    for i in scalar_in:
        f_scalarReader.scalar_reader(n_max, box_path, 
                                     temp_path, i, time_step)

# Opens mapping fortran output and saves it as a pickle file
if mapping_flag:
    mapping_file_in = os.path.join(temp_path, 'mappingVector.dat') 
    mapping         = box.mapping_reader(mapping_data_in=mapping_file_in, 
                                         pickle_path=pickle_path) 

# Stores data as a 1D and 3D pickle dictionary
if writing_flag:
    var_in = scalar_in + ['X', 'Y', 'Z', 'Ux', 'Uy', 'Uz']
    var_in.sort() 
    # Dictionaries 
    dict_1D = { } 
    dict_3D = { }
    mapping = helper.pickle_manager(pickle_name_file='mapping', 
                                    pickle_path=pickle_path)
    for i in var_in: 
        dict_1D[i] = helper.fortran_data_loader(variable_in=f'{i}.dat',  
                                                abs_path_in=temp_path) 
        dict_3D[i] = box.split_plot3D(array_1D=dict_1D[i], mapping=mapping)
    # Saving 1D and 3D arrays 
    helper.pickle_manager(pickle_name_file='dict_1D', pickle_path=pickle_path,
                          data_to_save=dict_1D)
    helper.pickle_manager(pickle_name_file='dict_3D', pickle_path=pickle_path,
                          data_to_save=dict_3D)

# Testing and playing around scripts 
if working_flag:
    # Loading dictionaries 
    data_in1D = helper.pickle_manager(pickle_name_file='dict_1D', 
                                      pickle_path=pickle_path)
    data_in3D = helper.pickle_manager(pickle_name_file='dict_3D', 
                                      pickle_path=pickle_path)
    mapping   = helper.pickle_manager(pickle_name_file='mapping', 
                                      pickle_path=pickle_path)
    data_keys = list(data_in1D.keys()) 

    grad      = box.gradient_fields(data_in3D) 

# Loading data 
    box.plot_contour(data_in3D, grid_x='X', grid_y='Z', field='RHO', 
                     slice_cut=20, slice_direction='Y', 
                     levels=500, saving_path=saving_path) 
    box.plot_contour(data_in3D, grid_x='X', grid_y='Z', field='T', 
                     slice_cut=20, slice_direction='Y', 
                     levels=500, saving_path=saving_path) 
    box.plot_contour(data_in3D, grid_x='X', grid_y='Z', field='Ux', 
                     slice_cut=20, slice_direction='Y', 
                     levels=500, saving_path=saving_path) 

    IPython.embed(colors='Linux') 


