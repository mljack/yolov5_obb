import os
import math
import numpy as np


def obb_to_pts(label):
    v_type, x, y, length, width, yaw = label
    c = np.array((x, y))
    yaw = math.radians(-yaw)
    dir = np.array((math.cos(yaw), math.sin(yaw)))
    normal = np.array((-math.sin(yaw), math.cos(yaw)))
    return np.array([
        c - 0.5*length*dir - 0.5*width*normal,
        c - 0.5*length*dir + 0.5*width*normal,
        c + 0.5*length*dir + 0.5*width*normal,
        c + 0.5*length*dir - 0.5*width*normal,
    ])


def convert(src_label_path):
    dst_label_path = src_label_path.replace("labels", "labelTxt")
    if not os.path.exists(dst_label_path):
        os.mkdir(dst_label_path)

    for item in os.listdir(src_label_path):
        src_path = os.path.join(src_label_path, item)
        dst_path = os.path.join(dst_label_path, item)
        if not src_path.endswith(".txt"):
            continue
        print(src_path)
        f2 = open(dst_path, "w")
        with open(src_path) as f:
            lines = f.readlines()
        for line in lines:
            label = [float(s) for s in line.strip().split(" ")]
            pts = obb_to_pts(label)
            poly = pts.reshape((8,)).tolist()
            poly_str = " ".join([f"{v:.2f}" for v in poly])
            f2.write(f"{poly_str} vehicle 1\n")
        f2.close()

src_paths = [
    #"data/eagle/0001_shijidadao_20200907_1202_200m_fixed_tiny/train/labelTxt_old",
    #"data/eagle/0011_private170/labelTxt_old",

    "data/eagle/0001_shijidadao_20200907_1202_200m_fixed/train/labels",
    "data/eagle/0001_shijidadao_20200907_1202_200m_fixed/val/labels",
    "data/eagle/0002_tongji_011/train/labels",
    "data/eagle/0002_tongji_011/val/labels",
    "data/eagle/0003_changtai_20200903_1205_250m_fixed/train/labels",
    "data/eagle/0003_changtai_20200903_1205_250m_fixed/val/labels",
    "data/eagle/0004_jinqiao_20200907_1104_200m_fixed/train/labels",
    "data/eagle/0004_jinqiao_20200907_1104_200m_fixed/val/labels",
    "data/eagle/0005_ysq1/train/labels",
    "data/eagle/0005_ysq1/val/labels",
    "data/eagle/0006_syq4/train/labels",
    "data/eagle/0006_syq4/val/labels",
    "data/eagle/0007_gm7/train/labels",
    "data/eagle/0007_gm7/val/labels",
    "data/eagle/0011_private170/labels",
    "data/eagle/0012_web-collection-003_dataset/train/labels",
    "data/eagle/0012_web-collection-003_dataset/val/labels",
    "data/eagle/0013_longyaolu_dji/train/labels",
    "data/eagle/0013_longyaolu_dji/val/labels",
    "data/eagle/0014_longyaolu_c1000e/train/labels",
    "data/eagle/0014_longyaolu_c1000e/val/labels",
]

for src_path in src_paths:
    convert(src_path)
