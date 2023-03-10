#!/opt/homebrew/bin/python3
import numpy as np 
import pickle 
import os 
import IPython 
import math 
import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec 
import seaborn as sb 
# My files 
import base_analysis
import probe 
import line 

# Configuration Parameters 
line_flag             = True   
probe_flag            = False  
new_data_flag         = False   
scatter_probe_flag    = False    
sub_sampling_flag     = False 
probe_sampling_rate   = 1 
probe_correlation_lag = 40
line_correlation_lag  = 50 
time_sub_sampling     = 45 #keep all positions 
spatial_sub_sampling  = 10 #keep all times 
temperature_inf       = 1200  #216 #freestream temperature
velocity_inf          = 2500 #3000 #freestream velocity  

# Paths 
pickle_path    = '/Users/martin/Documents/Research/UoA/Projects/LLNL/plate_data/data_7/pickle' 
save_path      = '/Users/martin/Documents/Research/UoA/Projects/LLNL/plate_data/data_7/results'
probe_save     = os.path.join(save_path, 'probe', 'total')
probe_boxcar   = os.path.join(save_path, 'probe', 'boxcar')
probe_scatter  = os.path.join(save_path, 'probe', 'scatter')
probe_legendre = os.path.join(save_path, 'probe', 'legendre') 
line_save      = os.path.join(save_path, 'line')
line_correlation_save = os.path.join(line_save, 'correlation') 
line_boxcar    = os.path.join(line_save, 'boxcar')
line_legendre  = os.path.join(line_save, 'legendre') 
temporal_line_legendre = os.path.join(line_legendre, 'temporal') 
spatial_line_legendre  = os.path.join(line_legendre, 'spatial') 
temporal_line_boxcar   = os.path.join(line_boxcar, 'temporal') 
spatial_line_boxcar    = os.path.join(line_boxcar, 'spatial') 

# Loading class's instances  
base  = base_analysis.Base_Analysis(pickle_path)
probe = probe.Probe(pickle_path, sampling_rate=probe_sampling_rate) 
line  = line.Line(pickle_path, sampling_rate=probe_sampling_rate) 

# Keys 
probe_keys = list(probe.location.keys()) 
line_keys  = list(line.location.keys()) 
variables  = ['U-X', 'U-Z', 'U-Y', 'P', 'T', 'RHO', 'DIL', 'P-DIL', 'MU']  

# Add new data to structures if this is on 
if new_data_flag:
# Add new data probe  
    for i in probe_keys: 
        mu           = probe.sutherland_law(probe.working_data[i]['T']) 
        pressure     = probe.working_data[i]['P'] 
        dilatation   = probe.working_data[i]['DIL'] 
        rho          = probe.working_data[i]['RHO'] 
        pressure_dil = pressure * dilatation 
        nu           = mu / rho
        probe.add_new_variable(i, 'P-DIL', pressure_dil, pickle_path, 'new_probe_data') 
        probe.add_new_variable(i, 'MU', mu, pickle_path, 'new_probe_data') 
        probe.add_new_variable(i, 'NU', nu, pickle_path, 'new_probe_data') 
# Add new data line 
    for i in line_keys: 
        mu           = line.sutherland_law(line.working_data[i]['T']) 
        pressure     = line.working_data[i]['P'] 
        dilatation   = line.working_data[i]['DIL'] 
        rho          = line.working_data[i]['RHO'] 
        pressure_dil = pressure * dilatation 
        nu           = mu / rho
        line.add_new_variable(i, 'P-DIL', pressure_dil, pickle_path, 'new_line_data') 
        line.add_new_variable(i, 'MU', mu, pickle_path, 'new_line_data') 
        line.add_new_variable(i, 'NU', nu, pickle_path, 'new_line_data') 

