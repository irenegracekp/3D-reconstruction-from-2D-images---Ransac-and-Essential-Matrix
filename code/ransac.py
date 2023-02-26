from lse import least_squares_estimation
import numpy as np

def ransac_estimator(X1, X2, num_iterations=60000):
    sample_size = 8

    eps = 10**-4

    best_num_inliers = -1
    best_inliers = None
    best_E = None

    for i in range(num_iterations):
        # permuted_indices = np.random.permutation(np.arange(X1.shape[0]))
        permuted_indices = np.random.RandomState(seed=(i*10)).permutation(np.arange(X1.shape[0]))
        sample_indices = permuted_indices[:sample_size]
        test_indices = permuted_indices[sample_size:]

        """ YOUR CODE HERE
        """

        sample_x1 = []
        sample_x2 = []

        for i in range(sample_size) :
          sample_x1.append(X1[sample_indices[i]]) 
          sample_x2.append(X2[sample_indices[i]])

        sample_x1 = np.array(sample_x1)
        sample_x2 = np.array(sample_x2)

        #find the B matrix
          
        E = least_squares_estimation(sample_x1, sample_x2)
        
        #find distance of matching points 
        skew_e3 = np.array([[0, -1, 0],[1, 0, 0],[0, 0, 0]])
      
        inliers = sample_indices
        for j in test_indices: 
          test_x1 = X1[j] 
          test_x2 = X2[j] 

          d1 = (test_x2.T @ E @ test_x1)*(test_x2.T @ E @ test_x1)
          denorm21 = np.linalg.norm(skew_e3 @ E @ test_x1) * np.linalg.norm(skew_e3 @ E @ test_x1)
          d1 = d1/denorm21 

          d2 = (test_x1.T @ E.T @ test_x2)*(test_x1.T @ E.T @ test_x2)
          denorm12 = np.linalg.norm(skew_e3 @ E.T @ test_x2) * np.linalg.norm(skew_e3 @ E.T @ test_x2)
          d2 = d2/denorm12
          residual = d1 + d2
          
          if residual < eps: 
            inliers = np.append(inliers, j) 
            
        """ END YOUR CODE
        """
        if inliers.shape[0] > best_num_inliers:
            best_num_inliers = inliers.shape[0]
            best_E = E
            best_inliers = inliers

    print(np.shape(best_inliers))
    return best_E, best_inliers