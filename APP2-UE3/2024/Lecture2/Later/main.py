
#%%
import pyvista as pv
import numpy as np

atria = pv.read('/home/vozenne/Dev/Marta/PVI_gap_quantification/data/output_example/mesh_clipped.vtk')

sphere=pv.read('/home/vozenne/Dev/Cardiac-EP-Electromechanical-Heart-Diseases/APP2-UE3/2024/Lecture2/Data/sphere.vtk')

p = pv.Plotter()
p.add_mesh(atria, show_edges =True)
p.add_mesh(sphere, show_edges =True)

print(np.shape(atria.points))
print(np.shape(sphere.points))

p.show()
#%%
atria["distances"] = np.empty(atria.n_points)
atria["distances"]= np.ones(atria.n_points)


for index_atria in range(0,atria.n_points):

    atria_xyz_coordinates=atria.points[index_atria,:]

    min=9999
    for index_sphere in range(0,sphere.n_points):
        sphere_xyz_coordinates=sphere.points[index_sphere,:]
        dist = np.linalg.norm(atria_xyz_coordinates-sphere_xyz_coordinates)
        if (dist<min):
            min=dist
    atria["distances"][index_atria]=min   

pp = pv.Plotter()
pp.add_mesh(sphere, show_edges =True)
pp.add_mesh(atria, scalars="distances", smooth_shading=True)
pp.show()        
#%%






import numpy as np
import pyvista as pv
from pyvista import examples

mesh = examples.download_bunny_coarse()
print(mesh)
mesh = examples.load_hexbeam()
print(mesh)

np.shape(mesh.points)
np.shape(mesh.cells)

A=np.linspace(1,99,99)

mesh.point_data['useless_information']=A
mesh.plot(scalars='useless_information',  show_edges=True)
#%%
# 
#from __future__ import annotations
import numpy as np
#import trame
import pyvista as pv


def hill(seed):
    """A helper to make a random surface."""
    mesh = pv.ParametricRandomHills(numberofhills=2, xvariancescalefactor=100, yvariancescalefactor=0.1, hillamplitude=2)
    mesh.rotate_z(-10, inplace=True)  # give the surfaces some tilt

    return mesh

#%%

cylinder = pv.Cylinder(

    center=[1, 2, 3], direction=[1, 0, 0], radius=2, height=20

)

#h0=pv.read('/home/vozenne/Dev/Marta/PVI_gap_quantification/data/output_example/cylinder.vtk')


sphere = pv.Sphere(theta_resolution=100,  phi_resolution=100)


np.shape(cylinder.points)
extracted = cylinder.extract_points(cylinder.points[:,2]>0

    
)

extracted.clear_data()  # clear for plotting

#extracted.plot()

surf = extracted.delaunay_2d(progress_bar=True)

#volume = cylinder.delaunay_3d(progress_bar=True)
p = pv.Plotter()
p.add_mesh(extracted, show_edges =True)
p.add_mesh(surf, show_edges =True)
p.show()

#%%

h0 = pv.read('/home/vozenne/Dev/Marta/PVI_gap_quantification/data/output_example/mesh_clipped.vtk')

h1 = hill(20)
# Shift one surface
h1.points[:, -1] -= 20
h1 = h1.elevation()

p = pv.Plotter()
p.add_mesh(h0, show_edges =True, smooth_shading=True, opacity=0.5)
p.add_mesh(h1, show_edges =True, smooth_shading=True)
#p.add_mesh(cylinder, color='blue',show_edges =True, smooth_shading=True)
#p.add_mesh(surf, color='blue',show_edges =True, smooth_shading=True)
p.show_grid()
p.show()
quit()
#%%
h0n = h0.compute_normals(point_normals=True, cell_normals=False, auto_orient_normals=True)
# ici on créer un nouveau vecteur qui a exactement le même nombre de points
h0n["distances"] = np.empty(h0.n_points)
for i in range(h0n.n_points):
    p = h0n.points[i]
    vec = h0n["Normals"][i] * h0n.length
    p0 = p - vec
    p1 = p + vec
    ip, ic = h1.ray_trace(p0, p1, first_point=True)
    dist = np.sqrt(np.sum((ip - p) ** 2))
    h0n["distances"][i] = dist

# Replace zeros with nans
mask = h0n["distances"] == 0
h0n["distances"][mask] = np.nan
np.nanmean(h0n["distances"])

p = pv.Plotter()
p.add_mesh(h0n, scalars="distances")
p.add_mesh(h1, color=True,  opacity=1)
p.show()
# %%


from scipy.spatial import KDTree
tree = KDTree(h1.points)
d_kdtree, idx = tree.query(h0.points)
h0["distances"] = d_kdtree
np.mean(d_kdtree)
p = pv.Plotter()
p.add_mesh(h0, scalars="distances", smooth_shading=True)
p.add_mesh(h1, color=True, opacity=0.75, smooth_shading=True)
p.show()