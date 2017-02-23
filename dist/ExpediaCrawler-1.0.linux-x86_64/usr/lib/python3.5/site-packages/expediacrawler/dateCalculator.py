from datetime import datetime
from datetime import timedelta


def calculate_new_dates(orig_leave_str, orig_return_str, offset):
    leave_date = datetime.strptime(orig_leave_str, "%m/%d/%Y").date()
    back_date = datetime.strptime(orig_return_str, "%m/%d/%Y").date()
    out_date = leave_date + timedelta(days=offset)
    return_date = back_date + timedelta(days=offset)
    out_str = out_date.strftime('%m/%d/%Y')
    return_str = return_date.strftime('%m/%d/%Y')
    return out_str, return_str
