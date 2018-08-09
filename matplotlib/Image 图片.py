# Author:Patrick
import numpy as np
import matplotlib.pyplot as plt

a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3, 3)
plt.imshow(a, interpolation='nearest', cmap='bone', origin='upper')  # 最大值在右下
# origin='lower'代表的就是选择的原点的位置
# https://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html 选择interpolation

plt.colorbar(shrink=.92)

plt.xticks(())
plt.yticks(())
plt.show()
