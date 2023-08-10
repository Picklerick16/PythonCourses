def main():
    middle_endian_date = list(input("Date: "))
    format_date(middle_endian_date)

def format_date(unformatted_date):
    months = {
        'December': '12',
        'November': '11',
        'October': '10',
        'September': '09',
        'August': '08',
        'July': '07',
        'June': '06',
        'May': '05',
        'April': '04',
        'March': '03',
        'February': '02',
        'January': '01'
    }

    # Join the list back into a string
    unformatted_date = ''.join(unformatted_date)
    
    # Split date into month, day, and year
    if "/" in unformatted_date:
        parts = unformatted_date.split("/")
    elif " " in unformatted_date:
        parts = unformatted_date.split(" ")
    
    month = parts[0]
    day = parts[1]
    year = parts[2]
    
    # Convert month to correct format
    if month in months:
        month = months[month]
        print(month)
    
    # Add extra zeroes if necessary
    day = day.zfill(2)
    month = month.zfill(2)
    year = year.zfill(4)

    # Combine date into correct format
    formatted_date = day + "/" + month + "/" + year
    print(formatted_date)

if __name__ == "__main__":
    main()
