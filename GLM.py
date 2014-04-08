from pylab import *
import math
import numpy as np

def line(x,w):
    """ returns "y" value from coefficients """
    return -(w[1]/w[2])*x - (w[0]/w[2])

def sigmoid(x):
    return 1/(1 + math.exp(-x))

def dE(w,X,t):
    """ returns a VECTOR that contains partial derivatives of Error function  """
    size = X.shape[1]
    y = np.array([sigmoid(i) for i in w.dot(X)])
    R = np.eye(size)
    for i in range(size):
        R[i][i] *= y[i]*(1-y[i])

    dw = ((y - t).dot(R)).dot(X.T)
    return dw

def learn(w,X,t):
    """ Perform gradient descent for "size" times. """
    size = X.shape[1]
    alpha = 0.5
    beta = 0.98
    for i in range(size):
        w = w - alpha * dE(w,X,t)
        alpha = alpha * beta
    return w


        
if __name__ == "__main__":
    X = np.array([[1,1,1,1,1,1,1,1,1,1],
                  [1,2,3,3,4,0,1,2,3,4],
                  [3,2,2,3,1,2,1,1,0,0]])

    t = np.array([1,1,1,1,1,0,0,0,0,0])
    
    # Initial weights are set to zeros.
    w = np.zeros(3,dtype=np.float)
    
    # Plot each points.
    for i in range(X.shape[1]):
        if t[i] == 1:
            plot(X[1][i],X[2][i],"go")
        else:
            plot(X[1][i],X[2][i],"ro")
            
    # Learn one time to generate the next decision boundary.
    nw = learn(w,X,t)

    # For plotting lines.
    xaxis = arange(-2.0, 6.0, 0.05)

    # Learn more if the weight vector still changes.
    while(np.linalg.norm(w-nw)/np.linalg.norm(w) > 0.01):
          w = nw
          nw = learn(w,X,t)
          # Draw locuses of decision boundary with magenta dots.
          plot(xaxis,line(xaxis,w),"m:",lw = 0.4) 

    # Final decision boundary with black line.
    print w
    plot(xaxis,line(xaxis,w),"k-",lw=1)

    # Graph options.
    title('Logistic Regression')
    xlabel('x1')
    ylabel('x2')
    gca().set_xlim(-1,5)
    gca().set_ylim(-1,4)
    
    # Show the graph.
    show()
