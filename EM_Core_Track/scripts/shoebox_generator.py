def generate_shoebox(length, width, height, zone_name="Shoebox"):
    return {
        "zone": zone_name,
        "geometry": {
            "length": length,
            "width": width,
            "height": height,
        },
        "envelope": {
            "u_wall": 0.05,
            "u_window": 0.3,
            "shgc": 0.25
        }
    }
