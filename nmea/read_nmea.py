import os

def read_data(file_path):

    gga_lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f):
            line = line.strip()
            if line.startswith(("$GPGGA", "$GNGGA", "$GLGGA", "$GAGGA")):
                gga_lines.append(line)
            if idx >= 999:
                break
    return gga_lines

def convert_to_decimal_degrees(degmin_str, direction):

    if degmin_str == '':
        return None

    # 경도: DDDMM, 위도: DDMM 구분 처리
    if len(degmin_str.split('.')[0]) > 4:
        degrees = int(degmin_str[:3])
        minutes = float(degmin_str[3:])
    else:
        degrees = int(degmin_str[:2])
        minutes = float(degmin_str[2:])

    decimal_degrees = degrees + minutes / 60

    # 남반구(S)나 서경(W)일 경우 음수로 변환
    if direction in ['S', 'W']:
        decimal_degrees = -decimal_degrees

    return decimal_degrees

def main():

    file_path = "/home/gonglini/practice/nmea/nmea.txt"

    if not os.path.exists(file_path):
        print(f"'{file_path}' 파일이 현재 경로에 존재하지 않습니다.")
        return

    gga_lines = read_data(file_path)

    if not gga_lines:
        print("GGA 데이터를 찾을 수 없습니다.")
        return

    print(f"총 {len(gga_lines)}개의 GGA 데이터를 읽었습니다.\n")

    for idx, gga in enumerate(gga_lines, start=1):
        print(f"[{idx}] {gga}")


if __name__ == "__main__":
    main()
