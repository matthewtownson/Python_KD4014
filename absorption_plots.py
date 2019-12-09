import sys
import pandas
import numpy
import matplotlib.pyplot

data = numpy.loadtxt(fname=sys.argv[1], delimiter=',')
wavelengths = pandas.read_csv(sys.argv[2],usecols=[0],header=None).to_numpy()

data_slice = data[:,650:800]
wavelength_slice = wavelengths[650:800]

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(wavelength_slice,numpy.mean(data_slice, axis=0))

axes2.set_ylabel('max')
axes2.plot(wavelength_slice,numpy.max(data_slice, axis=0))

axes3.set_ylabel('min')
axes3.plot(wavelength_slice,numpy.min(data_slice, axis=0))

fig.tight_layout()

matplotlib.pyplot.savefig('./group_plot.png')

matplotlib.pyplot.show()
