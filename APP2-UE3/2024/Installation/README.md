
# Prerequisites
 
The lecture features several exercises, as well as live demos during which you might wish to follow along the courses. In planning the courses, we assume participants will already have the following:  
 
 - A working python environnement installation (see instructions below).
 - A suite of scientific visualisation software.
 - Python; matplotlib, numpy, scipy.
 - A basic familiarity with linux shell commands.  
 - A comfortable text editor (or IDE) for Python etc.
   
## Mandatory visualisation softwares
 
 - [Paraview](https://www.paraview.org/)
 - [3DSlicer](https://www.slicer.org/)
 - [itksnap](http://www.itksnap.org/pmwiki/pmwiki.php)
  
## A comfortable text editor

- [vscode](https://code.visualstudio.com/)
- [jupyter-notebook](https://jupyter.org/)

## A working python environement

Such as pip or conda.

I use python or virtual python  environments with pip so I will only document this one.

```
# create a folder
mkdir /somewhere/imaging-processing-course/
cd /somewhere/imaging-processing-course/

# create and activate a virtual python environments
python3 -m venv venv-imaging-course 
activate venv-imaging-course/bin/activate
# install a few library
pip install numpy pyvista pydicom simpleITK pynrrd 
pip install scikit-learn matplotlib
```