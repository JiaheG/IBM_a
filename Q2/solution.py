def read_data():
    records = []
    N = int(input())
    for i in range(N):
        # Read standard input
        record = input()
        if "false" in record:
            records.append({"isValid": False, "errorCode": record.split("false ", 1)[1]})
        else:
            records.append({"isValid": True})
    return records

    
def check_validity(records):
    all_valid = True
    error_codes = []
    for record in records:
        if not record["isValid"]:
            all_valid = False
            error_codes.append(record["errorCode"])

    if all_valid:
        print("Yes")
        return True, []

    else:
        print("No")
        print(*error_codes)
        return False, error_codes

# 1 false ERR_OOM
# 2 true
# 3 false ERR_TIME_OUT
# 4 true
# 5 true
records = read_data()
valid, errors = check_validity(records)
