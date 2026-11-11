# ════════════════════════════════════════════════════════════════
#  FEAScript Benchmark
#  Finite Element Simulation in JavaScript
#  https://github.com/FEAScript/FEAScript-benchmark
#  MIT License © 2026 FEAScript
# ════════════════════════════════════════════════════════════════

"""Read the point data of a VTU file that Elmer's ResultOutputSolver writes in binary.

The binary format (Elmer's default) stores the values as raw IEEE doubles in an appended block, so they keep
full double precision. Elmer's ASCII format writes 8 significant digits, so the benchmarks do not use it.
"""
import re
import numpy as np

TYPES = {"Float64": "<f8", "Float32": "<f4", "Int32": "<i4", "Int64": "<i8", "UInt32": "<u4", "UInt64": "<u8"}


def read_vtu(path):
    """Return the point coordinates, an (n, 3) array, and a dict of the point data arrays by name."""
    raw = open(path, "rb").read()
    start = raw.find(b"<AppendedData")
    if start < 0:
        raise ValueError(f"{path}: no binary (appended) data, set Ascii Output = False in the .sif")
    header = raw[:start].decode()
    data = raw[raw.index(b"_", start) + 1:]  # the raw data starts after the underscore
    size_type = TYPES[(re.search(r'header_type="(\w+)"', header) or [None, "UInt32"])[1]]
    size_bytes = np.dtype(size_type).itemsize

    def block(tag):
        attrs = dict(re.findall(r'(\w+)="([^"]*)"', tag))
        if attrs.get("format") != "appended":
            raise ValueError(f"{path}: expected binary (appended) data, found format=\"{attrs.get('format')}\"")
        offset = int(attrs["offset"])
        nbytes = int(np.frombuffer(data, size_type, 1, offset)[0])
        values = np.frombuffer(data, TYPES[attrs["type"]], nbytes // np.dtype(TYPES[attrs["type"]]).itemsize, offset + size_bytes)
        ncomp = int(attrs.get("NumberOfComponents", 1))
        return attrs.get("Name"), values.reshape(-1, ncomp) if ncomp > 1 else values

    points = block(re.search(r"<Points>\s*(<DataArray[^>]*>)", header).group(1))[1]
    point_data = re.search(r"<PointData>(.*?)</PointData>", header, re.S).group(1)
    return points, dict(block(tag) for tag in re.findall(r"<DataArray[^>]*>", point_data))
