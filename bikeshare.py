import time
import pandas as pd


CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def sleep(msg):
    print(msg)
    time.sleep(1)


def get_city():
    city0 = ''
    choice1 = input("please choose the city 1 for chicago, 2 for"
                    "new york city, 3 for washington \n")
    if choice1 == '1':
        city0 = 'chicago'
    elif choice1 == '2':
        city0 = 'new york city'
    elif choice1 == '3':
        city0 = 'washington'
    else :
        get_city()
    
    print(city0)
    return city0


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all"
        to apply no month filter
        (str) day - name of the day of week to filter by, or "all"
        to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    
    
    city = get_city()
    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = ''
    while month not in months:
        month = input("Which month 'all', 'january', 'february', 'march',"
                      "'april', 'may'or 'june' \n").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day not in ['all', 'monday', 'tuesday', 'wednesday',
                      'thursday', 'friday', 'saturday', 'sunday']:
        day = input("Which day 'all', 'monday', 'tuesday', 'wednesday',"
                    "'thursday', 'friday', 'saturday', 'sunday' \n").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day
    if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no
        month filter
        (str) day - name of the day of week to filter by, or "all" to apply
        no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start month : => ', popular_month)

    # display the most common day of week
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]
    print('Most Popular Start day : => ', popular_day)

    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour : => ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    sleep('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('display most commonly used start station : => ', start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('display most commonly used end station : => ', end_station)

    # display most frequent combination of start station and end station trip
    both_station = df['Start Station'] + ' : => ' + df['End Station']
    both = both_station.mode()[0]
    print('display most commonly used both station : => ', both)

    print("\nThis took %s seconds." % (time.time() - start_time))
    sleep('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total = df['Trip Duration'].sum()
    print('Total travel time : =>', total)

    # display mean travel time
    mean = df['Trip Duration'].mean()
    print('Mean travel time : =>', mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    sleep('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    if city != 'washington':
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        user = df.groupby(['User Type'])['User Type'].count()
        print('counts of user types : =>', user)
        print('-'*40)

        # Display counts of gender
        user = df.groupby(['Gender'])['Gender'].count()
        print('counts of gender : =>', user)
        print('-'*40)

        # Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        print('earliest year of birth : =>', earliest)

        most_recent = df['Birth Year'].max()
        print('earliest year of birth : =>', most_recent)

        common_year = df['Birth Year'].mode()
        print('earliest year of birth : =>', common_year)

        print("\nThis took %s seconds." % (time.time() - start_time))
        sleep('-'*40)


def show(df):
    flag = ''
    start = 0
    end = 5
    while True:
        flag = input("Do you want to see more data .. enter"
                     "'y' or 'n' ").lower()
        if flag == 'y':
            data = df.iloc[start:end]
            print(data)
            start += 5
            end += 5
        else:
            break
    while True:
        restart = input('\nWould you like to restart? Enter \'y\' or \'n\'.\n')
        if restart.lower() == 'y':
            main()
        else:
            break


def main():
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        show(df)


if __name__ == "__main__":
	main()
