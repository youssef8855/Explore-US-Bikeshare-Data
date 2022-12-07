import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city= input('Please choose the city you want to get data about for the following "chicago, new york city, washington": ').lower()
    while city not in ['chicago','new york city','washington']:
         print('Invalid city name, Please choose one of the given cities')
         city= input('Please choose the city you want to get data about for the following "chicago, new york city, washington": ').lower()
        # TO DO: get user input for month (all, january, february, ... , june)
    month= input('Please choose the month you want to get data about "from january to June or all": ').lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june','all']:
        print('Invalid month name, Please choose one from january to June or all')
        month= input('Please choose the month you want to get data about "from january to June or all": ').lower()
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day= input('Please choose the day you want to get data about or all: ').lower()
    while day not in ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']:
        print('Invalid day name, Please writh the name correctly')
        day= input('Please choose the day you want to get data about or all: ').lower()
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is "{}".'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('The most common day of week is "{}".'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    df['day_hour'] = df['Start Time'].dt.hour
    print('The most common day hour is "{}"'.format(df['day_hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is "{}"'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most common end station is "{}"'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + "-" + df['End Station']
    print('The most frequent combination of start station and end station trip is "{}"'.format(df['combination'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total traveling time is "{}sec"'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('the average traveling time is "{}sec"'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('user type:', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if city != 'washington':
        print(df['Gender'].value_counts().to_frame())

    # TO DO: Display earliest, most recent, and most common year of birth
        print('The earliest birth year is "{}"'.format(int(df['Birth Year'].min())))
        print('The most recent birth year is "{}"'.format(int(df['Birth Year'].max())))
        print('The most common birth year is "{}"'.format(int(df['Birth Year'].mode()[0])))
    else:
        print('this option is not availabe for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    """ Five lines of data are shown to the user (if he wants) to explore,
    the display of five new lines is renewed in case the user desires and stops upon rejection """
    i = 0
    raw = (input("Would you like to review the data? yes/no \n")).lower()
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:i+5]) 
            raw = (input("Would you like to review more data? yes/no \n")).lower()
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
