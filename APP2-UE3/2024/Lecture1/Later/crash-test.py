#%%
import pyvista as pv
#%%
import numpy as np

# let's define first a simple matrix
M=np.linspace(1, 9, num=9)
N=M.reshape((3, 3))

print(N)
print(N.flatten())

print(N.flatten()[6])
#%%

# find the function 6=ind=f(x,y) that give the index for x,y location in the matrix

# find the function 6=ind=g(x,y,z) that give the index for x,y,z location in the matrix


print("N[0] =", N[0])
print("N[1] =", N[1])
print("N[2] =", N[2])

O=np.linspace(1, 27, num=27)
P=O.reshape((3, 3, 3))
Q=np.zeros((3,3,3))




for y in range(1,4):
    for x in range(1,4):

        idx=x+3*(y-1)
        print(x,y,idx)

for z in range(1,4): 
   for y in range(1,4):
    for x in range(1,4):

        idx=x+3*(y-1)+3*3*(z-1)
        #print(x,y,z,idx)

print(P)
print(np.shape(P))



#Q=np.transpose(P,(2, 1, 0))


#print("P[:,:,2] =", Q[0,:,:])

#%%



print("A =", A) 
print("A[0] =", A[0])      # 1st row
print("A[1] =", A[1])      # 2nd row
#print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
#print("A[0][-1] =", A[0][-1])   # Last element of 1st Row


K=np.matrix([[2,1,0],[0,2,2],[2,1,0]])
print(K,A)
# %%

dimAx, dimAy=np.shape(A)
dimKx, dimKy=np.shape(K)

S=np.zeros((dimAx, dimAy))
Kflip=np.zeros((dimKx, dimKy))

for ky in range(0,dimKy):
    for kx in range(0,dimKx): 
        idkx=kx-1 
        idky=ky-1
        Kflip[ky,ky]=K[2-kx,2-ky]
        print(2-kx,2-ky,' | ',idkx, idky,' | ', K[2-kx,2-ky], ' | ', Kflip[kx,ky])
        
        
#print('--')
#print(Kflip)        
                #tmp=tmp+A[x,y]*K[kx,ky]
# %%
A=np.matrix([[3, 3, 2, 1, 0],[0,0,1,3,1],[3,1,2,2,3], 
             [2,0,0,2,2], [2,0,0,0,1]])

for y in range (1,4):
    for x in range(1,4):    
        print(x,y)
        tmp=0
        
        for ky in range(0,dimKy): 
            for kx in range(0,dimKx): 
            
                idkx=kx-1 
                idky=ky-1
                print('---------')
                print(kx,ky,' | ',idkx, idky, ' | ' ,  K[-kx,-ky])
                print( x,y, ' | ',  x+idkx,y+idky, ' | ', A[x+idkx,y+idky])
                #print(kx,ky,K[-kx,-ky])                
                tmp=tmp+A[x+idkx,y+idky]*K[2-kx,2-ky]

        S[x,y]=tmp        
# %%
print('-----------------')
print(A)
print(S) 
print(K)    
from scipy import signal
T = signal.convolve2d(A, K, boundary='symm', mode='same')
print(T)
# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
path='/home/vozenne/Téléchargements/Slicer_Simplified_Mask/2024-11-12-Scene.png'
import PIL.Image
im = PIL.Image.open(path)
imgrey = np.float32(np.array(im.convert('L')))
print(np.shape(im))
print(np.shape(imgrey))

LL=np.matrix([[1,2,1],[2,4,2],[1,2,1]])
LL=np.matrix([[1,2,1],[2,4,2],[1,2,1]])
#LL=np.matrix([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
plt.figure(1)
plt.subplot(121)
plt.imshow(imgrey[0:50,0:50])
test = signal.convolve2d(imgrey, LL, boundary='symm', mode='same')
plt.subplot(122)
plt.imshow(test[0:50,0:50])

# %%
#seconde exercie with 2D convolution for borders.
import numpy as np
import matplotlib.pyplot as plt
B=np.zeros((12,12))
B[0,:]=1
B[1,:]=1
B[:,0]=1
B[:,1]=1
B[11,:]=1
B[11-1,:]=1
B[:,11]=1
B[:,11-1]=1
B[6,6]=1

