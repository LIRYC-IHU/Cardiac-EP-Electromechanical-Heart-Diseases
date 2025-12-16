#%%
import numpy as np
vector=np.arange(1,4)
print(vector)

tmp=np.arange(1,10)
matrix=tmp.reshape(3,3)
print("matrix")

#%%
import numpy as np
import nibabel as nib

# ouvrir 3D Slicer puis aller dans l'onglet download sample dataset et télécharger le jeux de données CTChest
# aller dans l'outil Save puis suavegarder le volume en nifti

nifti=nib.load('/home/vozenne/Documents/CTChest.nii.gz')

volume=nifti.get_fdata()

print(np.shape(volume))

slice=volume[:,:,65]
slice_for_threshold=slice
# %%
import matplotlib.pyplot as plt
plt.figure(1)
plt.subplot(121)
plt.imshow(slice, cmap='gray')

#%%
print(np.min(slice_for_threshold.flatten()))
print(np.max(slice_for_threshold.flatten()))

# Valeur seuil
seuil = -500

# Remplacer les éléments inférieurs à 5 par 99
slice_for_threshold[slice_for_threshold < seuil] = 0
plt.subplot(122)
plt.imshow(slice_for_threshold, cmap='gray')

# %%
import numpy as np
A=np.matrix([[3, 3, 2, 1, 0],[0,0,1,3,1],[3,1,2,2,3], 
             [2,0,0,2,2], [2,0,0,0,1]])

K=np.matrix([[2,1,0],[0,2,2],[2,1,0]])
print("A =", A) 
print("K =", K) 

print("A[0] =", A[0])      # 1st row
print("A[1] =", A[1])      # 2nd row

#print(K,A)
# %%
dimAx, dimAy=np.shape(A)
dimKx, dimKy=np.shape(K)

S=np.zeros((dimAx-2,dimAy-2))
print(np.shape(S))
for x in range (1,dimAx-1,1):
    for y in range (1,dimAy-1,1):
        #print(x,y)
        for kx in range (-1,2,1):
            for ky in range (-1,2,1):
            
                index_x=x+kx
                index_y=y+ky
                print(x,y, " index K ", -kx+1,-ky+1," index A " , index_x,index_y, ": ", A[index_x,index_y] ," * ", K[-kx+1, -ky+1], )
                S[x-1,y-1]=S[x-1,y-1]+A[index_x,index_y]*K[-kx+1, -ky+1]


print(S)
# %%
