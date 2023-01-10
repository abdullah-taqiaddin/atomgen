
#blender's python api library 
import bpy

import math

def create_atom(num_orbits, electrons_per_orbit):

    nucleus_radius = 0.5
    bpy.ops.mesh.primitive_circle_add(radius=nucleus_radius, fill_type='NGON', enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

    nucleus = bpy.context.active_object
    nucleus.name = "Nucleus"

	
    for i in range(num_orbits):
		#0.7 = magic number
        orbit_radius = 0.7 + 0.2 * i
        
        # Create orbit curve
        bpy.ops.curve.primitive_bezier_circle_add(radius=orbit_radius)
        orbit = bpy.context.active_object
        orbit.name = f"Orbit {i+1}"
        
        # Create electrons for current orbit
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.05)
        electron = bpy.context.active_object
        electron.name = f"Electron {i+1}"
        
        array_mod = electron.modifiers.new(type="ARRAY", name="Array")
        array_mod.count = electrons_per_orbit[i]
        bpy.context.object.modifiers["Array"].use_constant_offset = True
		

        # Add curve modifier to electron
        curve_mod = electron.modifiers.new(type="CURVE", name="Curve")
        curve_mod.object = orbit


#PARAMS: create_atom(number of orbit,a list of electrons for each orbit)
#TODO: add number of protons and neutrons
create_atom(3, [6, 8,3])
