from pylab import *
subplot(1,4,1)
tick_params(top='on',bottom='off',left='off',right='off')

subplot(1,4,2)
tick_params(top='off',bottom='on',left='off',right='off')

subplot(1,4,3)
tick_params(top='off',bottom='off',left='on',right='off')

subplot(1,4,4)
tick_params(top='off',bottom='off',left='off',right='on')

show()