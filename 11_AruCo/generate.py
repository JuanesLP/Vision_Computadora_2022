from PyQt5.QtCore import QLibraryInfo
import os
# from PySide2.QtCore import QLibraryInfo

import cv2 as cv

os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = QLibraryInfo.location(
    QLibraryInfo.PluginsPath
)

import numpy as np

# Cargamos el diccionario predefinido
diccionario = cv.aruco.Dictionary_get(cv.aruco.DICT_6X6_250)

# Generamos el marcador
imagen = np.zeros((200, 200), dtype=np.uint8)
imagen = cv.aruco.drawMarker(diccionario, 33, 200,
                             imagen, 1);

cv.imwrite("marker33.png", imagen);
cv.imshow("ventana", imagen);
cv.waitKey(0)
cv.destroyAllWindows()