if probe_flag:
    for i in probe_keys:
        print(i) 
    # Plot Scatter 
        radius_dict = probe.x_axis(i, sampling_flag=sub_sampling_flag) 
        probe_radius = radius_dict['x_axis'] 
        # Constant length scale (U-X)
        const_cutoff_k  = probe.const_cutoff_k(i, probe_radius, 
                correlation_lag=probe_correlation_lag)  
        if scatter_probe_flag:
            probe.plot_scatter(i, 'P', 'RHO', probe_radius, const_cutoff_k,  
                               correlation_lag=probe_correlation_lag,
                               saving_path=probe_scatter) 

            probe.plot_scatter(i, 'P', 'T', probe_radius, const_cutoff_k,  
                               correlation_lag=probe_correlation_lag,
                               saving_path=probe_scatter) 

            probe.plot_scatter(i, 'RHO', 'T', probe_radius, const_cutoff_k, 
                               correlation_lag=probe_correlation_lag,
                               saving_path=probe_scatter) 

            probe.plot_scatter(i, 'P', 'DIL', probe_radius, const_cutoff_k, 
                               correlation_lag=probe_correlation_lag,
                               saving_path=probe_scatter) 

            probe.plot_scatter(i, 'T', 'DIL', probe_radius, const_cutoff_k, 
                               correlation_lag=probe_correlation_lag,
                               saving_path=probe_scatter) 

            probe.plot_scatter(i, 'RHO', 'DIL', probe_radius, const_cutoff_k,  
                               correlation_lag=probe_correlation_lag,
                               saving_path=probe_scatter) 

            probe.plot_scatter(i, 'RHO', 'P-DIL', probe_radius, const_cutoff_k,  
                               correlation_lag=probe_correlation_lag,
                               saving_path=probe_scatter) 

            probe.plot_scatter(i, 'T', 'P-DIL', probe_radius, const_cutoff_k,  
                               correlation_lag=probe_correlation_lag,
                               saving_path=probe_scatter) 

        for j in variables:  
            print(i, j)  
        # General Functions 
            variable         = probe.working_data[i][j] 
            variable         = probe.sub_sampling(variable) 
            dict_out         = probe.data_process(variable, probe_radius, 
                               auto_correlation_len=probe_correlation_lag)
            correlation      = dict_out['correlation']
            pwr_spectral     = dict_out['spe']
            length_scales    = probe.length_scales(correlation['correlation_radius'],
                                correlation['correlation'], dict_out['fluctuation'],
                                dict_out['spe'])
            boxcar_dict      = probe.boxcar_filter(probe_radius, 
                               variable, const_cutoff_k) 
            legendre_dict    = probe.legendre_interpolation(boxcar_dict) 
            moments_str      = probe.statistical_moments_str(boxcar_dict) 

            # Shifting Factors 
            if (j == 'RHO'):
                shifting_factor = 1.6 
            elif (j == 'P'):
                shifting_factor = 1e9 
            elif (j == 'DIL') :
                shifting_factor = 1e12 
            elif (j == 'RHOE'):
                shifting_factor = 1e10 
            elif (j == 'VORTMAG'):
                shifting_factor = 1e12 
            elif (j == 'P-DIL'):
                shifting_factor = 1e21 
            elif (j == 'RHO-DIL'):
                shifting_factor = 1e10
            else: 
                shifting_factor = 1e7 

            # Plots  
            probe.plot_boxcar(i,j, boxcar_dict, moments_str, 
                        saving_path=probe_boxcar) 
            probe.plot_legendre(i, j, boxcar_dict, legendre_dict,
                                saving_path=probe_legendre) 
            probe.plot_results(i,j, probe_radius, variable, pwr_spectral,
                    correlation, length_scales, moments_str,
                  inertial_shifting_factor=shifting_factor,
                  saving_path=probe_save) 

