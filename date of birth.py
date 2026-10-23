months = ('Jan', 'Feb', 'March', 'April', 'May', 'June',
          'July', 'Aug', 'September', 'October', 'November', 'December');

endings = ('st', 'nd', 'rd') + 17 * ('th',) + ('st', 'nd', 'rd') + 7 * ('th',) + ('st',);

Year = input("Enter the Year: ");
Month = input("Enter the month: ");
Day = input("Enter The Day: ");

month_number = int(Month);
day_number = int(Day);

month_name = months[month_number-1]
ordinal = Day + endings[day_number-1]

print(month_name + " " + ordinal + ", " + Year);
input("press <Enter>")
