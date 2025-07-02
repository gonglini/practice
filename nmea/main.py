import pyproj
from read_nmea import convert_to_decimal_degrees, read_data


def parse_and_print_gga_line(line, proj_utm):

    parts = line.split(',')

    lat_dd = convert_to_decimal_degrees(parts[2], parts[3])
    lon_dd = convert_to_decimal_degrees(parts[4], parts[5])

    if lat_dd is not None and lon_dd is not None:
        easting, northing = proj_utm(lon_dd, lat_dd)
    else:
        easting, northing = None, None


    print(f"GGA_raw_data: {line}")
    print(f"GGA_message_id: {parts[0]}")
    print(f"GGA_utc: {parts[1]}")
    print(f"GGA_lat: {parts[2]}")
    print(f"GGA_lat_dir: {parts[3]}")
    print(f"GGA_lon: {parts[4]}")
    print(f"GGA_lon_dir: {parts[5]}")
    print(f"GGA_quality: {parts[6]}")
    print(f"GGA_num_satellite: {parts[7]}")
    print(f"GGA_HDOP: {parts[8]}")
    print(f"GGA_alt: {parts[9]} {parts[10]}")
    print(f"GGA_sep: {parts[11]} {parts[12]}")
    print(f"GGA_diff_age: {parts[13]}")

    if len(parts) > 14:
        if '*' in parts[14]:
            diff_station, checksum = parts[14].split('*')
        else:
            diff_station, checksum = parts[14], ''
    else:
        diff_station, checksum = '', ''

    print(f"GGA_diff_station: {diff_station}")
    print(f"GGA_check_sum: {checksum}")
    print(f"lat_decimal_deg: {lat_dd}")
    print(f"lon_decimal_deg: {lon_dd}")
    print(f"UTM_easting: {easting}")
    print(f"UTM_northing: {northing}")
    print("-" * 60)


def main():
    file_path = "/home/gonglini/practice/nmea/nmea.txt"
    gga_lines = read_data(file_path)

    proj_utm = pyproj.Proj(proj='utm', zone=52, ellps='WGS84', south=False)

    for line in gga_lines:
        parse_and_print_gga_line(line, proj_utm)


if __name__ == "__main__":
    main()