plt.figure(1)
plt.subplot(131)
plt.imshow(B)

H=np.matrix([[1,1],[1,1]])*0.25
H=np.matrix([[1,-1],[1,-1]])*0.25
H=np.matrix([[1,1],[-1,-1]])*0.25
#H=np.matrix([[1,0],[1,0]])*0.25
#H=np.matrix([[0,1],[0,1]])*0.25
from scipy import signal
output_true=signal.convolve2d(B, H)


def convolve_perso(input, kernel):

    dimIx, dimIy=np.shape(input)
    dimkx, dimky=np.shape(kernel)

    midle=np.int32(np.ceil(dimkx/2))

    output=np.zeros((dimIx-2, dimIy-2))
    for y in range (1,dimIy-1):
        for x in range(1,dimIx-1): 

            #print('####' ,x,y)
            tmp=0
            
            for ky in range(0,dimky): 
                for kx in range(0,dimkx): 
                
                    idkx=kx-1 
                    idky=ky-1
                    #print('---------')
                    #print(kx,ky,' | ',idkx, idky, ' | ' ,  kernel[-kx,-ky])
                    #print( x,y, ' | ',  x+idkx,y+idky, ' | ', input[x+idkx,y+idky])
                    #print(kx,ky,K[-kx,-ky])                
                    tmp=tmp+input[x+idkx,y+idky]*kernel[midle-kx,midle-ky]

            output[x-1,y-1]=tmp  
    return output


output=convolve_perso(B, H)
plt.subplot(132)
plt.imshow(output)
plt.subplot(133)
plt.imshow(output_true)
# %%
```
import matplotlib.pyplot as plt
from skimage import data
import numpy as np
image = data.astronaut()
grey=image = data.astronaut().mean(-1) * 100 + 100
plt.figure(1)
plt.subplot(121)
plt.imshow(grey, cmap='gray')
print(np.shape(image))
```

H=np.matrix([[1,-1],[1,-1]])*0.25
H=np.matrix([[1,1],[-1,-1]])*0.25
output=convolve_perso(grey, H)
plt.subplot(122)
plt.imshow(output, cmap='gray')

# %%

def convolve_perso_corr(input, kernel):

    dimIx, dimIy=np.shape(input)
    dimkx, dimky=np.shape(kernel)

    midle=np.int32(np.ceil(dimkx/2))
    print(midle)

    output=np.zeros((dimIx-2, dimIy-2))
    for y in range (midle,dimIy-midle):
        for x in range(midle,dimIx-midle): 

            #print('####' ,x,y)
            tmp=0
            
            for ky in range(0,dimky): 
                for kx in range(0,dimkx): 
                
                    idkx=kx-midle 
                    idky=ky-midle

                    #if (idkx<0):
                    #    print(kx,midle )
                    #if (idky<0):
                    #    print(ky,midle )    
                    #print('---------')
                    #print(kx,ky,' | ',idkx, idky, ' | ' ,  kernel[-kx,-ky])
                    #print( x,y, ' | ',  x+idkx,y+idky, ' | ', input[x+idkx,y+idky])
                    #print(kx,ky,K[-kx,-ky])                
                    tmp=tmp+input[x+idkx,y+idky]*kernel[kx,ky]

            output[x-1,y-1]=tmp  
    return output

path_bar_code='/home/vozenne/Téléchargements/barcode-49231.png'
from skimage.transform import rescale, resize, downscale_local_mean
import PIL.Image
im = PIL.Image.open(path_bar_code)
img = np.asarray(im)
image_rescaled = rescale(img[:,:,1], 0.25, anti_aliasing=False)
print(np.shape(image_rescaled))

subimg=image_rescaled[120:,:]
#im = np.float32(np.array(im.convert('L')))

plt.figure(1)
plt.subplot(131)
plt.imshow(subimg, cmap='gray')
print(np.shape(subimg))


H=image_rescaled[179:205,39:60]
plt.subplot(132)
plt.imshow(H, cmap='gray')
print(np.shape(H))
output=convolve_perso_corr(subimg, H)
plt.subplot(133)
plt.imshow(output, cmap='gray')
# %%