# Line and crunched data  
temporal_dict = { }
spatial_dict  = { }
temporal_raw_dict = { }
spatial_raw_dict  = { }  
if line_flag:
    # Crunching for data 
    for i in line_keys: 
        temporal_dict[i]     = { }
        spatial_dict[i]      = { }  
        temporal_raw_dict[i] = { }
        spatial_raw_dict[i]  = { }  
        for j in variables:
            temp_dict = line.temporal_data(i,j, n_points=spatial_sub_sampling, 
                                    auto_correlation_len=line_correlation_lag) 
            spat_dict = line.spatial_data(i,j, n_points=time_sub_sampling, axis='y', 
                                    auto_correlation_len=40) 
            # Not crunched data 
            temporal_raw_dict[i][j] = temp_dict
            spatial_raw_dict[i][j]  = spat_dict
            # Data Crunched  
            temporal_dict[i][j] = line.data_cruncher(temp_dict) 
            spatial_dict[i][j]  = line.data_cruncher(spat_dict) 
        # Calculate absolute cutoff scales in wave space 
        # and append to dictionaries 
        temporal_cutoff_k = line.const_cutoff_k(temporal_dict[i]['U-X']) 
        spatial_cutoff_k  = line.const_cutoff_k(spatial_dict[i]['U-Z']) 
        for k in variables:
            #temporal_dict[i][k]['window_size'] = int(np.round(temporal_cutoff_k)) 
            #spatial_dict[i][k]['window_size']  = int(np.round(spatial_cutoff_k)) 
            # Calculate and storage BL properties (only on the spatial dictionary)  
            if k == 'U-X':
                spatial_dict[i][k]['BL'] = line.boundary_layer_thickness(
                                           spatial_dict[i], k, 
                                           freestream_condition=velocity_inf) 
            if k == 'T':
                spatial_dict[i][k]['BL'] = line.boundary_layer_thickness(
                                           spatial_dict[i], k,
                                           freestream_condition=temperature_inf) 
    # Plotting BL thickness  
    line.plot_BL(spatial_dict, velocity_inf, temperature_inf, saving_path=save_path)  
    # Filters and Plots 
    for i in line_keys: 
        line.plot_wall_function(i, spatial_dict[i], saving_path=save_path) 
        for j in variables:
            print(i, j, 'filters') 
            # Temporal Data
            IPython.embed(colors='Linux') 
            temporal_filters = line.filters(temporal_raw_dict[i][j], 
                                        temporal_dict[i][j]['window_size'])
            temporal_dict[i][j]['legendre'] = temporal_filters['legendre'] 
            temporal_dict[i][j]['boxcar']   = temporal_filters['boxcar'] 
            temporal_dict[i][j]['length_scales'] = line.length_scales(
                    temporal_dict[i][j]['correlation']['correlation_radius'],
                    temporal_dict[i][j]['correlation']['correlation'],
                    temporal_dict[i][j]['fluctuation'],
                    temporal_dict[i][j]['spe'])
            # Spatial Data
            spatial_filters  = line.filters(spatial_raw_dict[i][j], 
                                        spatial_dict[i][j]['window_size'])
            spatial_dict[i][j]['legendre'] = spatial_filters['legendre'] 
            spatial_dict[i][j]['boxcar']   = spatial_filters['boxcar'] 
            spatial_dict[i][j]['length_scales'] = line.length_scales(
                    spatial_dict[i][j]['correlation']['correlation_radius'],
                    spatial_dict[i][j]['correlation']['correlation'],
                    spatial_dict[i][j]['fluctuation'],
                    spatial_dict[i][j]['spe'])

            # Plots  
            line.plot_correlation_spe(temporal_dict[i][j], 
                       spatial_dict[i][j], dataset=i, variable=j,
                       time_sub_sampling=time_sub_sampling,
                       spatial_sub_sampling=spatial_sub_sampling,
                       saving_path = line_correlation_save) 

            # Spatial 
            spatial_moments_str = line.statistical_moments_str(
                                    spatial_dict[i][j]['boxcar']) 
            line.plot_boxcar(i,j, spatial_dict[i][j]['boxcar'],  
                        moments_str_dict=spatial_moments_str, 
                        saving_path=spatial_line_boxcar) 
            line.plot_legendre(i, j, spatial_dict[i][j]['boxcar'], 
                                     spatial_dict[i][j]['legendre'],
                                saving_path=spatial_line_legendre) 
            # Temporal 
            temporal_moments_str = line.statistical_moments_str(
                                    temporal_dict[i][j]['boxcar']) 
            line.plot_boxcar(i,j, temporal_dict[i][j]['boxcar'],  
                        moments_str_dict=temporal_moments_str, 
                        saving_path=temporal_line_boxcar) 
            line.plot_legendre(i, j, temporal_dict[i][j]['boxcar'], 
                                     temporal_dict[i][j]['legendre'],
                                saving_path=temporal_line_legendre) 
