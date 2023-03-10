#!/opt/homebrew/bin/python3
'''
    Date:   09/19/2022
    Author: Martin E. Liza
    File:   box_plots.py
    Def:

    Author		Date		Revision
    ----------------------------------------------------
    Martin E. Liza	09/19/2022	Initial version.
'''
import numpy as np
import matplotlib.pyplot as plt 
import sys 
import os 
scripts_path   = os.environ.get('SCRIPTS')
python_scripts = os.path.join(scripts_path, 'Python') 
sys.path.append(python_scripts)
import helper_class as helper 

# Plot energy cascade 
def energy_cascade(energy_cascade, title_str, y_plus_str='y', 
                   p_factor=-5/3, shifting_factor=9E11, 
                   saving_path=None, fig_name=None):
    wave_vector = np.array(range(10, 
                          int(np.floor(2 * len(energy_cascade)) / 15))) 
    plt.title(title_str)
    plt.loglog(energy_cascade, 'o-', markerfacecolor='lightgray', 
               linewidth=3, color='k', label=y_plus_str) 
    plt.legend() 
    slope = shifting_factor* wave_vector ** p_factor 
    plt.plot(wave_vector, slope, '--', linewidth='2.5') 
    plt.grid('-.')
    plt.xlim(left=0.9)
    plt.ylabel('$E(\kappa)$')
    plt.xlabel('$\kappa\;\;[1/m]$') 
    if saving_path == None:
        plt.show()

    if saving_path != None:
        plt.tight_layout()
        if fig_name == None:
            plt.savefig(f'{saving_path}/energy_spectrum.png', dpi=300) 
        if fig_name != None:
            plt.savefig(f'{saving_path}/{fig_name}.png', dpi=300) 
        plt.close() 

# Plot correlation 
def correlation(correlation_dict, correlation_function, title_str,
                saving_path=None):
    plt.plot(correlation_dict['radius'], correlation_dict['norm_correlation'], 
             'o-', markerfacecolor='lightgray', linewidth='3', color='k') 
    # Transversal 
    if correlation_function == 'g':
        correlation_str = f'$L_{{22}}$ = {correlation_dict["integral"]:.3}\n$\lambda_{{g}}$ = {correlation_dict["taylor"]:.3}'
        saving_name     = 'transversal'

    # Longitudinal 
    if correlation_function == 'f':
        correlation_str = f'$L_{{11}}$ = {correlation_dict["integral"]:.3}\n$\lambda_{{f}}$ = {correlation_dict["taylor"]:.3}'
        saving_name     = 'longitudinal'

    plt.text(correlation_dict['radius'][-1], 1, correlation_str, 
             horizontalalignment='right', verticalalignment='top', 
             bbox=dict(facecolor='white', edgecolor='lightgray',
                                      boxstyle='round,pad=0.2'))
    plt.title(title_str)
    plt.xlabel('$radius\;\;[m]$')
    plt.ylabel('$correlation\;\;[\;]$')
    plt.grid('-.') 
    if saving_path == None:
        plt.show()

    if saving_path != None:
        plt.tight_layout()
        plt.savefig(f'{saving_path}/{saving_name}_correlation.png', dpi=300) 
        plt.close() 

# Plot y_plus 
def y_plus(y_plus, plus_field, plus_field_str, title, 
          saving_path=None, fig_name=None):
    plt.plot(y_plus, plus_field, 'o-', markerfacecolor='lightgray',
                   linewidth='3', color='k')
    plt.title(title)
    plt.grid('-.')
    plt.xscale('log')
    plt.xlabel('$y^+$')
    plt.ylabel(f'${plus_field_str}$')
    if saving_path == None:
        plt.show() 
    if saving_path != None:
        plt.tight_layout()
        if fig_name == None: 
            plt.savefig(os.path.join(saving_path, 'field_plus.png'), dpi=300) 
        if fig_name != None:
            plt.savefig(os.path.join(saving_path, f'{fig_name}.png'), dpi=300) 
        plt.close() 

# Plot Boundary Layers 
def boundary_layers(mean_velocity_thickness, mean_temperature_thickness,
                    mean_x, saving_path=None):
    # Loading variables 
    helper_scripts  = helper.Helper()
    n_box           = 50 
    mean_temperature_thickness *= 10**3
    mean_velocity_thickness    *= 10**3
    mean_x                     *= 10**2
    v_color         = 'mediumturquoise' 
    t_color         = 'darkorange'
    temp_smooth     = helper_scripts.smoothing_function(mean_temperature_thickness, n_box) 
    vel_smooth      = helper_scripts.smoothing_function(mean_velocity_thickness, n_box) 
    n_box           /= 2
    n_box           = int(n_box) 

    # Plot thickness 
    plt.plot(mean_x, mean_velocity_thickness, 'o', markersize=3,
            markerfacecolor='lightgrey', markeredgecolor='k') 
    plt.plot(mean_x[n_box:-n_box], vel_smooth[n_box:-n_box], color=v_color, 
             linestyle='-', linewidth=1.5, label='$U_x$')
    plt.plot(mean_x, mean_temperature_thickness, 'o', markersize=3, 
            markerfacecolor='lightgrey', markeredgecolor='k')
    plt.plot(mean_x[n_box:-n_box], temp_smooth[n_box:-n_box], color=t_color, 
             linestyle='-', linewidth=1.5, label='$T$') 
    plt.legend()
    plt.ylabel('y-axis [mm]')
    plt.xlabel('x-axis [cm]')
    plt.grid('-.') 
    
    if saving_path == None:
        plt.show() 
    if saving_path != None:
        plt.tight_layout()
        plt.savefig(f'{saving_path}/boundary_layers.png', dpi=300)
        plt.close() 
