import numpy as np

def pose_candidates_from_E(E):
  transform_candidates = []
  ##Note: each candidate in the above list should be a dictionary with keys "T", "R"
  """ YOUR CODE HERE
  """

  #for positive E

#check E determinant LS.bd) that det (Wh) 20

  U_ini, s_ini, Vh_ini = np.linalg.svd(E, full_matrices = True)

  if np.linalg.det(U_ini @ Vh_ini) < 0:
    E = -E
    print("triggered")

  U, s, Vh = np.linalg.svd(E, full_matrices = True)

  V = Vh.T

  S = np.diag(s)

  Rz_2pi_p =  [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
  Rz_2pi_p = np.array(Rz_2pi_p)

  Rz_2pi_n = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
  Rz_2pi_n = np.array(Rz_2pi_n)

  R1 = np.dot(U, np.dot(Rz_2pi_p.T, V.T))
  R2 = np.dot(U, np.dot(Rz_2pi_n.T, V.T))
  
  T1 = U[:,2]
  T2 = U[:,2]

  #for negative E

  U1, s1, Vh1 = np.linalg.svd(E, full_matrices=True)

  V1 = Vh1.T

  S1 = np.diag(s1)

  R11 = np.dot(U1, np.dot(Rz_2pi_p.T, V1.T))
  R22 = np.dot(U1, np.dot(Rz_2pi_n.T, V1.T))
  
  T11 = -U1[:,2]
  T22 = -U1[:,2]

  canidatel = {}
  canidatel['T'] = T1
  canidatel['R'] = R1
  transform_candidates.append(canidatel)

  canidate2 = {}
  canidate2['T'] = T2
  canidate2['R'] = R2
  transform_candidates.append(canidate2)

  canidate11 = {}
  canidate11['T'] = T11
  canidate11['R'] = R11
  transform_candidates.append(canidate11)

  canidate22 = {}
  canidate22['T'] = T22
  canidate22['R'] = R22
  transform_candidates.append(canidate22)
  """ END YOUR CODE
  """
  return transform_candidates