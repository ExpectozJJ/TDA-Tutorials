from ripser import ripser
import numpy as np
import gudhi as gd
# import cechmate as cm
import math
import scipy.io as sio

def Ripser(pdb_id, thresh):
    # thresh is the threshold of filtration parameter
    data = np.load(pdb_id+".npz", allow_pickle=True)

    data = data['PRO']

    for pro in data:
        typ = pro['typ']
        pos = pro['pos']

    rc = ripser(np.array(pos), maxdim=3, thresh=thresh)['dgms']
    sio.savemat(pdb_id+"_rips.mat", {"betti0": rc[0], "betti1": rc[1], "betti2": rc[2], "betti3": rc[3]})

# def alpha_complex(pdb_id):
#     # Using cechmate library 
#     data = np.load(pdb_id+".npz", allow_pickle=True)

#     for pro in data['PRO']:
#         protyp = pro['typ']
#         propos = pro['pos']

#     alpha = cm.Alpha()
#     filtration = alpha.build(propos) 
#     dgmsalpha = alpha.diagrams(filtration)

#     betti0, betti1, betti2 = dgmsalpha[0], dgmsalpha[1], dgmsalpha[2]

#     # Multiplying by 2 since here the filtration parameter is radius
#     betti0 = np.array(betti0)*2
#     betti1 = np.array(betti1)*2
#     betti2 = np.array(betti2)*2
#     betti = [betti0, betti1, betti2]

#     betti0 = sorted(betti[0], key=lambda x: x[0])
#     betti0 = np.flip(betti0, axis=0)
#     betti1 = sorted(betti[1], key=lambda x: x[0])
#     betti1 = np.flip(betti1, axis=0)
#     betti2 = sorted(betti[2], key=lambda x: x[0])
#     betti2 = np.flip(betti2, axis=0)

#     sio.savemat(pdb_id+"_alpha.mat", {"betti0": betti0, "betti1": betti1, "betti2": betti2})

def gudhi_alpha(pdb_id):

    #data = np.load(pdb_id+".npz", allow_pickle=True)
    data = np.load("C60.npz", allow_pickle=True)

    for pro in data['PRO']:
        protyp = pro['typ']
        propos = pro['pos']
    
    ac = gd.AlphaComplex(propos)
    st = ac.create_simplex_tree()
    dgmsalpha = st.persistence()

    betti0, betti1, betti2 = [], [], []
    for r in dgmsalpha:
        if r[0] == 0:
            betti0.append([r[1][0], r[1][1]])
        elif r[0] == 1:
            betti1.append([r[1][0], r[1][1]])
        elif r[0] == 2:
            betti2.append([r[1][0], r[1][1]])
    
    # Using circumradius, we take sqrt of F and multiply by 2  
    betti0 = np.array(np.sqrt(betti0)*2)
    betti1 = np.array(np.sqrt(betti1)*2)
    betti2 = np.array(np.sqrt(betti2)*2)
    betti = [betti0, betti1, betti2]

    betti0 = sorted(betti[0], key=lambda x: x[0])
    betti0 = np.flip(betti0, axis=0)
    betti1 = sorted(betti[1], key=lambda x: x[0])
    betti1 = np.flip(betti1, axis=0)
    betti2 = sorted(betti[2], key=lambda x: x[0])
    betti2 = np.flip(betti2, axis=0)

    # sio.savemat(pdb_id+"_gdalpha.mat", {"betti0": betti0, "betti1": betti1, "betti2": betti2})

gudhi_alpha("C60")
Ripser("C60", 2)
    
    
    
    
    