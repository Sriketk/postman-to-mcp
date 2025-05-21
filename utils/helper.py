from datetime import datetime

def is_datetime(date_str):
    known_formats = [
        "%Y-%m-%d",
        "%d-%m-%Y",
        "%m/%d/%Y",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%SZ",
        "%d %b %Y",
        "%B %d, %Y",
        "%Y/%m/%d %H:%M",
        "%m-%d-%Y",
        "%Y.%m.%d"
    ]
    
    for fmt in known_formats:
        try:
            datetime.strptime(date_str, fmt)
            return True
        except ValueError:
            continue
    return False
    
def get_datetime_format(date_str):
    known_formats = [
        "%Y-%m-%d",
        "%d-%m-%Y",
        "%m/%d/%Y",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%SZ",
        "%d %b %Y",
        "%B %d, %Y",
        "%Y/%m/%d %H:%M",
        "%m-%d-%Y",
        "%Y.%m.%d"
    ]
    
    for fmt in known_formats:
        try:
            datetime.strptime(date_str, fmt)
            return fmt
        except ValueError:
            continue
    return None

def format_literal_type(values):
    if not values:
        return None  # or return "" if you prefer empty string

    cleaned = [v for v in values if v and v.strip()]
    if not cleaned:
        return None

    return 'Literal[' + ', '.join(f'"{v}"' for v in cleaned) + ']'
