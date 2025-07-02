import os
import pyproj

def read_data(file_path):
    """GGA raw line만 리스트로 반환"""
    gga_lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f):
            line = line.strip()
            if line.startswith(("$GPGGA", "$GNGGA", "$GLGGA", "$GAGGA")):
                gga_lines.append(line)
            if idx >= 999:
                break
    return gga_lines

def convert_to_decimal_degrees(ddmm_mmmm, direction):
    """DDMM.MMMM -> Decimal Degrees 변환"""
    if ddmm_mmmm == '':
        return None
    # 위도 (DDMM), 경도 (DDDMM) 자동 처리
    if len(ddmm_mmmm.split('.')[0]) > 4:
        degrees = int(ddmm_mmmm[:3])
        minutes = float(ddmm_mmmm[3:])
    else:
        degrees = int(ddmm_mmmm[:2])
        minutes = float(ddmm_mmmm[2:])
    decimal_degrees = degrees + minutes / 60
    if direction in ['S', 'W']:
        decimal_degrees = -decimal_degrees
    return decimal_degrees

def parse_and_print_gga_line(line, proj_utm):
    """GGA 라인을 파싱하여 보기 좋게 출력"""
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
        diff_station, checksum = parts[14].split('*') if '*' in parts[14] else (parts[14], '')
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
    file_path = "nmea.txt"
    gga_lines = read_data(file_path)

    proj_utm = pyproj.Proj(proj='utm', zone=52, ellps='WGS84', south=False)

    for line in gga_lines:
        parse_and_print_gga_line(line, proj_utm)

if __name__ == "__main__":
    main()
