def calculate_average_mbit_per_seconds(speed_in_seconds, file_size_description):
    if file_size_description == '100MB':
        return calculate_with_bits(speed_in_seconds, 838860800)
    if file_size_description == '1GB':
        return calculate_with_bits(speed_in_seconds, 8589934592)


def calculate_with_bits(speed_in_seconds, file_size_in_bits):
    if speed_in_seconds == 0:
        return 0
    return (file_size_in_bits / speed_in_seconds)/1000/1000
