import os
import ee

ee.Initialize()

from datasets.glad_gfc_raw import gfc 

template_image_1 = gfc # imported from elsewhere so using a common asset defined once (could also use ee.Image("UMD/hansen/global_forest_change_2022_v1_10")