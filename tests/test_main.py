from datetime import datetime


def get_file_name(item):
    """Replicates the filename generation logic from main.py."""
    imei = item['imei']
    created_at = item['created_at']
    date_time = datetime.fromtimestamp(int(created_at))
    year = date_time.strftime("%Y")
    month = date_time.strftime("%m")
    item_id = item['id']
    return f"{imei}/{year}/{month}/{item_id}"


def test_file_name_format():
    item = {
        'imei': '123456789',
        'created_at': '1609459200',
        'id': 'abc123',
    }
    date_time = datetime.fromtimestamp(int(item['created_at']))
    expected = f"123456789/{date_time.strftime('%Y')}/{date_time.strftime('%m')}/abc123"
    assert get_file_name(item) == expected


def test_file_name_structure():
    item = {
        'imei': '999',
        'created_at': '0',
        'id': 'test-id',
    }
    result = get_file_name(item)
    parts = result.split('/')
    assert len(parts) == 4
    assert parts[0] == '999'
    assert parts[3] == 'test-id'


def test_file_name_year_month():
    # timestamp 1000000000 = 2001-09-09 01:46:40 UTC
    item = {
        'imei': 'device-1',
        'created_at': '1000000000',
        'id': 'record-42',
    }
    result = get_file_name(item)
    date_time = datetime.fromtimestamp(1000000000)
    assert result.startswith(f"device-1/{date_time.strftime('%Y')}/{date_time.strftime('%m')}/")
    assert result.endswith('/record-42')
